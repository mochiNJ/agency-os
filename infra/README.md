# 🔧 `infra/` — the services and assets we actually run

**Charter: keys, fonts, containers and scripts that make the tools work. Never client content.**

| folder | what it is |
|---|---|
| `fal/` | the FUNDED image and video engine. `fal-image.sh` / `fal-video.sh` call the API directly (not an MCP). Key in `fal/.env`, never committed. Every generation is logged by `_log.py` into `system/costs/`. |
| `fonts/` | the real the agency typefaces, vendored: **DM Serif Display** (display) + **Poppins** (everything else). Slide text is rendered LOCALLY from these, because the Canva MCP cannot set a font family. See `system/font-pipeline.md`. |
| `postiz/` | the self-hosted publishing stack (`docker-compose.yml`). Reached publicly through a Cloudflare Tunnel at postiz.example.com. Values and gotchas in `system/verified-facts.md`. |
| `bin/` | downloaded binaries. **Gitignored and re-fetchable**, never source. |

## Rules

**Secrets never enter git.** `.env` files here are gitignored and were verified untracked on 2026-09-06.
`*.env.example` shows the shape without the values.

**A retired font is deleted, not parked.** `_retired/` held Sora and Inter after the typography overhaul
replaced them; it was removed on 2026-09-06 under LAW 4, since git is the archive.

**These files follow their own conventions**, not the repo's naming rules: `Poppins-SemiBold.ttf` is
correct as the font vendor ships it, and renaming it would break font lookups. `infra/` is therefore
exempt from the naming checks in `system/structure-check.py`.
