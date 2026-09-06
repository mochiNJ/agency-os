# OpenMontage — System Re-Audit + Integration Plan (Session 24)

**Status:** ✅ DECIDED (2026-07-28, session 25) — **PARK IT.** Installed + working, NOT wired into
the pipeline. Use only for no-footage/service clients; never for PRODUCT brands. Run recipe +
gotchas live in [`docs/openmontage-setup.md`](../docs/openmontage-setup.md). Agent 09 has a pointer.
**Author:** Claude (Opus 4.8), 2026-07-28. Ground-truth verified live this session, not assumed.

> **Session-25 outcome (proof runs done):** Rendered a zero-key demo (world-in-numbers.mp4 — clean
> motion-graphics, but ≈ plain Remotion). Then a real-footage test with a live Pexels key: free/keyword
> path = 2/3 clips right (1 was pottery); after installing the CLIP libraries + fixing a real
> `transformers`-5.x bug, the smart CLIP-ranked path = 3/4 clips right (1 was a large-format 2D printer).
> **Verdict: OpenMontage's real value = footage/AI video for clients with NO footage of their own; it is
> not hands-off (a human still culls ~1 in 4 stock picks) and is the WRONG tool for a product brand like
> a client.** Decision: keep it in the drawer, labelled, don't rewire the house.

---

## PART 0 — Live ground-truth (verified this session, corrects an over-optimistic note)

OpenMontage is installed and its Python venv runs. I ran its own preflight
(`registry.provider_menu_summary()`) via `OpenMontage/.venv/Scripts/python.exe`.

**What is TRULY working, zero real keys:**
- **Composition: all 3 engines live** — `ffmpeg: true, remotion: true, hyperframes: true`. This is the
  prize. Remotion (React animated scenes/charts/captions) + HyperFrames (HTML/GSAP motion) + FFmpeg.
- **Narration:** Piper TTS (local, offline, free).
- Subtitles, video_post (9/9), audio_processing (2/2), screen_capture (cap+ffmpeg), character_animation
  (6/6), mermaid diagrams — all live and free.

**⚠️ IMPORTANT CORRECTION to our session-23 note.** The `.env` has *every* key present, but they are all
**placeholder values copied from `.env.example`** (I compared them byte-for-byte — FAL, OpenAI, Google,
Higgsfield, Pexels… all placeholders). The preflight lists a few Google providers (Veo, Imagen, Google
TTS, Gemini) as "available," but that is a **false positive** from the placeholder `GOOGLE_API_KEY` — they
would fail at real generation time. So the honest state is:
- **Real image generation: 0 providers** (stock keys Pexels/Unsplash/Pixabay are unset → unavailable).
- **Real video generation: 0 providers** (Veo/Kling/etc. all need real keys).
- **Truly keyless visuals today = Remotion/HyperFrames motion-graphics, text, data, charts, terminal
  scenes** — NOT AI images and NOT real product footage.

**Consequence:** OpenMontage's free path makes **motion-graphics / data / explainer** video beautifully.
It does **not**, with zero keys, make photoreal product video or pull stock footage. To unlock stock
footage (still free, no credit card) we need to drop in **free Pexels + Unsplash + Pixabay API keys**.
To unlock AI images/video we need paid keys (FAL, Google, etc.).

---

## PART 1 — FULL SYSTEM RE-AUDIT (against the goal: onboard → 30-day calendar + ready-to-publish posts + a video per chosen day)

Legend: ✅ have & working · 🟡 have but limited/unfunded · ❌ missing · $ = cost to close.

