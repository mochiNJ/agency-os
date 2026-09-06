# fal.ai — our pay-as-you-generate image + video engine

**Status:** WIRED + LIVE-TESTED (2026-08-13). One key, one prepaid balance, every top model.
Key lives in `infra/fal/.env` (`FAL_KEY=...`, gitignored, never committed).

**How agents call it (direct-API — we do NOT edit the human-gated MCP settings file):**

```bash
# IMAGE (synchronous, seconds):
bash infra/fal/fal-image.sh <model-id> "<prompt>" <output.png> [image_size] [extra-json]

# VIDEO (queue + poll, minutes — costs real money, preflight with user first):
bash infra/fal/fal-video.sh <model-id> "<prompt>" <output.mp4> [extra-json]
```

`image_size`: `square` `square_hd` `portrait_4_3` `portrait_16_9` `landscape_4_3`
`landscape_16_9`, or exact pixels via extra-json: `'{"image_size":{"width":1080,"height":1350}}'`.

Both scripts read the key from `.env`, print the result URL, and download the file. They
need `curl` + `python` only (no `jq` — this Windows box has no jq).

---

## Model cheat-sheet — PICK THE BEST MODEL FOR THE TASK

> 📏 **STANDING RULE (user, 2026-08-13): price is NEVER the deciding factor.** Choose the model that
> gets us a perfect result in 1–2 tries. The $ column is for LOGGING (see `system/costs/`), not for
> picking a cheaper model. Remaking a cheap image five times is worse than nailing it once with the best.

| Job | Best model | Rough $/image | Notes |
|---|---|---|---|
| **Crisp brand TEXT, brand boards, infographics, anything with readable words/logo, 2K/4K** | **Nano Banana Pro** (Google Gemini 3 Pro Image) | ~$0.039–0.24 | ⭐ The user's go-to + genuinely SOTA for text/brand. DEFAULT for case-study/carousel slides. Confirm exact slug on fal.ai/models. |
| **Photoreal lifestyle / product scenes, strong instruction-following** | **GPT Image** (ChatGPT's model) | ~$0.005–0.21 | Top for realistic scenes. Confirm exact slug on fal.ai/models. |
| Throwaway draft / quick layout test only | `fal-ai/flux/schnell` | ~$0.003 | ✅ live-tested. NOT for finished slides. `{"num_inference_steps":4}`. |
| Solid photoreal without GPT Image | `fal-ai/flux-pro/v1.1` | ~$0.04–0.05 | Good Flux-family fallback. |

**Video** (per second, submit via `fal-video.sh`): Wan ~$0.05 · Kling ~$0.07 · Veo 3.1 ~$0.10–0.20.
Confirm the exact video model slug on https://fal.ai/models before the first run.

> ⚠️ Only the Flux family slugs above are verified by a live test. GPT Image + Nano Banana Pro
> slugs change occasionally — look them up on fal.ai/models and paste the exact `model-id` before
> the first call, rather than guessing. `text-free PLATE, then compose text` still applies (see
> system/prompt-writing-rules.md) for any image models that render text poorly.

## Balance
Pay-as-you-go, does not expire. As of 2026-08-13 the account had ~$2 loaded.
Whole the flagship demo carousel ≈ $1–3 of generation; a busy client month ≈ $10–15.
Top up at https://fal.ai/dashboard/billing. If balance hits $0, generations fail with HTTP 402 —
STOP and tell the user (never silently downgrade to a lesser tool).
