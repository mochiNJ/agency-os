# Running this agency on Hermes (Nous Research)

*Written 2026-09-06. Hermes is a different runtime from the one this system was built in, so three
things need wiring: where skills live, how subagents get their model, and the fact that nothing
fires automatically. Sources: the Hermes docs at hermes-agent.nousresearch.com (configuration,
profiles, skills, delegation, MCP).*

**Verify each step against the current Hermes docs before trusting it.** These commands and config
keys were read from the documentation, not run on this machine.

---

## 1. Install and make a profile for the agency

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
hermes profile create agency
```

A profile is a separate Hermes home at `~/.hermes/profiles/agency/`, with its own `config.yaml`,
`.env`, `SOUL.md`, memory, sessions and cron jobs. Keeping the agency in its own profile means its
memory and model settings never mix with anything else you run.

## 2. Point it at this repo and pin the models

A profile does NOT change the working directory on its own. In
`~/.hermes/profiles/agency/config.yaml`:

```yaml
model: <your main model>

terminal:
  cwd: "<absolute path to this repo>"

delegation:
  provider: "<provider>"
  model: "<the cheaper model producing agents should run on>"
```

`delegation` is what makes every `delegate_task` subagent run on the cheaper model while the
dispatcher stays sharp. The pin is global: there is no per-task model parameter. This is the Hermes
equivalent of our model policy (`system/model-policy.md`).

## 3. Secrets and MCP servers

Secrets go in `~/.hermes/profiles/agency/.env`, never in `config.yaml` and never in a chat.

MCP servers are declared in the same `config.yaml`:

```yaml
mcp_servers:
  postiz:
    command: npx
    args: ["-y", "postiz-mcp"]
    env:
      POSTIZ_URL: "http://localhost:5000"
      POSTIZ_API_KEY: ${POSTIZ_API_KEY}
```

`.mcp.example.json` in this repo lists the servers this system expects and what each is for; it is
the other runtime's format, so translate it into the YAML above rather than copying it. Hermes also
ships a reviewed catalog: `hermes mcp` for the picker, `hermes mcp catalog` to list, and
`hermes mcp install <name>`. If MCP support was not installed with Hermes, add it with
`cd ~/.hermes/hermes-agent && uv pip install -e ".[mcp]"`.

## 4. Skills

They are already here, committed at `.hermes/skills/`, which is Hermes's project-local skill folder.
Confirm they load:

```bash
bash install-skills.sh
```

It must report every folder loadable. A skill with its `SKILL.md` buried one level down is a skill
that does not exist, and nothing warns you.

## 5. Prove the machine works before doing any client work

```bash
python system/structure-check.py     # must exit 0
python system/sync.py                # must exit 0
bash install-skills.sh               # every skill loadable
node dashboard/server.js             # then open http://localhost:4321
```

Then scaffold a throwaway client, run one small job end to end through `delegate_task`, confirm the
output files exist where the CONTRACT says, and delete the throwaway.

```bash
python system/structure-check.py --new-client testco
```

## 6. What is genuinely different, and what to do about it

| Built for | Here | What to do |
|---|---|---|
| Project rules in `CLAUDE.md` | Hermes embeds `AGENTS.md` and `CLAUDE.md` into every agent and subagent prompt | nothing, it works |
| 16 agent files auto-registered as named subagents | `delegate_task` creates subagents at runtime, no file registry | pass the brief's path in `context`; see `AGENTS.md` |
| A hook injecting the enforcement checklist before every generation | no hook system documented | the checklist is in `AGENTS.md`, which is always embedded |
| A hook printing linked documents after every edit | same | run `python system/hooks/doc-links.py <file>` by hand after editing a governed file |
| Per-agent model in each agent file | delegation model is global | set `delegation.model` once |
| Skills at `.claude/skills/` | `.hermes/skills/` | already done in this repo |

Two Hermes features worth using once the basics run: **cron jobs** per profile (the Monday trend
sweep and the monthly report are both scheduled work), and **memory**, which is genuinely different
from how this system stores knowledge. Our rule is that nothing important lives only in a model's
memory: it goes in a file, because subagents spawn fresh. Keep that rule. Let Hermes's memory be a
convenience, never the source of truth.