| Pipeline stage | Agent(s) | Status | What we HAVE | Gap / cost to close |
|---|---|---|---|---|
| Onboarding brief | 01 brand-strategist | ✅ | 13-Q flow, brand-profile.md | none |
| Competitor research | 02 | ✅ | agent + web/last30days | none |
| Trend spotting | 03 trend-spotter | 🟡 | last30days **4/7 sources** live | +TikTok/IG/Reddit = free **ScrapeCreators** key ($0) |
| SEO/AEO | 04 seo-aeo | ✅ | claude-seo skill suite | none (needs a live site to audit) |
| Content calendar | 05 content-strategist | ✅ | reads 4 brain files → 30-day calendar | none |
| Copywriting | 06 copywriter | ✅ | full skill stack | none |
| Humanizer | 07 | ✅ | mandatory gate | none |
| **Images/graphics** | 08 visual-director | 🟡 | **mcp-image (Gemini) free**; Higgsfield connected but **0 credits**; Claid unfunded | product brands OK (scene around real photo). Paid upgrade: Recraft ~$12/mo or Ideogram |
| **Video** | 09 video-producer | 🟡→**this is the weak spot** | Remotion+ffmpeg (our path) + the approved-visuals **bake** flow (proved on client reel). **No good path for a client with NO footage.** | **← OpenMontage closes this.** Free for motion-graphics; +free stock keys for footage; +paid for AI video |
| Campaigns | 10 campaign-manager | ✅ | coordinates 06/07/08/09 | inherits video gap |
| Paid ads | 11 paid-ads-manager | ❌ blocked | Meta Ads MCP present | **needs OAuth** (connector settings) — human gate |
| Email/WhatsApp | 12 | 🟡 | agent ready | needs Gmail/Mailchimp + WhatsApp(Composio) connect |
| Influencer | 13 | 🟡 | agent ready | needs Apify/Stormy MCP + key |
| **Publishing** | 14 publisher | ✅ | **IG + FB auto-post live** via Postiz + Cloudflare Tunnel; ≤25MB rule | TikTok paused (audit catch); YouTube to research |
| Analytics | 15 analyst | 🟡 | agent ready | richer once ads/GA connected |
| **QC gate** | 16 quality-controller | ✅ | 8/10 gate + qc-log | none — **stays the final gate over OpenMontage too** |

**One-line audit verdict:** the agency is strong end-to-end for a **product brand with real photos**
(exactly a client). The **single biggest capability hole is "video for a client with no footage"** —
which is precisely what OpenMontage is built to fill. Everything else is either working or a known,
cheap/human-gated connect.

---

## PART 2 — OpenMontage INTEGRATION DESIGN

### 2.1 The core decision: ALONGSIDE, not REPLACE

OpenMontage **sits alongside** our current video path as a new engine for **Agent 09
(video-producer)**. It does **not** replace our Remotion+ffmpeg + bake flow.

- **PRODUCT brands with real photos/footage (e.g. a client)** → keep our current path. The hard rule
  "real product footage, never invent the product" is safest when we control the compositing. OpenMontage
  may still be used here *only* in **source-footage / hybrid mode**, feeding it the client's real photos as
  fixed assets — never letting it generate the product.
- **SERVICE brands / any client with NO footage** → OpenMontage becomes the **primary** engine. This is
  the gap we cannot currently fill well.

Rationale: OpenMontage is brand-new community code (see risks). Making it the engine only where we have
*no better option* limits blast radius while capturing the whole upside.

### 2.2 Which of its pipelines map to our content types

| Our content type | OpenMontage pipeline | Zero-key? |
|---|---|---|
| Explainer / educational reel (service brand) | `animated-explainer`, `animation` | ✅ (motion-graphics) |
| Brand teaser / mood reel | `cinematic` | ✅ text/data; footage needs stock keys |
| Podcast → short clips | `podcast-repurpose`, `clip-factory` | ✅ (needs a source file) |
| Dub / translate an existing video | `localization-dub` | 🟡 (Google TTS/translate = key) |
| Software / app screen demo | `screen-demo` | ✅ |
| Talking-head / avatar | `talking-head`, `avatar-spokesperson` | ❌ needs GPU or paid |
| Real-footage documentary montage | `documentary-montage` | 🟡 needs free stock keys + deps |

### 2.3 How our HARD RULES survive (non-negotiable)

1. **Real product footage for PRODUCT brands** — OpenMontage is never allowed to *generate* a product.
   For product brands it runs only in source/hybrid mode on the client's real assets, or isn't used.
