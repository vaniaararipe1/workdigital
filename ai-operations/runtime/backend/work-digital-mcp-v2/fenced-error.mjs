const normalize = value => typeof value === "string" ? value.trim().toLowerCase() : "";

export function classifyFencedDeliveryError(error = {}) {
  const code = normalize(error.code);
  const message = normalize(error.message);

  if (code === "42501" || message.includes("runtime operator required")) {
    return "runtime-operator-required";
  }
  // PostgREST currently surfaces the PL/pgSQL exception as P0001 even when
  // the nested function requested SQLSTATE 40001. Keep the stable-code path,
  // but recognize the exact database message as a compatibility fallback.
  if (code === "40001" || message.includes("stale lease fence")) {
    return "stale-runtime-fence";
  }
  if (code === "55000" || message.includes("work packet is not writable")) {
    return "work-packet-not-writable";
  }
  if (["22023", "22007", "22008", "22p02"].includes(code)
    || message.includes("invalid fenced delivery")) {
    return "invalid-fenced-delivery";
  }
  return "fenced-delivery-unavailable";
}
