# Model Policy — which Claude model runs what, and when to ask the user to switch
**Created 2026-08-18** at the user's request, after repeatedly hitting the account session limit (running everything on Opus). This is the standing rule for model choice across the agency.

## The default (no action needed from the user)
| Who | Model | Why |
|---|---|---|
| **Producing sub-agents** — visual-director (08), quality-controller (16); and by extension copywriter (06), humanizer (07) for routine work | **Sonnet** | Execution + checklist + verification work. ~5× less usage-limit weight than Opus. Set in each agent's frontmatter (`model: sonnet`). |
| **The main chat / dispatcher** (the model the user has selected in the app) | **the user's choice** — recommend **Sonnet** for routine production/dispatch | Dispatching (spawning agents, git, verifying files, MD updates) does not need Opus. Opus here burns the limit fastest. |
| **Genuinely novel creative work** — a first-of-its-kind concept, a hard debug, a strategy the pipeline has never done | **Opus** (spawn that ONE sub-agent on Opus) | Worth the cost only where deep reasoning changes the outcome. |

## The rule about switching (what the user asked for)
1. **Sub-agent needs a higher model?** The dispatcher CAN do this itself (the Agent tool takes a `model` override) → it just spawns that sub-agent on Opus and tells the user it did. No switch needed from the user.
2. **The MAIN chat needs a different model than it's currently on?** The dispatcher CANNOT change its own session model → it must TELL THE USER to switch, in plain terms, and say which model and why. The user switches via the app's model selector (or `/model` in a terminal Claude; `/fast` toggles Opus fast-mode).
3. **Default going forward:** unless a task needs deep creative reasoning, everything runs on **Sonnet** (sub-agents already do; the user may set the main chat to Sonnet too). The dispatcher only interrupts to request a switch when it genuinely matters.

## Plain-English version for the user
- Day to day, the workers (design, quality-check) now run on the cheaper **Sonnet** engine — I set that up, nothing for you to do.
- If one specific job needs the top **Opus** engine, I can put just that one worker on Opus myself, so I just do it and mention it.
- The only time I'll ask YOU to flip a switch is if the **main chat** (me) needs a different engine than it's on — because I can't change my own engine, only you can, in the app's model menu.
- Recommendation: keep the main chat on **Sonnet** for this production work; switch it to **Opus** only when we sit down to invent something brand-new (a fresh concept, a tricky problem). I'll tell you when that moment comes.
