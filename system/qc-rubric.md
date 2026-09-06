# Quality Control Rubric

Used by Agent 16 (Quality Controller). Minimum score to pass: **8/10**. Zero exceptions.
**THREE ways to fail (reformed 2026-08-15):** (a) ANY critical defect in the CRITICAL DEFECT HARD FAILS list → the
slide CANNOT score ≥8, mark FAIL (a beautiful slide still fails); (b) raw score below 8; OR (c) the Creative Ambition
Gate caps it below 8 (a MID/BASIC verdict caps at 7, even at a perfect checklist 10). Final score = the LOWER of the
raw score and any cap; any hard fail forces it under 8.

> ⚠ **The authoritative, current QC logic lives in `.claude/agents/16-quality-controller.md`** (reformed after the
> 2026-08-15 slide-review brief). It adds: a CRITICAL DEFECT HARD-FAIL gate (missing/unreadable/clipped text or logo,
> empty placeholder, background seam, AI artifact, approximated/altered wordmark, wrong hex, inconsistent DB logo,
> retired/banned value, wrong tool for a deterministic slide), 3-lens scoring (Technical / Brand / Design — a Technical
> or Brand fail overrides the Design score), a TWO-STAGE QC (asset before Canva + final slide after), judging at FINAL
> VIEWING SIZE, and measuring against the project BRAND-LOCK file. Read that agent file for the exact gate; this rubric
> is the scoring reference underneath it.

---

## Pre-Check (before scoring)

For text content: confirm this file came from `pending-qc/` (processed by Humanizer), not directly from `pending-humanizer/`.

If the file came directly from the Copywriter without passing through the Humanizer → **REJECT immediately** and send back to Humanizer first. Do not score it.

Read before scoring:
1. `clients/[name]/brand-profile.md`
2. `clients/[name]/competitor-report.md`

---

## Scoring Rubric — 10 Points

### 1. BRAND ALIGNMENT (2 pts)
- **2** = Could ONLY be from this brand. Voice and style match perfectly.
- **1** = Mostly on-brand, minor inconsistencies.
- **0** = Generic. Could be any brand.

### 2. PLATFORM FIT (2 pts)
- **2** = Perfect format, length, hashtag count, dimensions.
- **1** = Functional but not optimized.
- **0** = Wrong format or violates platform conventions.

### 3. CONTENT QUALITY (2 pts)
- **2** = Strong hook, professional quality, clear CTA.
- **1** = Acceptable but forgettable.
- **0** = Weak hook, poor quality, no CTA.

### 4. STRATEGY ALIGNMENT (2 pts)
- **2** = Directly serves the content calendar goal.
- **1** = Related but not precise.
- **0** = Off-strategy.

### 5. ACCURACY & SAFETY (2 pts)
- **2** = No errors, no risks, all claims safe and accurate.
- **1** = Minor issue corrected.
- **0** = Error, misleading claim, or brand risk.

---

## ⭐ CREATIVE AMBITION GATE (applied AFTER the 5-dimension score — this is a CAP, not extra points)

**Why this exists:** a client reel scored a perfect 10/10 four separate times (v3, v4, v5, v6) and the client rejected every one as "mid / basic." The 5 dimensions above measure whether the work is *correct, safe, on-brand, on-platform*. They do NOT measure whether it is *good*. A technically flawless but forgettable asset was scoring 10 and still failing the only judge that matters — the client. This gate closes that gap.

**After you compute the raw score, ask three questions and be brutally honest:**
1. Would a top-tier studio actually ship this, or is it just "clean"?
2. Will the client be *excited* to post it, or merely okay with it?
3. Is there a real creative idea here, or only tidy execution of an obvious one?

**Assign ONE verdict, then apply its cap. The final score = the LOWER of (raw score, cap):**

