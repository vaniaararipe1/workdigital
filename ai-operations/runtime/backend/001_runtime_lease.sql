-- Apply only to the confirmed Control Plane Supabase database.
-- No dispatcher is enabled by this migration.
begin;

create table public.wd_runtime_operators (
  user_id uuid primary key references auth.users(id) on delete cascade
);
create table public.wd_runtime_lease (
  singleton boolean primary key default true check (singleton),
  version bigint not null default 0 check (version between 0 and 9007199254740991),
  owner text,
  principal uuid,
  acquired_at timestamptz,
  expires_at timestamptz,
  check ((owner is null and principal is null and acquired_at is null and expires_at is null)
    or (owner is not null and principal is not null and acquired_at is not null and expires_at is not null
      and expires_at > acquired_at and length(btrim(owner)) between 1 and 200))
);
insert into public.wd_runtime_lease(singleton) values(true);
create table public.wd_runtime_lease_audit (
  version bigint primary key,
  previous_version bigint not null,
  previous_owner text,
  owner text,
  principal uuid not null,
  request_owner text not null,
  occurred_at timestamptz not null,
  acquired_at timestamptz,
  expires_at timestamptz
);
alter table public.wd_runtime_operators enable row level security;
alter table public.wd_runtime_lease enable row level security;
alter table public.wd_runtime_lease_audit enable row level security;
revoke all on public.wd_runtime_operators, public.wd_runtime_lease,
  public.wd_runtime_lease_audit from public, anon, authenticated;

create function public.wd_read_runtime_lease() returns jsonb
language plpgsql security definer set search_path = '' as $$
declare v public.wd_runtime_lease%rowtype;
begin
  if auth.uid() is null or not exists (
    select 1 from public.wd_runtime_operators where user_id=auth.uid()
  ) then raise exception 'Runtime operator required' using errcode='42501'; end if;
  select * into strict v from public.wd_runtime_lease where singleton=true;
  return jsonb_build_object('version',v.version,'owner',v.owner,
    'acquired_at',v.acquired_at,'expires_at',v.expires_at);
end;
$$;

create function public.wd_cas_runtime_lease(
  p_expected_version bigint, p_request_owner text, p_next jsonb
) returns jsonb language plpgsql security definer set search_path = '' as $$
declare
  v public.wd_runtime_lease%rowtype;
  v_now timestamptz;
  v_owner text;
  v_acquired timestamptz;
  v_expires timestamptz;
begin
  if auth.uid() is null or not exists (
    select 1 from public.wd_runtime_operators where user_id=auth.uid()
  ) then raise exception 'Runtime operator required' using errcode='42501'; end if;
  if p_expected_version is null or p_expected_version < 0
    or p_expected_version >= 9007199254740991
    or p_request_owner is null or length(btrim(p_request_owner)) not between 1 and 200
    or p_next is null or jsonb_typeof(p_next) <> 'object'
    or not (p_next ?& array['version','owner','acquired_at','expires_at'])
    or jsonb_typeof(p_next->'version') <> 'number'
    or (p_next->>'version')::numeric <> p_expected_version+1
  then raise exception 'Invalid lease document' using errcode='22023'; end if;
  if p_next->'owner' <> 'null'::jsonb and jsonb_typeof(p_next->'owner') <> 'string'
  then raise exception 'Invalid owner' using errcode='22023'; end if;
  v_owner := p_next->>'owner';
  if v_owner is not null then
    if v_owner <> p_request_owner or length(btrim(v_owner)) not between 1 and 200
      or jsonb_typeof(p_next->'acquired_at') <> 'string'
      or jsonb_typeof(p_next->'expires_at') <> 'string'
      or (p_next->>'acquired_at') !~ '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}[.][0-9]{3}Z$'
      or (p_next->>'expires_at') !~ '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}[.][0-9]{3}Z$'
    then raise exception 'Invalid acquisition' using errcode='22023'; end if;
    v_acquired := (p_next->>'acquired_at')::timestamptz;
    v_expires := (p_next->>'expires_at')::timestamptz;
    if not isfinite(v_acquired) or not isfinite(v_expires)
      or v_expires-v_acquired < interval '1 second'
      or v_expires-v_acquired > interval '5 minutes'
    then raise exception 'Invalid timestamps' using errcode='22023'; end if;
  elsif p_next->'acquired_at' <> 'null'::jsonb or p_next->'expires_at' <> 'null'::jsonb then
    raise exception 'Release must clear timestamps' using errcode='22023';
  end if;
  -- Serialize reads and writes in one transaction. Evaluate the clock after waiting.
  select * into strict v from public.wd_runtime_lease where singleton=true for update;
  v_now := clock_timestamp();
  if v.version <> p_expected_version then return jsonb_build_object('applied',false); end if;
  if v_owner is null then
    if v.owner is distinct from p_request_owner or v.principal is distinct from auth.uid()
      or v.expires_at is null or v.expires_at <= v_now
    then return jsonb_build_object('applied',false); end if;
  else
    if v.owner is not null and v.expires_at > v_now
      and (v.owner <> p_request_owner or v.principal is distinct from auth.uid())
    then return jsonb_build_object('applied',false); end if;
    if v_expires <= v_now or v_expires > v_now+interval '5 minutes'
      or v_acquired > v_now+interval '5 seconds'
      or v_acquired < v_now-interval '5 minutes'
    then raise exception 'Invalid lease clock or TTL' using errcode='22023'; end if;
  end if;
  update public.wd_runtime_lease set version=v.version+1, owner=v_owner,
    principal=case when v_owner is null then null else auth.uid() end,
    acquired_at=v_acquired, expires_at=v_expires where singleton=true;
  insert into public.wd_runtime_lease_audit(
    version,previous_version,previous_owner,owner,principal,request_owner,occurred_at,acquired_at,expires_at
  ) values(v.version+1,v.version,v.owner,v_owner,auth.uid(),p_request_owner,v_now,v_acquired,v_expires);
  return jsonb_build_object('applied',true,'lease',jsonb_build_object(
    'version',v.version+1,'owner',v_owner,'acquired_at',v_acquired,'expires_at',v_expires));
end;
$$;
revoke all on function public.wd_read_runtime_lease() from public,anon,authenticated,service_role;
revoke all on function public.wd_cas_runtime_lease(bigint,text,jsonb) from public,anon,authenticated,service_role;
grant execute on function public.wd_read_runtime_lease() to authenticated;
grant execute on function public.wd_cas_runtime_lease(bigint,text,jsonb) to authenticated;
commit;
