# fal.ai Setup — step-by-step (for a fresh chat)

**What this is:** a plain-English guide to get us a pay-as-you-generate image + video engine wired in.
We chose **fal.ai** because one account + one key gives us *every* top model on a single prepaid bill:
**GPT Image 2** (the model ChatGPT uses), **Nano Banana Pro** (Google, best for text/brand), **Flux**
(cheap/fast workhorse), plus the video models (Kling, Veo, Seedance, Wan). Balance is pay-as-you-go and
does not expire monthly. Full reasoning lives in the session-38 chat + `system/tool-sources.md`.

> 🧭 **How we split the work:** the steps marked **👤 YOU** need a human (signup, entering a card, copying
> the secret key). The steps marked **🤖 CLAUDE** I do for you in the new chat once you hand me the key.
> You do about 5 minutes of clicking; I do the wiring, testing, and building.

---

## PART 1 — 👤 YOU do this (about 5 minutes, in your browser)

### Step 1 — Create the account
1. Go to **https://fal.ai**
2. Click **Sign Up** (top right).
3. Easiest: choose **Continue with Google** and pick your account. (Email + password also works.)
4. No card is needed just to sign up.

### Step 2 — Add a card + a little balance
1. In the fal dashboard, find **Billing** (left side menu).
2. Add a **credit/debit card**. fal is pay-as-you-go: it charges the card only for what we actually
   generate. If the balance/card is missing, generations fail with a "402 payment" error, so this step
   is required.
3. If it offers a one-time **top-up / prepay**, load a small amount (**$10–$20 is plenty** — that covers
   the entire the flagship demo carousel with room to spare). If it only bills the card as-you-go, that's fine too.

### Step 3 — Create the API key (this is the thing you bring me)
1. Go to **https://fal.ai/dashboard/keys**
2. Click **Create new key**.
3. Give it a name, e.g. **`[client]-agency`**, and confirm.
4. **Copy the key immediately.** fal shows the full key **only once**. It starts with **`key_`** followed
   by a long string.
5. Paste it somewhere safe for a moment (you'll give it to me in the new chat).

> 🔒 **Keep this key secret.** It's like a password for spending your balance. Don't post it publicly or
> in a screenshot. When you give it to me, I store it in a **gitignored** file (never uploaded to GitHub).
> If it ever leaks, you can delete it on the keys page and make a new one in 10 seconds.

---

## PART 2 — 🤖 CLAUDE does this (in the new chat, after you paste the key)

You won't have to do any of this, just hand me the key and say go. I will:
1. **Store the key safely** in a gitignored config the agents read (`FAL_KEY=…`), never committed.
2. **Wire fal into** the visual-director (08) + video-producer (09) so they can call it. (Direct-API
   approach, so we avoid touching the human-gated MCP settings file.)
3. **Run one tiny, cheap test** first — a cost check + a small Flux image (a few cents) — to PROVE it works
   and returns a real image, before we spend on anything bigger. ("Connected" ≠ "working," we verify.)
4. **Show you the price before every generation** from then on (fal lets me preflight the cost).
5. **Start building a demo carousel slide 1** (the hook) — concept + exact prompt shown to you for sign-off first
   (Rule 7), then generate, one slide per turn.

---

## PART 3 — 👤 Paste THIS as your first message in the new chat (names the chat + tells me everything)

```
the agency — [today's date] — wire up fal.ai and build the flagship demo carousel slide 1

I created a fal.ai account and loaded a small balance. Here is my fal API key:
key_PASTE_IT_HERE

Please: (1) store it in a gitignored config, never commit it; (2) wire fal into the visual-director
and video-producer agents (direct-API, no MCP settings edit); (3) run one tiny cheap test image first
to prove it works and show me the cost; then (4) start building a demo coffee brand flagship slide 1 (the
hook) through the visual-director — show me the concept + exact prompt for sign-off BEFORE generating,
one slide per turn. Read docs/fal-ai-setup.md and clients/[client]/products/[product]/
blueprint-and-prompts.md for context.
```

---

## Model cheat-sheet (which "chef" I'll pick per job, all on fal)
| Model | Best for | Rough $/image |
|---|---|---|
| **GPT Image 2** (ChatGPT's model) | realistic scenes, strong instruction-following | $0.005–$0.21 |
| **Nano Banana Pro** (Google) | crisp text, brand boards, infographics, 2K/4K | $0.039–$0.24 |
| **Flux** (Black Forest Labs) | fast/cheap drafts + iteration | $0.003–$0.05 |

Video (also on fal, per second): Wan ~$0.05 · Kling ~$0.07 · Veo 3.1 ~$0.10–0.20.
Whole the flagship demo carousel ≈ **$1–$3** of generation. A busy client month ≈ **$10–$15**.
