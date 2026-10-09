-- Apply only to the confirmed Work Digital Control Plane Supabase database.
-- No dispatcher is enabled by this migration.

create schema wd_runtime;
revoke all on schema wd_runtime from public, anon, authenticated;

create table wd_runtime.operators (
  user_id uuid primary key references auth.users(id) on delete cascade
);
create table wd_runtime.lease (
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
insert into wd_runtime.lease(singleton) values(true);
create table wd_runtime.lease_audit (
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
alter table wd_runtime.operators enable row level security;
alter table wd_runtime.lease enable row level security;
alter table wd_runtime.lease_audit enable row level security;
revoke all on all tables in schema wd_runtime from public, anon, authenticated;

create function wd_runtime.authorized() returns boolean
language sql stable security definer set search_path = '' as $$
  select auth.uid() is not null and exists (
    select 1 from wd_runtime.operators where user_id=auth.uid()
  );
$$;

create function wd_runtime.read_lease() returns jsonb
language plpgsql security definer set search_path = '' as $$
declare v wd_runtime.lease%rowtype;
begin
  if not wd_runtime.authorized() then
    raise exception 'Runtime operator required' using errcode='42501';
  end if;
  select * into strict v from wd_runtime.lease where singleton=true;
  return jsonb_build_object('version',v.version,'owner',v.owner,
    'acquired_at',v.acquired_at,'expires_at',v.expires_at);
end;
$$;

create function wd_runtime.cas_lease(
  p_expected_version bigint, p_request_owner text, p_next jsonb
) returns jsonb language plpgsql security definer set search_path = '' as $$
declare
  v wd_runtime.lease%rowtype;
  v_now timestamptz;
  v_owner text;
  v_acquired timestamptz;
  v_expires timestamptz;
begin
  if not wd_runtime.authorized() then
    raise exception 'Runtime operator required' using errcode='42501';
  end if;
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
  select * into strict v from wd_runtime.lease where singleton=true for update;
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
  update wd_runtime.lease set version=v.version+1, owner=v_owner,
    principal=case when v_owner is null then null else auth.uid() end,
    acquired_at=v_acquired, expires_at=v_expires where singleton=true;
  insert into wd_runtime.lease_audit(
    version,previous_version,previous_owner,owner,principal,request_owner,occurred_at,acquired_at,expires_at
  ) values(v.version+1,v.version,v.owner,v_owner,auth.uid(),p_request_owner,v_now,v_acquired,v_expires);
  return jsonb_build_object('applied',true,'lease',jsonb_build_object(
    'version',v.version+1,'owner',v_owner,'acquired_at',v_acquired,'expires_at',v_expires));
end;
$$;

-- The lease row remains locked until the delivery update commits. A heartbeat or takeover
-- cannot invalidate the fence between its check and the Work Packet write.
create function wd_runtime.persist_work_packet(
  p_request_owner text,
  p_fence_version bigint,
  p_packet_key text,
  p_result jsonb,
  p_next_action text default null
) returns jsonb language plpgsql security definer set search_path = '' as $$
declare
  v wd_runtime.lease%rowtype;
  v_now timestamptz;
  v_packet public.work_packets%rowtype;
begin
  if not wd_runtime.authorized() then
    raise exception 'Runtime operator required' using errcode='42501';
  end if;
  if p_request_owner is null or length(btrim(p_request_owner)) not between 1 and 200
    or p_fence_version is null or p_fence_version < 1
    or p_packet_key is null or length(btrim(p_packet_key)) < 1
    or p_result is null or jsonb_typeof(p_result) not in ('object','array','string')
  then raise exception 'Invalid fenced delivery' using errcode='22023'; end if;
  select * into strict v from wd_runtime.lease where singleton=true for update;
  v_now := clock_timestamp();
  if v.owner is distinct from p_request_owner
    or v.principal is distinct from auth.uid()
    or v.version <> p_fence_version
    or v.expires_at is null or v.expires_at <= v_now
  then raise exception 'Stale lease fence' using errcode='40001'; end if;
  update public.work_packets
  set result=p_result, next_action=p_next_action, status='REVIEW',
      completed_at=v_now, updated_at=v_now
  where packet_key=p_packet_key
    and result is null
    and status in ('SENT','READY','IN_PROGRESS','EXECUTING')
  returning * into v_packet;
  if not found then raise exception 'Work Packet is not writable' using errcode='55000'; end if;
  return to_jsonb(v_packet);
end;
$$;

-- Public wrappers are SECURITY INVOKER. Privileged code remains in a non-exposed schema.
create function public.wd_read_runtime_lease() returns jsonb
language sql security invoker set search_path = '' as $$
  select wd_runtime.read_lease();
$$;
create function public.wd_cas_runtime_lease(
  p_expected_version bigint, p_request_owner text, p_next jsonb
) returns jsonb language sql security invoker set search_path = '' as $$
  select wd_runtime.cas_lease(p_expected_version,p_request_owner,p_next);
$$;
create function public.wd_persist_work_packet_fenced(
  p_request_owner text, p_fence_version bigint, p_packet_key text,
  p_result jsonb, p_next_action text default null
) returns jsonb language sql security invoker set search_path = '' as $$
  select wd_runtime.persist_work_packet(
    p_request_owner,p_fence_version,p_packet_key,p_result,p_next_action
  );
$$;

revoke all on all functions in schema wd_runtime from public,anon,authenticated,service_role;
revoke all on function public.wd_read_runtime_lease() from public,anon,authenticated,service_role;
revoke all on function public.wd_cas_runtime_lease(bigint,text,jsonb) from public,anon,authenticated,service_role;
revoke all on function public.wd_persist_work_packet_fenced(text,bigint,text,jsonb,text) from public,anon,authenticated,service_role;
grant usage on schema wd_runtime to authenticated;
grant execute on function wd_runtime.authorized() to authenticated;
grant execute on function wd_runtime.read_lease() to authenticated;
grant execute on function wd_runtime.cas_lease(bigint,text,jsonb) to authenticated;
grant execute on function wd_runtime.persist_work_packet(text,bigint,text,jsonb,text) to authenticated;
grant execute on function public.wd_read_runtime_lease() to authenticated;
grant execute on function public.wd_cas_runtime_lease(bigint,text,jsonb) to authenticated;
grant execute on function public.wd_persist_work_packet_fenced(text,bigint,text,jsonb,text) to authenticated;

