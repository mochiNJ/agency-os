# OpenMontage — Setup & Usage (PARKED tool, ready on demand)

**What it is:** a free, open-source, local agentic video-production system
(github.com/calesthio/OpenMontage). It can (a) fetch **real stock footage** and cut
a finished reel, (b) generate **AI video** (with paid keys), and (c) render
motion-graphics/explainer video with its Remotion + HyperFrames engines.

**Status (decided 2026-07-28, session 25): PARKED — installed, working, NOT wired
into the pipeline.** Use it only for **no-footage / service clients**. Do NOT use it
for PRODUCT brands like a client (its clips are other people's products → misleading).
See the honest evaluation in [`system/openmontage-integration-plan.md`](../system/openmontage-integration-plan.md).

Lives in `OpenMontage/` — **gitignored** (large + its own AGPLv3 repo). Re-clonable from
GitHub. The Pexels key and installed libraries live only on this PC, never committed.

---

## What's installed & working on this machine (verified session 25)

- Python venv at `OpenMontage/.venv` (run tools with `OpenMontage/.venv/Scripts/python.exe`).
- Composition engines: **FFmpeg + Remotion + HyperFrames all live** (the zero-key path).
- Free narration: **Piper TTS** (offline). Free music search: **Pixabay**.
- **Pexels API key** is set in `OpenMontage/.env` (`PEXELS_API_KEY=…`) → unlocks real
  stock footage + images. Free, no card. (Get more: pexels.com/api.)
- **CLIP "smart ranking" libraries installed** (`torch`, `transformers`, `opencv-python`,
  ~4 GB) so `clip_search` / `corpus_builder` work — they semantically pick the best
  real clips instead of dumb keyword matching.

### ⚠️ Gotchas (already handled — keep them handled)
1. **No `make` on Windows** — call the venv python directly; don't use the Makefile recipes as-is.
2. **`.env` ships with placeholder keys** — `make setup` copies `.env.example`, so most
   providers read as "available" in preflight but are FALSE POSITIVES (would fail at
   generation). Only trust a provider after a real call succeeds. Real key set so far: Pexels.
3. **`transformers` version bug (FIXED):** newest `transformers` 5.x breaks OpenMontage's
   CLIP text-embedding (`'BaseModelOutputWithPooling' object has no attribute 'norm'`).
   Fix = pin to 4.x: `OpenMontage/.venv/Scripts/python.exe -m pip install "transformers>=4.40,<5"`.
   (Installed 4.57.6.) If OpenMontage is ever re-cloned/re-installed, re-apply this pin.
4. **Zero-key ≠ product/footage video.** With no real keys you only get motion-graphics/
   text/data (basically Remotion). Real footage needs the Pexels key; AI video needs paid keys.

---

## How to run it (the two paths we tested)

Both are driven from small Python scripts using the venv interpreter. Preflight first:

```bash
OpenMontage/.venv/Scripts/python.exe -c "from tools.tool_registry import registry; import json; registry.discover(); print(json.dumps(registry.provider_menu_summary(), indent=2))"
```

**A) Zero-key motion-graphics demo (proves the engine):**
```
cd OpenMontage && .venv/Scripts/python.exe render_demo.py --list
cd OpenMontage && .venv/Scripts/python.exe render_demo.py world-in-numbers
```
Output → `OpenMontage/projects/demos/renders/`.

**B) Real-footage reel (the useful path for a no-footage client):**
Two sub-paths, both driven via the registry tools:
- **Free / fast (keyword):** `direct_clip_search` (Pexels) → `video_stitch` → music via
  `pixabay_music`. Fast, no heavy libs, but keyword-literal (grabs the occasional wrong clip).
- **Smart (CLIP-ranked):** `corpus_builder` builds a CLIP-indexed pool → `clip_search`
  `rank_for_slot` picks the best clip per scene → `video_stitch` → music. Needs the
  torch/transformers libs (installed). Better picks; still ~1 in 4 needs a human cull.

Reference driver scripts from the session-25 evaluation show the exact tool calls and the
result-object shapes (`results[i].record.clip_id` / `.local_path`, etc.). The OpenMontage
agent contract (read before real production): `OpenMontage/AGENT_GUIDE.md`.

---

## Hard rules that survive any OpenMontage use (non-negotiable)
- **PRODUCT brands:** never use OpenMontage stock/AI clips as the product. Real product only.
- **Sound-on**, **/video-director brief first**, output is a **DRAFT** → **Agent 16 QC (≥8/10)** →
  **≤25 MB light copy** → **Publisher**. OpenMontage's own self-review does not replace our QC.
- Public content still says **"Lebanon" only** (never the town) — feed as a brief constraint.

## To fully remove it later
Delete the `OpenMontage/` folder (frees ~4 GB incl. the CLIP libs + downloaded clips). Nothing
else in the repo depends on it. The Pexels key dies with the folder (it's only in `OpenMontage/.env`).
