# 📚 `docs/` — what a HUMAN reads, usually once

**Charter: setup guides and reference for you, not for the agents.**
If an agent reads it at runtime, it belongs in `system/`. That boundary was broken until 2026-09-06:
`qc-rubric.md`, `client-types.md`, `onboarding-questions.md` and `auto-posting-guide.md` all lived here
while agents read them on every run. They moved to `system/`.

| file | what it is |
|---|---|
| `mcp-setup.md` | MCP server configuration |
| `hermes-setup.md` | **read this first on a Hermes machine.** Profile, model pinning for subagents, MCP in `config.yaml`, where skills live, and what has no automatic enforcement here. |
| `skills-install.md` | installing the GitHub skill packages |
| `fal-ai-setup.md` | the funded image/video engine |
| `pricing-plans.md` | what we charge |
| `openmontage-setup.md` | **PARKED.** Kept in case OpenMontage is ever revisited. |
