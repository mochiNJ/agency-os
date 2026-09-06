# AGENTS.md — how this agency runs on Hermes

**Hermes embeds this file, and `CLAUDE.md`, into the system prompt of the main agent AND of every
subagent it spawns. `CLAUDE.md` holds the rules. THIS file holds the two things that change because
the runtime is Hermes rather than Claude Code.**

---

## 1. The enforcement that used to be automatic is now YOUR job

In the other runtime a hook fired before every image, video and subagent spawn and injected the
checklist below. Hermes's documentation describes no hook system, so nothing injects it. **It is
reproduced here in full, because it is embedded in every agent's prompt.** Treat it as standing law.

1. **PALETTE, FONTS and NAME come from `clients/[client]/brand-profile.md`**, never from the brief,
   never from memory. If a brief and that file disagree, the FILE wins and you STOP and flag it.
2. **CONCEPT FIRST, then user sign-off, then build**, for every logo, identity, and
   first-of-its-kind visual. No generation before an approved concept.
3. **NEVER silently downgrade a tool.** If the required tool is unavailable or out of credit, STOP
   and say so before building. A quietly substituted lesser path is a violation, not a save.
4. **Save the full final prompt verbatim** to `clients/[client]/prompts/`.
5. **TOKEN DISCIPLINE.** Read only what the task needs. One efficient pass. Concise report.
   See `system/token-discipline.md` and `system/model-policy.md`.
6. **FILE SYSTEM LAW** (`system/file-system-law.md`): the FOLDER is the status, never the filename.
   MOVE, never copy. Wrong is deleted, different goes to `_alts/`. Only `_inbox/` and `_alts/`
   exist. **Never delete a video:** `*.mp4` is gitignored, so the working copy is the only copy.
   Finished work goes to `clients/[client]/library/posts/YYYY-MM-DD-slug/`.
7. **SKILLS:** load your MANDATORY skill from `system/skill-router.md` BEFORE the first draft.
8. **INSPIRATION:** read `inspiration-library/recipes/README.md` and the matching
   `by-business-type/` board before producing a visual.

**The linked-documents check is also manual now.** After editing a governed file, run:

```
python system/hooks/doc-links.py <the file you just edited>
```

It prints every document that must be updated in the same turn. The map is
`system/doc-dependencies.md`. Skipping it is how a stale file wins the next time an agent reads it.

---

## 2. The 16 agents are BRIEFS, not registered subagents

Hermes creates subagents at runtime with `delegate_task`; it does not read agent definitions from
files. So `.claude/agents/01..16` are not auto-loaded. They are still the source of truth for what
each agent does, and the pipeline runs like this:

1. **TICKET.** Create `system/jobs/YYYY-MM-DD-[client]-[task].md` from
   `templates/job-ticket-template.md`.
2. **INPUT CHECK.** Verify every input file that stage's CONTRACT requires actually exists. Missing
   input means STOP and report, never improvise around it.
3. **DELEGATE.** Call `delegate_task` once per stage, and put in `context`: the path of the agent
   brief (`.claude/agents/NN-name.md`) with an instruction to read it in full, the ticket path, the
   exact input paths, and the MANDATORY skill from `system/skill-router.md`. The brief IS the
   agent's system prompt; hand it over rather than paraphrasing it.
4. **VERIFY.** After each stage, confirm the CONTRACT's output files physically exist. No file
   means the stage did not happen, whatever the subagent reported.
5. **QC.** Agent 16 scores it and logs `system/qc-log.md`. No log entry means it is not deliverable.
6. **CLIENT SIGN-OFF** before publishing. A passing QC score is not client approval.

**One model for all subagents.** `delegate_task` has no per-task model parameter: the delegation
model is pinned globally in the profile's `config.yaml`. Our policy of running producing agents on a
cheaper model than the dispatcher therefore becomes a config setting, not a per-spawn decision. See
`docs/hermes-setup.md`.

**Run producing agents ONE at a time.** Hermes can batch a `tasks` array, and the temptation is to
fire all four producers at once. Do not: parallel heavy generations trip usage limits faster and
make failures hard to attribute.

---

## 3. Where the skills live

Every skill is committed to `.hermes/skills/` in this repo, which is Hermes's project-local skill
location, so a clone already has them. `bash install-skills.sh` verifies every folder is loadable
and exits non-zero if one is not. Run it once after cloning.
