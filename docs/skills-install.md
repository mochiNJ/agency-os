# Skills Installation

Skills are **vendored**: committed to this repo, so a clone already has them. `bash install-skills.sh`
VERIFIES that every folder in `.claude/skills/` is loadable (`SKILL.md` at the top, or `skills/*/SKILL.md`
for a pack) and exits non-zero if one is not. `bash install-skills.sh --fetch` additionally re-clones the
two packs whose upstream is confirmed, should they ever go missing.

---

## Auto-Install (Recommended)

```bash
bash install-skills.sh
```

Installs all 25 skills automatically. Re-run any time you set up a new computer.

---

## Manual Install — Marketing Skills

```bash
# Core marketing suite — 14 skills
# (market-ads, market-audit, market-brand, market-competitors, market-copy,
#  market-emails, market-funnel, market-landing, market-launch, market-proposal,
#  market-report, market-report-pdf, market-seo, market-social)
git clone https://github.com/zubair-trabzada/ai-marketing-claude
cp -r ai-marketing-claude/skills/* .claude/skills/

# SEO + AEO + GEO — 25 sub-skills, 18 sub-agents (free)
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo .claude/skills/claude-seo
rm -rf .claude/skills/claude-seo/.git

# AI writing humanizer (free)
git clone --depth 1 https://github.com/blader/humanizer .claude/skills/humanizer
rm -rf .claude/skills/humanizer/.git

# Email marketing bible — 55K words of strategy (free)
git clone --depth 1 https://github.com/CosmoBlk/email-marketing-bible .claude/skills/email-marketing-bible
rm -rf .claude/skills/email-marketing-bible/.git

# Creative director — 20+ methodologies, Cannes-caliber scoring (free)
git clone --depth 1 https://github.com/smixs/creative-director-skill .claude/skills/creative-director
rm -rf .claude/skills/creative-director/.git

# Last 30 days research — Reddit, X, YouTube ranked by engagement (free)
git clone --depth 1 https://github.com/mvanhorn/last30days-skill .claude/skills/last30days
rm -rf .claude/skills/last30days/.git

# X/Twitter article publisher (free)
git clone --depth 1 https://github.com/wshuyi/x-article-publisher-skill .claude/skills/x-article-publisher
rm -rf .claude/skills/x-article-publisher/.git

# Extra copywriting, CRO, and email skills (free)
git clone --depth 1 https://github.com/coreyhaines31/marketingskills .claude/skills/marketingskills
rm -rf .claude/skills/marketingskills/.git
```

---

## Manual Install — Workflow Skills (obra/superpowers)

```bash
# Installs all 4 from the obra/superpowers monorepo using sparse checkout
REPO="https://github.com/obra/superpowers.git"
for SKILL in dispatching-parallel-agents writing-plans executing-plans systematic-debugging; do
  TMP=".claude/skills/_tmp"
  git clone --filter=blob:none --no-checkout --depth 1 "$REPO" "$TMP"
  git -C "$TMP" sparse-checkout init --cone
  git -C "$TMP" sparse-checkout set "skills/$SKILL"
  git -C "$TMP" checkout
  cp -r "$TMP/skills/$SKILL" ".claude/skills/$SKILL"
  rm -rf "$TMP"
done
```

---

## In-House Skills (built in this project)

These are built into the repo — no install needed:

| Skill | File | What It Does |
|-------|------|-------------|
| `/video-director` | `.claude/skills/video-director/SKILL.md` | 5-phase creative pre-production for all videos |
| `/prompt-engineer` | `.claude/skills/prompt-engineer/SKILL.md` | Expands vague image/video requests into full production briefs |

---

## All 25 Skills — Which Agent Uses What

| Agent | Skills It Invokes |
|-------|-----------------|
| 01 Brand Strategist | `/market-brand`, `/dispatching-parallel-agents` |
| 02 Competitor Researcher | `/market-competitors`, `/competitor-analysis` |
| 03 Trend Spotter | `/last30days` |
| 04 SEO/AEO Agent | `/seo-audit`, `/ai-seo`, `/market-seo`, `claude-seo` |
| 05 Content Strategist | `/market-social`, `/content-strategy`, `/dispatching-parallel-agents` |
| 06 Copywriter | `/market-copy`, `/marketing-psychology`, `/copywriting` |
| 07 Humanizer | `/humanizer` |
| 08 Visual Director | `/creative-director`, `/banner-design`, `/canvas-design` |
| 09 Video Producer | `/video-director`, `/prompt-engineer` |
| 10 Campaign Manager | `/market-launch`, `/market-funnel`, `/market-proposal`, `/writing-plans`, `/executing-plans`, `/dispatching-parallel-agents`, `/creative-director` |
| 11 Paid Ads Manager | `/market-ads` |
| 12 Email + WhatsApp | `/email-marketing-bible`, `/market-emails` |
| 15 Analyst | `/market-audit`, `/analytics-tracking`, `/market-report`, `/market-report-pdf` |
| Any agent (when broken) | `/systematic-debugging` |

---

## Slash Command Reference

| Command | What It Does |
|---------|-------------|
| `/seo audit [url]` | Full SEO + AEO + GEO audit |
| `/market audit [url]` | Full marketing audit |
| `/market brand` | Brand voice analysis |
| `/market social` | Social content strategy |
| `/market copy` | Copywriting frameworks |
| `/market ads` | Ad creative and copy |
| `/market emails` | Email sequences |
| `/market competitors` | Competitive intelligence |
| `/market proposal` | Client proposal |
| `/market report` | Performance report |
| `/market report-pdf` | PDF version of report |
| `/video-director` | Pre-production brief for any video |
| `/prompt-engineer` | Expand vague brief into full production prompt |
| `/humanizer` | Remove AI writing patterns from any text |
| `/last30days` | Research what's trending right now |
| `/creative-director` | Develop and score creative concepts |
| `/email-marketing-bible` | Deep email strategy frameworks |
| `/dispatching-parallel-agents` | Coordinate multiple agents at once |
| `/writing-plans` | Write a detailed step-by-step plan |
| `/executing-plans` | Execute a plan with checkpoints |
| `/systematic-debugging` | 4-phase root cause diagnosis |
