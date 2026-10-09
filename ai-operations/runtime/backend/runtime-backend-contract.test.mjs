import { test } from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const migrationUrl = new URL("./001_runtime_lease.sql", import.meta.url);
const mcpUrl = new URL("./work-digital-mcp-v2/index.ts", import.meta.url);

test("lease privileges stay behind authenticated private-schema functions", async () => {
  const sql = await readFile(migrationUrl, "utf8");
  assert.match(sql, /create schema wd_runtime/i);
  assert.match(sql, /security definer set search_path = ''/i);
  assert.match(sql, /revoke all on all tables in schema wd_runtime from public, anon, authenticated/i);
  assert.match(sql, /revoke all on all functions in schema wd_runtime from public,anon,authenticated,service_role/i);
  assert.match(sql, /grant execute on function public\.wd_read_runtime_lease\(\) to authenticated/i);
  assert.doesNotMatch(sql, /grant\s+(?:select|insert|update|delete|all).*wd_runtime\.(?:lease|operators|lease_audit)/i);
});

test("fenced delivery locks the lease before writing a work packet", async () => {
  const sql = await readFile(migrationUrl, "utf8");
  const fn = sql.slice(sql.indexOf("create function wd_runtime.persist_work_packet"));
  const lock = fn.indexOf("from wd_runtime.lease where singleton=true for update");
  const fence = fn.indexOf("v.version <> p_fence_version");
  const write = fn.indexOf("update public.work_packets");
  assert.ok(lock >= 0 && fence > lock && write > fence);
  assert.match(fn, /v\.principal is distinct from auth\.uid\(\)/);
  assert.match(fn, /v\.expires_at is null or v\.expires_at <= v_now/);
  assert.match(fn, /and result is null/);
});

test("current MCP source preserves OAuth and exposes the three runtime tools", async () => {
  const source = await readFile(mcpUrl, "utf8");
  assert.match(source, /withOAuthProtectedResource\(/);
  assert.match(source, /withSupabase\(\s*\{ auth: "user" \}/);
  assert.match(source, /version: "2\.7\.0"/);
  for (const tool of [
    "read_runtime_lease",
    "cas_runtime_lease",
    "persist_work_packet_fenced",
  ]) {
    assert.match(source, new RegExp(`server\\.registerTool\\(\\s*"${tool}"`));
  }
  assert.match(source, /supabase\.rpc\("wd_persist_work_packet_fenced"/);
});
