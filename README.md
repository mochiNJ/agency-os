# AI Marketing Agency — Operating System
**GitHub:** https://github.com/mochiNJ/ai-marketing-agency
**Status:** In production. the agency (our own brand) is building its demo showcase; a client has one reel published.

---

## 📐 Read this first: where everything lives

**Before creating, moving, naming or deleting ANY file, read
[`system/file-system-law.md`](system/file-system-law.md).** It is the single source of truth for where
every file goes, what its status is, and when it dies. It contains **THE ROUTING RULE**, a numbered
decision tree that answers "where does this new file belong?" and tells you what to do when nothing
fits (create the folder AND register it, in the same turn).

| I want to know... | read |
|---|---|
| where a new file or document belongs | [`system/file-system-law.md`](system/file-system-law.md), "THE ROUTING RULE" |
| what a given folder is for | [`system/folder-registry.md`](system/folder-registry.md) |
| where anything in the repo lives | [`PROJECT-MAP.md`](PROJECT-MAP.md) |
| whether the repo currently obeys the rules | `python system/structure-check.py` |
| which files must change together | [`system/doc-dependencies.md`](system/doc-dependencies.md) |

```bash
python system/structure-check.py          # must pass before any filing work is called done
python system/sync.py                     # checks facts + dead links
```

---

## What This Is

A complete AI-powered marketing agency. 16 agents handle every part of client marketing
automatically — from onboarding to posting content. You manage the agency. The agents do the work.

---

## First-Time Setup (do this once)

### Step 1 — Install large skill packages
Open a terminal in this folder and run:
```bash
bash install-skills.sh
```
This downloads all 25 skills the agents need. Takes under a minute.

### Step 2 — Add your API keys
Open `.mcp.json` and replace the placeholder text with real keys:

| Placeholder Text | Replace With | Where To Get It |
|-----------------|-------------|----------------|
| `GET_FREE_AT_AISTUDIO.GOOGLE.COM` | Your Gemini API key | aistudio.google.com (free) |
| `GET_FROM_DASHBOARD.COMPOSIO.DEV` | Your Composio key | dashboard.composio.dev (free tier) |
| `GET_FROM_AYRSHARE.COM` | Your Ayrshare key | ayrshare.com (~$29/mo) |

### Step 3 — Onboard your first client
Open Claude Code (`claude` in terminal), then say:
> "Onboard new client: [Business Name]. Run brand-strategist."

---

## The 16 Agents

| # | Agent | Job |
|---|-------|-----|
| 01 | Brand Strategist | 13-question client onboarding — builds the brand profile |
| 02 | Competitor Researcher | Automatically researches competitors |
| 03 | Trend Spotter | Weekly real-time trend monitoring |
| 04 | SEO / AEO Agent | Website audit for Google + AI search (ChatGPT, Perplexity) |
| 05 | Content Strategist | 30-day content calendar |
| 06 | Copywriter | All captions, scripts, emails, ad copy |
| 07 | Humanizer | Removes AI writing patterns — mandatory before QC |
| 08 | Visual Director | All images and graphics |
| 09 | Video Producer | Short-form videos (TikTok, Reels) — uses Remotion (free) ✅ tested |
| 10 | Campaign Manager | Full campaign coordination |
| 11 | Paid Ads Manager | Meta and Google ad management |
| 12 | Email + WhatsApp | Retention sequences and broadcast templates |
| 13 | Influencer Agent | Creator discovery, vetting, and outreach |
| 14 | Publisher | Posts to all platforms (via Ayrshare or Postiz) |
| 15 | Analyst | Monthly performance reports + feedback loop |
| 16 | Quality Controller | 8/10 minimum gate — nothing ships without passing |

---

## How Content Flows

```
Client answers 13 questions (Agent 01)
    ↓
Research runs automatically — competitors, trends, SEO (Agents 02, 03, 04)
    ↓
30-day content calendar created (Agent 05)
    ↓ in parallel:
Copy written (06) → Humanized (07) → QC reviewed (16)
Images created (08) ────────────────→ QC reviewed (16)
Videos created (09) ────────────────→ QC reviewed (16)
    ↓ score ≥ 8/10
Published to social media (Agent 14)
    ↓ monthly
Performance analyzed → brain improves (Agent 15)
```

---

## Skills Installed (25 total)

**In GitHub** (14 marketing skills):
market-ads, market-audit, market-brand, market-competitors, market-copy,
market-emails, market-funnel, market-landing, market-launch, market-proposal,
market-report, market-report-pdf, market-seo, market-social

**Local only — run `install-skills.sh` to install** (7 large skills):
claude-seo, humanizer, email-marketing-bible, creative-director,
last30days, x-article-publisher, marketingskills

**Workflow skills from obra/superpowers** (4 skills — also in install-skills.sh):
dispatching-parallel-agents, writing-plans, executing-plans, systematic-debugging

**Built in-house** (2 skills — already in GitHub):
video-director, prompt-engineer

---

## System Files

| File | What It Does |
|------|-------------|
| `system/progress.md` | Full project status — say "show me progress" to read it |
| `system/changelog.md` | Every change ever made, including errors and fixes |
| `system/active-clients.md` | All clients list |
| `system/pipeline-status.md` | Where every piece of content is right now |
| `system/qc-log.md` | All QC decisions (pass/fail scores) |
| `system/weekly-trends.md` | Global trends, updated every Monday |

---

## Known Issue: GitHub Push Timeouts

If you ever see `error: RPC failed; HTTP 408` — that means GitHub cut off
the upload because it was too large. Large skill packages are intentionally
excluded from GitHub (see `.gitignore`). Run `install-skills.sh` to install
them locally instead. If a new large file causes this error, tell Claude Code
and it will handle it the same way.
