import { test } from "node:test";
import assert from "node:assert/strict";
import { classifyFencedDeliveryError } from "./work-digital-mcp-v2/fenced-error.mjs";

test("classifies stale fences returned with their requested SQLSTATE", () => {
  assert.equal(classifyFencedDeliveryError({ code: "40001", message: "Stale lease fence" }), "stale-runtime-fence");
});

test("classifies stale fences wrapped by PostgREST as P0001", () => {
  assert.equal(classifyFencedDeliveryError({ code: "P0001", message: "Stale lease fence" }), "stale-runtime-fence");
});

test("preserves the other fenced delivery error categories", () => {
  assert.equal(classifyFencedDeliveryError({ code: "42501" }), "runtime-operator-required");
  assert.equal(classifyFencedDeliveryError({ code: "55000" }), "work-packet-not-writable");
  assert.equal(classifyFencedDeliveryError({ code: "22023" }), "invalid-fenced-delivery");
  assert.equal(classifyFencedDeliveryError({ code: "P0001", message: "Unexpected" }), "fenced-delivery-unavailable");
});
