const TEST_KEY = /(^|-)TEST(?:-|$)/i;

function recordKey(record, field) {
  return record?.[field] ?? record?.key ?? "";
}

function isProductionRecord(record, field) {
  return !TEST_KEY.test(String(recordKey(record, field)));
}

export function filterSnapshotRecords({
  operations = [],
  tasks = [],
  work_packets = [],
} = {}) {
  const filteredOperations = operations.filter((operation) =>
    isProductionRecord(operation, "operation_key")
  );
  const operationIds = new Set(filteredOperations.map(({ id }) => id));

  const filteredTasks = tasks.filter((task) =>
    isProductionRecord(task, "task_key") && operationIds.has(task.operation_id)
  );
  const taskIds = new Set(filteredTasks.map(({ id }) => id));

  const filteredWorkPackets = work_packets.filter((workPacket) =>
    isProductionRecord(workPacket, "packet_key") &&
    operationIds.has(workPacket.operation_id) &&
    taskIds.has(workPacket.task_id)
  );

  return {
    operations: filteredOperations,
    tasks: filteredTasks,
    work_packets: filteredWorkPackets,
  };
}
