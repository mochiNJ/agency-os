# Tool & Skill Sources — where everything came from + update checks

**Purpose:** every external tool, skill pack, and agent we install comes from somewhere (usually a
GitHub repo). Those upstreams get **updated** by their authors. This file is the single list of where
each one came from so we can **check for updates on a schedule** (roughly monthly) instead of running
stale versions forever. Requested by the user 2026-08-12 after learning OpenMontage had shipped a big
update we would otherwise have missed.

**How to use it:**
1. Once a month (or when something misbehaves), go down the table and check each upstream for new commits/releases.
2. For a git-cloned tool: `git -C <local path> fetch && git -C <local path> log --oneline HEAD..origin/main` (or `git status`) shows if we're behind.
3. For a plugin/skill marketplace: re-run its install/update, or diff against the upstream repo.
4. Update the **"Last checked"** date + note what changed. If we update, log it in `system/changelog.md`.
5. **Never auto-update a tool we rely on mid-project without testing it first** (community code can break; see OpenMontage's `transformers` pin). Update on a calm day, then verify with a test render/run.

> ⚠️ **Honesty note:** entries marked **(confirmed)** have a verified upstream URL. Entries marked
> **(to confirm)** are our best guess — do NOT treat the URL as certain until someone verifies it.
> Better to leave it "to confirm" than to invent a repo.

---

## A) Standalone tools (installed software, their own repos)

| Tool | Upstream source | Local location | Update status | Last checked |
|---|---|---|---|---|
| **OpenMontage** (AI video/footage pipeline) | https://github.com/calesthio/OpenMontage **(confirmed)** | `OpenMontage/` (gitignored) | ⚠️ **UPDATE AVAILABLE** — upstream updated ~week of 2026-08-05; our install is months old | 2026-08-12 |
| **Postiz** (self-hosted publishing) | https://github.com/gitroomhq/postiz-app **(confirmed by product; verify exact fork/tag)** | `infra/postiz/` (docker) | check for new Docker image tag | 2026-08-12 |

## B) Skill / plugin packs (installed into `.claude/skills/`)

| Pack / skill | Upstream source | Notes | Last checked |
|---|---|---|---|
| **Anthropic Agent Skills** (pdf, pptx, xlsx, docx, canvas-design, skill-creator, etc.) | https://github.com/anthropics/skills.git **(confirmed — in `known_marketplaces.json`)** | marketplace `anthropic-agent-skills`, installed 2026-06-06 | 2026-08-12 |
| **claude-seo** (SEO/AEO agent suite) | https://github.com/AgriciDaniel/claude-seo **(confirmed — in its `marketplace.json`)** | big suite (seo-technical, seo-geo, seo-local, …) | 2026-08-12 |
| **marketingskills** (market-ads, market-emails, market-social, …) | https://github.com/coreyhaines31/marketingskills **(confirmed — in its `marketplace.json`)** | Corey Haines marketing skill pack | 2026-08-12 |
| **Planning/engineering skills** (systematic-debugging, writing-plans, executing-plans, dispatching-parallel-agents) | https://github.com/obra/superpowers **(to confirm)** | CLAUDE.md notes we adopted the "obra/superpowers methodology" 2026-08-05; verify these skills came from there | 2026-08-12 |
| **humanizer** | **(to confirm)** — based on Wikipedia "Signs of AI writing"; likely a public repo | our mandatory de-AI text gate | 2026-08-12 |
| **last30days** | **(to confirm)** — has its own repo | real-time social/web research skill | 2026-08-12 |
| **creative-director** | **(to confirm)** | Cannes/D&AD-calibrated concept engine | 2026-08-12 |
| **video-director** | **(to confirm)** | mandatory pre-production brief skill | 2026-08-12 |
| **email-marketing-bible** | **(to confirm)** | 908-source email KB | 2026-08-12 |
| **prompt-engineer** | **(to confirm)** | image/video prompt expansion | 2026-08-12 |
| **antigravity** | https://github.com/KINGSTAR-OMEGA/claude-token-optimizer **(CONFIRMED 2026-09-06 — repo fetched live; the raw image link inside our archived `_archive/Antigravity/README.md` points at that exact repo. MIT, by KINGSTAR-OMEGA. Note the README calls itself "Claude-Code-Enhancements", but the repo slug is `claude-token-optimizer`.)** | token-efficient execution skill. Upstream ships 3 variants (`antigravity/` V1, `antigravity2.0/`, `ultimate-protocol/`); **we run v2.0** at both user level and project level (`.claude/skills/antigravity/SKILL.md`). Full copy of the upstream download is kept at `_archive/Antigravity/`. | 2026-09-06 |
| **x-article-publisher** | **(to confirm)** | publishes Markdown to X Articles | 2026-08-12 |

## C) Connected MCP servers (services, not repos — track the account/credits, not code)

| MCP | What it is | Billing model | State (2026-08-12) |
|---|---|---|---|
| **fal.ai** (direct-API, key in `infra/fal/.env`) | image + video model aggregator (Flux, GPT Image, Nano Banana Pro, Kling, Veo, Wan) | **pay-as-you-go prepaid balance** (does not expire) | ✅ **WIRED + LIVE-TESTED 2026-08-13**, ~$2 balance. Called via `infra/fal/fal-image.sh` / `fal-video.sh` (NOT the MCP settings file). See `infra/fal/README.md` + `docs/fal-ai-setup.md`. Top up: fal.ai/dashboard/billing. |
| **Higgsfield** (`2f19b591-…`) | image + video + voice aggregator (Kling, Minimax, Seedance, Nano Banana, ElevenLabs) | subscription **or** one-time credit top-up packs | **free plan, 0 credits** — needs top-up to generate |
| **Canva** (`69f3b784-…`) | design + real SVG export | free (connected) | connected |
| **Postiz** | publishing | self-hosted (free) | connected via tunnel |
| **meta-ads** | Meta paid ads | needs OAuth re-auth | disconnected (auth required) |

---

## Maintenance log
- **2026-08-12** — file created. Seeded from `known_marketplaces.json`, each skill's `marketplace.json`,
  and the OpenMontage/Postiz docs. Flagged: OpenMontage update available; several skill upstreams still
  **(to confirm)**. TODO next: verify the "to confirm" repos and add exact commit pins.
- **2026-08-13** — **fal.ai wired + live-tested.** Key stored in `infra/fal/.env` (gitignored),
  direct-API helpers `infra/fal/fal-image.sh` (proven, Flux schnell) + `fal-video.sh` (built, not yet
  live-tested to save balance). Wired into visual-director (08) + video-producer (09). This is now our
  FUNDED default image/video engine, replacing the 0-credit Higgsfield for generation. Balance ~$2.
