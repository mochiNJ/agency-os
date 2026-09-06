# 📚 `docs/` — what a HUMAN reads, usually once

**Charter: setup guides and reference for you, not for the agents.**
If an agent reads it at runtime, it belongs in `system/`. That boundary was broken until 2026-09-06:
`qc-rubric.md`, `client-types.md`, `onboarding-questions.md` and `auto-posting-guide.md` all lived here
while agents read them on every run. They moved to `system/`.

| file | what it is |
|---|---|
| `mcp-setup.md` | MCP server configuration |
| `skills-install.md` | installing the GitHub skill packages |
| `fal-ai-setup.md` | the funded image/video engine |
| `postiz-second-pc-setup.md` | running Postiz on another machine |
| `agency-os-clean-copy-plan.md` | how the whole system is exported client-free to the second machine (the private `agency-os` repo), and how the two stay in sync |
| `pricing-plans.md` | what we charge |
| `openmontage-setup.md` | **PARKED.** Kept in case OpenMontage is ever revisited. |
| `canva-typography-app-plan.md` | **SHELVED 2026-09-06.** Sora does not exist in Canva, so no app can fix it. Kept because the assessment is still valid if the agency adopts Canva-available fonts. |
