import { test } from "node:test";
import assert from "node:assert/strict";

import { filterSnapshotRecords } from "./work-digital-mcp-v2/snapshot-filter.mjs";

test("snapshot filter removes test and orphan records without mutating the source", () => {
  const source = {
    operations: [
      { id: "op-live", operation_key: "OP-001" },
      { id: "op-test", operation_key: "OP-TEST-001" },
    ],
    tasks: [
      { id: "task-live", operation_id: "op-live", task_key: "TASK-001" },
      { id: "task-test", operation_id: "op-live", task_key: "TASK-TEST-001" },
      { id: "task-child-test", operation_id: "op-test", task_key: "TASK-002" },
      { id: "task-orphan", operation_id: "missing", task_key: "TASK-003" },
    ],
    work_packets: [
      { id: "wp-live", operation_id: "op-live", task_id: "task-live", packet_key: "WP-001" },
      { id: "wp-test", operation_id: "op-live", task_id: "task-live", packet_key: "WP-TEST-001" },
      { id: "wp-orphan-task", operation_id: "op-live", task_id: "missing", packet_key: "WP-002" },
      { id: "wp-orphan-op", operation_id: "missing", task_id: "task-live", packet_key: "WP-003" },
    ],
  };

  const result = filterSnapshotRecords(source);

  assert.deepEqual(result.operations.map(({ id }) => id), ["op-live"]);
  assert.deepEqual(result.tasks.map(({ id }) => id), ["task-live"]);
  assert.deepEqual(result.work_packets.map(({ id }) => id), ["wp-live"]);
  assert.equal(source.operations.length, 2);
  assert.equal(source.tasks.length, 4);
  assert.equal(source.work_packets.length, 4);
});

test("snapshot filter accepts empty input", () => {
  assert.deepEqual(filterSnapshotRecords(), {
    operations: [],
    tasks: [],
    work_packets: [],
  });
});
