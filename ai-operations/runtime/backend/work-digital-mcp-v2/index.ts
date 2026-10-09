import "jsr:@supabase/functions-js/edge-runtime.d.ts";



import {
  withOAuthProtectedResource,
  withSupabase,
} from "npm:@supabase/server@^1.6.0";



import {

  createMcpHandler,

  McpServer,

} from "npm:@modelcontextprotocol/server@^2.0.0";



import { z } from "npm:zod@^4.3.6";



function createHandler(supabase: any) {
  return createMcpHandler(() => {

  const server = new McpServer({

    name: "work-digital-control-plane",

    version: "2.7.0",

  });



  // ============================================================

  // HEALTH

  // ============================================================



  server.registerTool(

    "health",

    {

      title: "Work Digital Control Plane Health",

      description:

        "Verifica se o servidor MCP da Work Digital e a conexão com o banco estão online.",

      inputSchema: z.object({}),

      annotations: {

        readOnlyHint: true,

      },

    },

    async () => {

      const { error } = await supabase

        .from("operations")

        .select("id")

        .limit(1);



      if (error) {

        return {

          content: [{

            type: "text",

            text: JSON.stringify({

              ok: false,

              service: "work-digital-control-plane",

              protocol: "MCP",

              database: "error",

              error: error.message,

              version: "2.7.0",

            }),

          }],

          isError: true,

        };

      }



      return {

        content: [{

          type: "text",

          text: JSON.stringify({

            ok: true,

            service: "work-digital-control-plane",

            protocol: "MCP",

            status: "online",

            database: "connected",

            version: "2.7.0",

          }),

        }],

      };

    },

  );



  // ============================================================

  // AGENTS

  // ============================================================



  server.registerTool(

    "list_agents",

    {

      title: "List Work Digital Agents",

      description:

        "Lista os agentes registrados no Control Plane da Work Digital.",

      inputSchema: z.object({}),

      annotations: {

        readOnlyHint: true,

      },

    },

    async () => {

      const { data, error } = await supabase

        .from("agents")

        .select("*")

        .order("name", { ascending: true });



      if (error) {

        return {

          content: [{

            type: "text",

            text: JSON.stringify({

              ok: false,

              error: error.message,

            }),

          }],

          isError: true,

        };

      }



      return {

        content: [{

          type: "text",

          text: JSON.stringify({

            ok: true,

            agents: data,

          }),

        }],

      };

    },

  );



  server.registerTool(

    "create_agent",

    {

      title: "Create Work Digital Agent",

      description:

        "Registra um novo agente no Control Plane da Work Digital.",

      inputSchema: z.object({

        agent_key: z.string(),

        name: z.string(),

        role: z.string(),

        specialty: z.string().nullable().optional(),

        project_name: z.string().nullable().optional(),

        status: z.string().optional(),

        permissions: z

          .record(z.string(), z.unknown())

          .optional(),

        metadata: z

          .record(z.string(), z.unknown())

          .optional(),

      }),

    },

    async ({

      agent_key,

      name,

      role,

      specialty,

      project_name,

      status,

      permissions,

      metadata,

    }) => {

      const { data, error } = await supabase

        .from("agents")

        .insert({

          agent_key,

          name,

          role,

          specialty: specialty ?? null,

          project_name: project_name ?? null,

          status: status ?? "ACTIVE",

          permissions: permissions ?? {},

          metadata: metadata ?? {},

        })

        .select()

        .single();



      if (error) {

        return {

          content: [{

            type: "text",

            text: JSON.stringify({

              ok: false,

              error: error.message,

            }),

          }],

          isError: true,

        };

      }



      return {

        content: [{

          type: "text",

          text: JSON.stringify({

            ok: true,

            agent: data,

          }),

        }],

      };

    },

  );



  server.registerTool(

    "update_agent",

    {

      title: "Update Work Digital Agent",

      description:

        "Atualiza campos de um agente existente no Control Plane da Work Digital, identificado por agent_key.",

      inputSchema: z.object({

        agent_key: z.string(),

        name: z.string().optional(),

        role: z.string().optional(),

        specialty: z.string().nullable().optional(),

        project_name: z.string().nullable().optional(),

        status: z.string().optional(),

        permissions: z

          .record(z.string(), z.unknown())

          .optional(),

        metadata: z

          .record(z.string(), z.unknown())

          .optional(),

      }),

    },

    async ({

      agent_key,

      name,

      role,

      specialty,

      project_name,

      status,

      permissions,

      metadata,

    }) => {

      const updates: Record<string, unknown> = {};



      if (name !== undefined) updates.name = name;

      if (role !== undefined) updates.role = role;

      if (specialty !== undefined) updates.specialty = specialty;

      if (project_name !== undefined) updates.project_name = project_name;

      if (status !== undefined) updates.status = status;

      if (permissions !== undefined) updates.permissions = permissions;

      if (metadata !== undefined) updates.metadata = metadata;



      if (Object.keys(updates).length === 0) {

        return {

          content: [{

            type: "text",

            text: JSON.stringify({

              ok: false,

              error: "Nenhum campo informado para atualização.",

            }),

          }],

          isError: true,

        };

      }



      const { data, error } = await supabase

        .from("agents")

        .update(updates)

        .eq("agent_key", agent_key)

        .select()

        .maybeSingle();



      if (error) {

        return {

          content: [{

            type: "text",

            text: JSON.stringify({

              ok: false,

              error: error.message,

            }),

          }],

          isError: true,

        };

      }



      if (!data) {

        return {

          content: [{

            type: "text",

            text: JSON.stringify({

              ok: false,

              error: `Agente não encontrado: ${agent_key}`,

            }),

          }],

          isError: true,

        };

      }



      return {

        content: [{

          type: "text",

          text: JSON.stringify({

            ok: true,

            agent: data,

          }),

        }],

      };

    },

  );



  // ============================================================

  // OPERATIONS

  // ============================================================



  server.registerTool(

    "list_operations",

    {

      title: "List Work Digital Operations",

      description:

        "Lista as operações registradas no Control Plane da Work Digital.",

      inputSchema: z.object({}),

      annotations: {

        readOnlyHint: true,

      },

    },

    async () => {

      const { data, error } = await supabase

        .from("operations")

        .select("*")

        .order("created_at", { ascending: false });



      if (error) {

        return {

          content: [{

            type: "text",

            text: JSON.stringify({

              ok: false,

              error: error.message,

            }),

          }],

          isError: true,

        };

      }



      return {

        content: [{

          type: "text",

          text: JSON.stringify({

            ok: true,

            operations: data,

          }),

        }],

      };

    },

  );



  server.registerTool(

    "create_operation",

    {

      title: "Create Work Digital Operation",

      description:

        "Cria uma nova operação no Control Plane da Work Digital.",

      inputSchema: z.object({

        operation_key: z.string(),

        name: z.string(),

        status: z.string().optional(),

        initiated_by: z.string().nullable().optional(),

        coordinator_agent: z.string().nullable().optional(),

        objective: z.string().nullable().optional(),

      }),

    },

    async ({

      operation_key,

      name,

      status,

      initiated_by,

      coordinator_agent,

      objective,

    }) => {

      const { data, error } = await supabase

        .from("operations")

        .insert({

          operation_key,

          name,

          status: status ?? "BACKLOG",

          initiated_by: initiated_by ?? null,

          coordinator_agent: coordinator_agent ?? null,

          objective: objective ?? null,

        })

        .select()

        .single();



      if (error) {

        return {

          content: [{

            type: "text",

            text: JSON.stringify({

              ok: false,

              error: error.message,

            }),

          }],

          isError: true,

        };

      }



      return {

        content: [{

          type: "text",

          text: JSON.stringify({

            ok: true,

            operation: data,

          }),

        }],

      };

    },

  );



  // ============================================================

  // TASKS

  // ============================================================



  server.registerTool(

    "list_tasks",

    {

      title: "List Work Digital Tasks",

      description:

        "Lista tarefas do Control Plane. Pode filtrar por operation_id.",

      inputSchema: z.object({

        operation_id: z.string().optional(),

      }),

      annotations: {

        readOnlyHint: true,

      },

    },

    async ({ operation_id }) => {

      let query = supabase

        .from("tasks")

        .select("*")

        .order("priority", { ascending: false });



      if (operation_id) {

        query = query.eq("operation_id", operation_id);

      }



      const { data, error } = await query;



      if (error) {

        return {

          content: [{

            type: "text",

            text: JSON.stringify({

              ok: false,

              error: error.message,

            }),

          }],

          isError: true,

        };

      }



      return {

        content: [{

          type: "text",

          text: JSON.stringify({

            ok: true,

            tasks: data,

          }),

        }],

      };

    },

  );



  server.registerTool(

    "create_task",

    {

      title: "Create Work Digital Task",

      description:

        "Cria uma nova tarefa operacional no Control Plane da Work Digital.",

      inputSchema: z.object({

        operation_id: z.string().nullable().optional(),

        parent_task_id: z.string().nullable().optional(),

        task_key: z.string(),

        title: z.string(),

        objective: z.string().nullable().optional(),

        owner_agent: z.string().nullable().optional(),

        status: z.string().optional(),

        priority: z.number().optional(),

        dependencies: z.array(z.unknown()).optional(),

        constraints: z

          .record(z.string(), z.unknown())

          .optional(),

        next_action: z.string().nullable().optional(),

      }),

    },

    async ({

      operation_id,

      parent_task_id,

      task_key,

      title,

      objective,

      owner_agent,

      status,

      priority,

      dependencies,

      constraints,

      next_action,

    }) => {

      const { data, error } = await supabase

        .from("tasks")

        .insert({

          operation_id: operation_id ?? null,

          parent_task_id: parent_task_id ?? null,

          task_key,

          title,

          objective: objective ?? null,

          owner_agent: owner_agent ?? null,

          status: status ?? "BACKLOG",

          priority: priority ?? 50,

          dependencies: dependencies ?? [],

          constraints: constraints ?? {},

          next_action: next_action ?? null,

        })

        .select()

        .single();



      if (error) {

        return {

          content: [{

            type: "text",

            text: JSON.stringify({

              ok: false,

              error: error.message,

            }),

          }],

          isError: true,

        };

      }



      return {

        content: [{

          type: "text",

          text: JSON.stringify({

            ok: true,

            task: data,

          }),

        }],

      };

    },

  );



  // ============================================================

  // WORK PACKETS

  // ============================================================



  server.registerTool(

    "list_work_packets",

    {

      title: "List Work Digital Work Packets",

      description:

        "Lista Work Packets. Pode filtrar por operation_id e destination_agent.",

      inputSchema: z.object({

        operation_id: z.string().optional(),

        destination_agent: z.string().optional(),

      }),

      annotations: {

        readOnlyHint: true,

      },

    },

    async ({

      operation_id,

      destination_agent,

    }) => {

      let query = supabase

        .from("work_packets")

        .select("*")

        .order("created_at", { ascending: false });



      if (operation_id) {

        query = query.eq("operation_id", operation_id);

      }



      if (destination_agent) {

        query = query.eq(

          "destination_agent",

          destination_agent,

        );

      }



      const { data, error } = await query;



      if (error) {

        return {

          content: [{

            type: "text",

            text: JSON.stringify({

              ok: false,

              error: error.message,

            }),

          }],

          isError: true,

        };

      }



      return {

        content: [{

          type: "text",

          text: JSON.stringify({

            ok: true,

            work_packets: data,

          }),

        }],

      };

    },

  );



  server.registerTool(

    "create_work_packet",

    {

      title: "Create Work Digital Work Packet",

      description:

        "Cria um Work Packet para transferência estruturada de trabalho entre agentes.",

      inputSchema: z.object({

        packet_key: z.string(),

        operation_id: z.string().nullable().optional(),

        task_id: z.string().nullable().optional(),

        source_agent: z.string().nullable().optional(),

        destination_agent: z.string().nullable().optional(),

        objective: z.string().nullable().optional(),

        context: z.string().nullable().optional(),

        evidence: z.array(z.unknown()).optional(),

        insights: z.array(z.unknown()).optional(),

        instructions: z.array(z.unknown()).optional(),

        constraints: z.array(z.unknown()).optional(),

        reference_links: z.array(z.unknown()).optional(),

        expected_output: z.string().nullable().optional(),

        status: z.string().optional(),

      }),

    },

    async ({

      packet_key,

      operation_id,

      task_id,

      source_agent,

      destination_agent,

      objective,

      context,

      evidence,

      insights,

      instructions,

      constraints,

      reference_links,

      expected_output,

      status,

    }) => {

      const { data, error } = await supabase

        .from("work_packets")

        .insert({

          packet_key,

          operation_id: operation_id ?? null,

          task_id: task_id ?? null,

          source_agent: source_agent ?? null,

          destination_agent: destination_agent ?? null,

          objective: objective ?? null,

          context: context ?? null,

          evidence: evidence ?? [],

          insights: insights ?? [],

          instructions: instructions ?? [],

          constraints: constraints ?? [],

          reference_links: reference_links ?? [],

          expected_output: expected_output ?? null,

          status: status ?? "CREATED",

        })

        .select()

        .single();



      if (error) {

        return {

          content: [{

            type: "text",

            text: JSON.stringify({

              ok: false,

              error: error.message,

            }),

          }],

          isError: true,

        };

      }



      return {

        content: [{

          type: "text",

          text: JSON.stringify({

            ok: true,

            work_packet: data,

          }),

        }],

      };

    },

  );




  // ============================================================
  // UPDATE OPERATIONS / TASKS / WORK PACKETS
  // ============================================================

  server.registerTool(
    "update_operation",
    {
      title: "Update Work Digital Operation",
      description: "Atualiza uma operação existente, identificada por operation_key.",
      inputSchema: z.object({
        operation_key: z.string(),
        name: z.string().optional(),
        status: z.string().optional(),
        initiated_by: z.string().nullable().optional(),
        coordinator_agent: z.string().nullable().optional(),
        objective: z.string().nullable().optional(),
      }),
    },
    async ({ operation_key, name, status, initiated_by, coordinator_agent, objective }) => {
      const updates: Record<string, unknown> = {};
      if (name !== undefined) updates.name = name;
      if (status !== undefined) updates.status = status;
      if (initiated_by !== undefined) updates.initiated_by = initiated_by;
      if (coordinator_agent !== undefined) updates.coordinator_agent = coordinator_agent;
      if (objective !== undefined) updates.objective = objective;

      if (Object.keys(updates).length === 0) {
        return { content: [{ type: "text", text: JSON.stringify({ ok: false, error: "Nenhum campo informado para atualização." }) }], isError: true };
      }

      const { data, error } = await supabase.from("operations").update(updates).eq("operation_key", operation_key).select().maybeSingle();
      if (error) return { content: [{ type: "text", text: JSON.stringify({ ok: false, error: error.message }) }], isError: true };
      if (!data) return { content: [{ type: "text", text: JSON.stringify({ ok: false, error: `Operação não encontrada: ${operation_key}` }) }], isError: true };
      return { content: [{ type: "text", text: JSON.stringify({ ok: true, operation: data }) }] };
    },
  );

  server.registerTool(
    "update_task",
    {
      title: "Update Work Digital Task",
      description: "Atualiza uma tarefa existente, identificada por task_key.",
      inputSchema: z.object({
        task_key: z.string(),
        operation_id: z.string().nullable().optional(),
        parent_task_id: z.string().nullable().optional(),
        title: z.string().optional(),
        objective: z.string().nullable().optional(),
        owner_agent: z.string().nullable().optional(),
        status: z.string().optional(),
        priority: z.number().optional(),
        dependencies: z.array(z.unknown()).optional(),
        constraints: z.record(z.string(), z.unknown()).optional(),
        next_action: z.string().nullable().optional(),
      }),
    },
    async ({ task_key, operation_id, parent_task_id, title, objective, owner_agent, status, priority, dependencies, constraints, next_action }) => {
      const updates: Record<string, unknown> = {};
      if (operation_id !== undefined) updates.operation_id = operation_id;
      if (parent_task_id !== undefined) updates.parent_task_id = parent_task_id;
      if (title !== undefined) updates.title = title;
      if (objective !== undefined) updates.objective = objective;
      if (owner_agent !== undefined) updates.owner_agent = owner_agent;
      if (status !== undefined) updates.status = status;
      if (priority !== undefined) updates.priority = priority;
      if (dependencies !== undefined) updates.dependencies = dependencies;
      if (constraints !== undefined) updates.constraints = constraints;
      if (next_action !== undefined) updates.next_action = next_action;

      if (Object.keys(updates).length === 0) {
        return { content: [{ type: "text", text: JSON.stringify({ ok: false, error: "Nenhum campo informado para atualização." }) }], isError: true };
      }

      const { data, error } = await supabase.from("tasks").update(updates).eq("task_key", task_key).select().maybeSingle();
      if (error) return { content: [{ type: "text", text: JSON.stringify({ ok: false, error: error.message }) }], isError: true };
      if (!data) return { content: [{ type: "text", text: JSON.stringify({ ok: false, error: `Tarefa não encontrada: ${task_key}` }) }], isError: true };
      return { content: [{ type: "text", text: JSON.stringify({ ok: true, task: data }) }] };
    },
  );

  server.registerTool(
    "read_runtime_lease",
    {
      title: "Read Work Digital Runtime Lease",
      description: "Lê a reserva durável do runtime. Não ativa o dispatcher.",
      inputSchema: z.object({}),
      annotations: { readOnlyHint: true },
    },
    async () => {
      const { data, error } = await supabase.rpc("wd_read_runtime_lease");
      if (error) {
        const denied = error.code === "42501";
        return {
          content: [{ type: "text", text: JSON.stringify({
            ok: false,
            error: denied ? "runtime-operator-required" : "runtime-lease-unavailable",
          }) }],
          isError: true,
        };
      }
      return {
        content: [{ type: "text", text: JSON.stringify({ ok: true, lease: data }) }],
      };
    },
  );

  server.registerTool(
    "cas_runtime_lease",
    {
      title: "Compare and Swap Work Digital Runtime Lease",
      description: "Adquire, renova ou libera a reserva durável usando versão esperada e identidade explícita.",
      inputSchema: z.object({
        expected_version: z.number().int().min(0),
        request_owner: z.string().min(1).max(200),
        next: z.object({
          version: z.number().int().min(1),
          owner: z.string().min(1).max(200).nullable(),
          acquired_at: z.string().nullable(),
          expires_at: z.string().nullable(),
        }),
      }),
    },
    async ({ expected_version, request_owner, next }) => {
      const { data, error } = await supabase.rpc("wd_cas_runtime_lease", {
        p_expected_version: expected_version,
        p_request_owner: request_owner,
        p_next: next,
      });
      if (error) {
        const invalid = ["22023", "22007", "22008", "22P02"].includes(error.code);
        const denied = error.code === "42501";
        return {
          content: [{ type: "text", text: JSON.stringify({
            ok: false,
            error: denied
              ? "runtime-operator-required"
              : invalid
              ? "invalid-runtime-lease"
              : "runtime-lease-unavailable",
          }) }],
          isError: true,
        };
      }
      if (data?.applied !== true) {
        return {
          content: [{ type: "text", text: JSON.stringify({
            ok: false,
            error: "runtime-lease-conflict",
          }) }],
          isError: true,
        };
      }
      return {
        content: [{ type: "text", text: JSON.stringify({
          ok: true,
          lease: data.lease,
        }) }],
      };
    },
  );

  server.registerTool(
    "persist_work_packet_fenced",
    {
      title: "Persist Fenced Work Packet Delivery",
      description: "Persiste uma entrega interna somente quando owner, usuário, versão e validade da reserva continuam atuais.",
      inputSchema: z.object({
        request_owner: z.string().min(1).max(200),
        fence_version: z.number().int().min(1),
        packet_key: z.string().min(1),
        result: z.unknown(),
        next_action: z.string().nullable().optional(),
      }),
    },
    async ({ request_owner, fence_version, packet_key, result, next_action }) => {
      const { data, error } = await supabase.rpc("wd_persist_work_packet_fenced", {
        p_request_owner: request_owner,
        p_fence_version: fence_version,
        p_packet_key: packet_key,
        p_result: result,
        p_next_action: next_action ?? null,
      });
      if (error) {
        const denied = error.code === "42501";
        const stale = error.code === "40001";
        const notWritable = error.code === "55000";
        const invalid = ["22023", "22007", "22008", "22P02"].includes(error.code);
        return {
          content: [{ type: "text", text: JSON.stringify({
            ok: false,
            error: denied
              ? "runtime-operator-required"
              : stale
              ? "stale-runtime-fence"
              : notWritable
              ? "work-packet-not-writable"
              : invalid
              ? "invalid-fenced-delivery"
              : "fenced-delivery-unavailable",
          }) }],
          isError: true,
        };
      }
      return {
        content: [{ type: "text", text: JSON.stringify({
          ok: true,
          work_packet: data,
        }) }],
      };
    },
  );

  server.registerTool(
    "update_work_packet",
    {
      title: "Update Work Digital Work Packet",
      description: "Atualiza metadados de um Work Packet existente. Entregas de runtime devem usar persist_work_packet_fenced.",
      inputSchema: z.object({
        packet_key: z.string(),
        operation_id: z.string().nullable().optional(),
        task_id: z.string().nullable().optional(),
        source_agent: z.string().nullable().optional(),
        destination_agent: z.string().nullable().optional(),
        objective: z.string().nullable().optional(),
        context: z.string().nullable().optional(),
        evidence: z.array(z.unknown()).optional(),
        insights: z.array(z.unknown()).optional(),
        instructions: z.array(z.unknown()).optional(),
        constraints: z.array(z.unknown()).optional(),
        reference_links: z.array(z.unknown()).optional(),
        expected_output: z.string().nullable().optional(),
        result: z.string().nullable().optional(),
        next_action: z.string().nullable().optional(),
        sent_at: z.string().nullable().optional(),
        received_at: z.string().nullable().optional(),
        completed_at: z.string().nullable().optional(),
        status: z.string().optional(),
      }),
    },
    async ({ packet_key, operation_id, task_id, source_agent, destination_agent, objective, context, evidence, insights, instructions, constraints, reference_links, expected_output, result, next_action, sent_at, received_at, completed_at, status }) => {
      const updates: Record<string, unknown> = {};
      if (operation_id !== undefined) updates.operation_id = operation_id;
      if (task_id !== undefined) updates.task_id = task_id;
      if (source_agent !== undefined) updates.source_agent = source_agent;
      if (destination_agent !== undefined) updates.destination_agent = destination_agent;
      if (objective !== undefined) updates.objective = objective;
      if (context !== undefined) updates.context = context;
      if (evidence !== undefined) updates.evidence = evidence;
      if (insights !== undefined) updates.insights = insights;
      if (instructions !== undefined) updates.instructions = instructions;
      if (constraints !== undefined) updates.constraints = constraints;
      if (reference_links !== undefined) updates.reference_links = reference_links;
      if (expected_output !== undefined) updates.expected_output = expected_output;
      if (result !== undefined) updates.result = result;
      if (next_action !== undefined) updates.next_action = next_action;
      if (sent_at !== undefined) updates.sent_at = sent_at;
      if (received_at !== undefined) updates.received_at = received_at;
      if (completed_at !== undefined) updates.completed_at = completed_at;
      if (status !== undefined) updates.status = status;

      if (Object.keys(updates).length === 0) {
        return { content: [{ type: "text", text: JSON.stringify({ ok: false, error: "Nenhum campo informado para atualização." }) }], isError: true };
      }

      const { data, error } = await supabase.from("work_packets").update(updates).eq("packet_key", packet_key).select().maybeSingle();
      if (error) return { content: [{ type: "text", text: JSON.stringify({ ok: false, error: error.message }) }], isError: true };
      if (!data) return { content: [{ type: "text", text: JSON.stringify({ ok: false, error: `Work Packet não encontrado: ${packet_key}` }) }], isError: true };
      return { content: [{ type: "text", text: JSON.stringify({ ok: true, work_packet: data }) }] };
    },
  );


  // ============================================================
  // EVIDENCE
  // ============================================================

  server.registerTool(
    "list_evidence",
    {
      title: "List Work Digital Evidence",
      description: "Lista evidências registradas no Control Plane. Pode filtrar por operation_id e task_id.",
      inputSchema: z.object({
        operation_id: z.string().optional(),
        task_id: z.string().optional(),
      }),
      annotations: {
        readOnlyHint: true,
      },
    },
    async ({ operation_id, task_id }) => {
      let query = supabase
        .from("evidence")
        .select("*")
        .order("created_at", { ascending: false });

      if (operation_id) {
        query = query.eq("related_operation_id", operation_id);
      }

      if (task_id) {
        query = query.eq("related_task_id", task_id);
      }

      const { data, error } = await query;

      if (error) {
        return {
          content: [{
            type: "text",
            text: JSON.stringify({ ok: false, error: error.message }),
          }],
          isError: true,
        };
      }

      return {
        content: [{
          type: "text",
          text: JSON.stringify({ ok: true, evidence: data }),
        }],
      };
    },
  );

  server.registerTool(
    "create_evidence",
    {
      title: "Create Work Digital Evidence",
      description: "Registra uma nova evidência no Control Plane da Work Digital.",
      inputSchema: z.object({
        evidence_key: z.string(),
        content: z.string(),
        source: z.string().nullable().optional(),
        source_type: z.string().nullable().optional(),
        source_url: z.string().nullable().optional(),
        observed_at: z.string().nullable().optional(),
        relevance: z.string().nullable().optional(),
        reliability: z.string().nullable().optional(),
        status: z.string().optional(),
        related_operation_id: z.string().nullable().optional(),
        related_task_id: z.string().nullable().optional(),
        metadata: z.record(z.string(), z.unknown()).optional(),
      }),
    },
    async ({
      evidence_key,
      content,
      source,
      source_type,
      source_url,
      observed_at,
      relevance,
      reliability,
      status,
      related_operation_id,
      related_task_id,
      metadata,
    }) => {
      const { data, error } = await supabase
        .from("evidence")
        .insert({
          evidence_key,
          source: source ?? null,
          source_type: source_type ?? null,
          source_url: source_url ?? null,
          observed_at: observed_at ?? null,
          content,
          relevance: relevance ?? null,
          reliability: reliability ?? null,
          status: status ?? "ACTIVE",
          related_operation_id: related_operation_id ?? null,
          related_task_id: related_task_id ?? null,
          metadata: metadata ?? {},
        })
        .select()
        .single();

      if (error) {
        return {
          content: [{
            type: "text",
            text: JSON.stringify({ ok: false, error: error.message }),
          }],
          isError: true,
        };
      }

      return {
        content: [{
          type: "text",
          text: JSON.stringify({ ok: true, evidence: data }),
        }],
      };
    },
  );

  // ============================================================
  // INSIGHTS
  // ============================================================

  server.registerTool(
    "list_insights",
    {
      title: "List Work Digital Insights",
      description: "Lista insights registrados no Control Plane. Pode filtrar por operation_id.",
      inputSchema: z.object({
        operation_id: z.string().optional(),
      }),
      annotations: {
        readOnlyHint: true,
      },
    },
    async ({ operation_id }) => {
      let query = supabase
        .from("insights")
        .select("*")
        .order("created_at", { ascending: false });

      if (operation_id) {
        query = query.eq("operation_id", operation_id);
      }

      const { data, error } = await query;

      if (error) {
        return {
          content: [{
            type: "text",
            text: JSON.stringify({ ok: false, error: error.message }),
          }],
          isError: true,
        };
      }

      return {
        content: [{
          type: "text",
          text: JSON.stringify({ ok: true, insights: data }),
        }],
      };
    },
  );

  server.registerTool(
    "create_insight",
    {
      title: "Create Work Digital Insight",
      description: "Registra um novo insight no Control Plane da Work Digital.",
      inputSchema: z.object({
        insight_key: z.string(),
        description: z.string(),
        operation_id: z.string().nullable().optional(),
        origin_agent: z.string().nullable().optional(),
        supporting_evidence: z.array(z.unknown()).optional(),
        implications: z.string().nullable().optional(),
        confidence: z.unknown().nullable().optional(),
        status: z.string().optional(),
        related_tasks: z.array(z.unknown()).optional(),
      }),
    },
    async ({
      insight_key,
      description,
      operation_id,
      origin_agent,
      supporting_evidence,
      implications,
      confidence,
      status,
      related_tasks,
    }) => {
      const { data, error } = await supabase
        .from("insights")
        .insert({
          insight_key,
          operation_id: operation_id ?? null,
          origin_agent: origin_agent ?? null,
          description,
          supporting_evidence: supporting_evidence ?? [],
          implications: implications ?? null,
          confidence: confidence ?? null,
          status: status ?? "ACTIVE",
          related_tasks: related_tasks ?? [],
        })
        .select()
        .single();

      if (error) {
        return {
          content: [{
            type: "text",
            text: JSON.stringify({ ok: false, error: error.message }),
          }],
          isError: true,
        };
      }

      return {
        content: [{
          type: "text",
          text: JSON.stringify({ ok: true, insight: data }),
        }],
      };
    },
  );

  // ============================================================
  // DECISIONS
  // ============================================================

  server.registerTool(
    "list_decisions",
    {
      title: "List Work Digital Decisions",
      description: "Lista decisões registradas no Control Plane. Pode filtrar por operation_id.",
      inputSchema: z.object({
        operation_id: z.string().optional(),
      }),
      annotations: {
        readOnlyHint: true,
      },
    },
    async ({ operation_id }) => {
      let query = supabase
        .from("decisions")
        .select("*")
        .order("created_at", { ascending: false });

      if (operation_id) {
        query = query.eq("operation_id", operation_id);
      }

      const { data, error } = await query;

      if (error) {
        return {
          content: [{
            type: "text",
            text: JSON.stringify({ ok: false, error: error.message }),
          }],
          isError: true,
        };
      }

      return {
        content: [{
          type: "text",
          text: JSON.stringify({ ok: true, decisions: data }),
        }],
      };
    },
  );

  server.registerTool(
    "create_decision",
    {
      title: "Create Work Digital Decision",
      description: "Registra uma nova decisão no Control Plane da Work Digital.",
      inputSchema: z.object({
        decision_key: z.string(),
        decision: z.string(),
        operation_id: z.string().nullable().optional(),
        context: z.string().nullable().optional(),
        evidence: z.array(z.unknown()).optional(),
        alternatives: z.array(z.unknown()).optional(),
        chosen_option: z.string().nullable().optional(),
        decision_maker: z.string().nullable().optional(),
        status: z.string().optional(),
        impact: z.string().nullable().optional(),
      }),
    },
    async ({
      decision_key,
      decision,
      operation_id,
      context,
      evidence,
      alternatives,
      chosen_option,
      decision_maker,
      status,
      impact,
    }) => {
      const { data, error } = await supabase
        .from("decisions")
        .insert({
          decision_key,
          operation_id: operation_id ?? null,
          decision,
          context: context ?? null,
          evidence: evidence ?? [],
          alternatives: alternatives ?? [],
          chosen_option: chosen_option ?? null,
          decision_maker: decision_maker ?? null,
          status: status ?? "PROPOSED",
          impact: impact ?? null,
        })
        .select()
        .single();

      if (error) {
        return {
          content: [{
            type: "text",
            text: JSON.stringify({ ok: false, error: error.message }),
          }],
          isError: true,
        };
      }

      return {
        content: [{
          type: "text",
          text: JSON.stringify({ ok: true, decision: data }),
        }],
      };
    },
  );

  return server;

});
}

Deno.serve(
  withOAuthProtectedResource(
    withSupabase(
      { auth: "user" },
      async (req, { supabase }) => {
        const handler = createHandler(supabase);
        return handler.fetch(req);
      },
    ),
  ),
);