2. **Sound-on** — OpenMontage always scores + narrates (Piper/music). Satisfies the rule by default.
3. **8/10 QC gate** — OpenMontage's `renders/final.mp4` is treated as a *draft*. It still goes through
   **our Agent 16** and gets logged in `system/qc-log.md`. OpenMontage's own self-review is a bonus, not
   a substitute. No qc-log entry = deliverable does not exist (unchanged).
4. **≤25 MB publish copy** — our existing ffmpeg light-copy step runs on OpenMontage's final.mp4 before
   the Publisher touches it. Publishing pipeline is 100% unchanged.
5. **video-remarks + "Lebanon only" public-location rule** — fed into OpenMontage as brief constraints
   at the `idea`/proposal stage; on-screen text is screenshot-verified (existing rule) before QC.
6. **/video-director brief is still MANDATORY** — OpenMontage *starts* from a brief; our creative brief
   feeds its `idea` stage. A video without our brief is still forbidden.

### 2.4 What must change (only after your approval)

- **`.claude/agents/09-video-producer.md`** — add OpenMontage as the engine for no-footage video: the
  decision tree (product+photos → our path; service/no-footage → OpenMontage), the Windows run recipe
  (`OpenMontage/.venv/Scripts/python.exe`, no `make`), and the "still goes through our QC + light-copy +
  Publisher" handoff. Keep the bake/Remotion-direct path documented for product brands.
- **`/video-director` skill** — one note: for no-footage briefs, hand the brief to OpenMontage's pipeline;
  the 7-layer mandate maps onto OpenMontage's research→proposal→script→scene_plan→assets→edit→compose.
- **`CLAUDE.md`** — mention OpenMontage in the tool-audit expectation + pipeline reference.
- **`docs/openmontage-setup.md`** (new) — install/run/update steps, the placeholder-key gotcha, the free
  stock-key upgrade, the zero-key demo command. So the next session doesn't re-derive.

### 2.5 Where it lives / how we vendor it

**Recommendation: keep OpenMontage gitignored (do NOT commit it into our repo).** Reasons: it is large,
it is its own git repository, and it is **AGPLv3** (strong copyleft). We only *use* it locally — we never
redistribute it — so AGPL imposes nothing on us as long as it stays a separate, un-committed tool. We
instead **pin the exact commit hash** and document the clone+setup in `docs/openmontage-setup.md`. That
gives reproducibility without dragging a copyleft codebase into our history.

### 2.6 Risks (flagged honestly)

- **Brand-new community code** — test on throwaway briefs before any client work. Do not trust it on a
  client deliverable until we've seen it produce ≥8/10 output ourselves.
- **Preflight false-positives** — placeholder keys report Google as "available." Never promise a provider
  works until a real generation succeeds.
- **Zero-key ≠ product video** — free path = motion-graphics/text/data. Photoreal/footage needs keys.
- **Windows quirks** — no `make` (call venv python directly); HyperFrames needs Node ≥22; first npx
  render has a cold-fetch delay.
- **AGPLv3** — fine for internal use; matters only if we ever redistribute (we won't). Documented.
- **Usage/time** — real renders take minutes; one asset at a time (usage limits).

---

## PART 3 — EXECUTION PLAN (step by step, gated)

1. **PROVE IT (no repo changes):** render one zero-key demo end-to-end
   (`OpenMontage/.venv/Scripts/python.exe render_demo.py --list`, then render one, e.g. world-in-numbers),
   and show you the finished .mp4. Nothing is trusted until we see real output.
2. **Get your approval** on the ALONGSIDE design + the file changes in 2.4.
3. **(Optional, $0) unlock free stock footage** — add free Pexels/Unsplash/Pixabay keys so OpenMontage can
   pull real footage. You'd sign up (2 min each); I wire the keys in.
4. **Wire in** — edit the 3 files in 2.4 + write `docs/openmontage-setup.md`, pin the commit hash.
5. **Real test** — run one *service-style* brief through OpenMontage → our QC → confirm ≥8/10.
6. **Update** `system/progress.md` + `system/changelog.md`; you `git push`.

**Paused here for your approval before step 2 onward.** Step 1 (the demo) is safe and reversible — I can
run it now if you say go.