| Verdict | Meaning | Score cap |
|---|---|---|
| **STANDOUT** | Genuine idea. A top studio would ship it. The client will want to post it immediately. | No cap — eligible for up to 10 |
| **COMPETENT** | Well-made but safe, expected, forgettable. Nothing wrong, nothing memorable. "Fine." | **Capped at 9** — cannot be perfect |
| **MID / BASIC** | Passes every technical check but has no spark. The kind of "correct but boring" work a discerning client rejects. | **Capped at 7 = AUTOMATIC REJECT** |

**Do NOT give the benefit of the doubt on this gate.** It exists precisely because clean-but-boring work kept scoring 10. If you are unsure whether something is STANDOUT or COMPETENT, it is COMPETENT. If it's "correct but I wouldn't be proud to sign it," that is MID/BASIC. A MID/BASIC rejection must include specific *creative direction* (not a checklist fix): what idea is missing, and one concrete direction to raise the ambition.

**Prevention beats rejection:** this gate is a backstop. The producing agent (video-producer, visual-director, copywriter, campaign-manager) should have run the `creative-director` / `video-director` skill BEFORE building, so the idea is strong on the first pass. If an asset arrives here MID/BASIC, that upstream gate was skipped — note it in the rejection.

---

## Extra Checks by Content Type

**Images:**
- Correct dimensions for the platform?
- PRODUCT BRANDS: Is the client's REAL product visible and accurate? (Never approve an invented version)
- Brand colors match the profile?

**Ads:**
- Is the creative from the `approved/` folder (not generated fresh)?
- Does the ad copy match what was approved?
- Is there a clear value proposition in the first 3 seconds (video ads)?

**Email / WhatsApp:**
- Has the Humanizer processed this? (no AI patterns remaining)
- Is there a single clear CTA per message?
- Does it comply with email/WhatsApp marketing regulations?

---

## Approved Stamp (score ≥ 8)

```
╔════════════════════════════════════╗
║  ✅ QC APPROVED                    ║
║  Score: [X]/10                     ║
║  Brand Alignment:   [X]/2          ║
║  Platform Fit:      [X]/2          ║
║  Content Quality:   [X]/2          ║
║  Strategy:          [X]/2          ║
║  Accuracy & Safety: [X]/2          ║
║  Creative Ambition Gate: STANDOUT / COMPETENT (cap 9) ║
║  Humanizer processed: YES/NO       ║
║  Revision cycles: [N]              ║
║  Approved for: [platform]          ║
║  Scheduled: [date/time]            ║
╚════════════════════════════════════╝
```

Move to: `clients/[name]/library/posts/[YYYY-MM-DD-slug]/`
Log in: `system/qc-log.md`
Notify: publisher agent

---

## Rejected Stamp (score < 8)

```
╔════════════════════════════════════════╗
║  ❌ QC REJECTED                        ║
║  Score: [X]/10  (minimum needed: 8)   ║
║  Creative Ambition Gate: MID/BASIC (cap 7) — if this is why ║
║  Failed: [which dimensions AND/OR the gate + why] ║
║  Required changes:                    ║
║  1. [Specific — never vague]          ║
║  2. [Specific]                        ║
║  (If gate failure: give CREATIVE direction, not a checklist fix) ║
║  Return to: [originating agent]       ║
╚════════════════════════════════════════╝
```

Move to: `rejected/`
Log in: `system/qc-log.md`
Return to originating agent with specific notes.

---

## Feedback Quality Standard

**BAD feedback (never do this):**
> "Improve the tone."

**GOOD feedback (always this specific):**
> "Opens with 'We are proud to present' — this brand's tone is bold and direct, not corporate. Rewrite opening as a provocative statement or question. Direction: 'This season we didn't follow trends. We ignored them.'"

Vague feedback wastes revision cycles. Every rejection note must name the exact phrase or element that failed, explain why it fails against the brand profile, and give a clear direction for the fix.

---

## Maximum Revision Cycles

After 3 failed cycles → STOP → escalate to human:

```
⚠️ HUMAN REVIEW REQUIRED
File: [filename]
Client: [client name]
Score after 3 cycles: [X]/10
Core problem: [summary of what keeps failing]
Recommendation: [what the human should decide]
```
