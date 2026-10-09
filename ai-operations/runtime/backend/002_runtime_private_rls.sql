-- Explicit deny policies document the private-table boundary and keep direct
-- access closed. Authorized calls go through SECURITY DEFINER functions.
create policy runtime_operators_private
on wd_runtime.operators
for all
to public
using (false)
with check (false);

create policy runtime_lease_private
on wd_runtime.lease
for all
to public
using (false)
with check (false);

create policy runtime_lease_audit_private
on wd_runtime.lease_audit
for all
to public
using (false)
with check (false);
