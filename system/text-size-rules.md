# 📏 TEXT SIZE: hard minimums, because ours has been unreadable

**User, 2026-09-06, with evidence.** He put our published the demo brand post next to `@yourmediasa` in the Instagram
profile grid. Theirs reads at a glance. Ours does not: *"I struggle to read it. I have to actually click on the
post and open it and make it bigger so I can read it comfortably."*

He is right, and this is a **conversion problem, not a taste problem.** People scroll a profile grid and decide
from the thumbnail whether to tap. If the cover text cannot be read at grid size, the post does not get opened.

An earlier vague version of this rule already existed (Rule 12, "always pick the larger text-size option") and
**it did not work**, because "larger" is not a number. This file replaces it with numbers.

---

## THE MATH (why the numbers are what they are)

All our masters are **1080 x 1350**. What matters is how big text is on a real phone.

| Where | How wide it displays | Scale vs the 1080px master |
|---|---|---|
| Post opened in the feed | full screen width, ~412dp | **0.38** |
| Profile grid thumbnail | one third of that, ~137dp | **0.127** |

Legibility floor on a phone: under **~12dp** is uncomfortable, under **~9dp** is effectively unreadable.

So to be read **in the feed**, master text must be at least `12 / 0.38` = **32px**, comfortably **37px+**.
To be read **in the grid**, master text must be at least `12 / 0.127` = **95px**, comfortably **119px+**.

## MEASURED on the 13 a demo house slides (2026-09-05), all of which passed QC

| Element | Master px | In feed | In grid | Verdict |
|---|---|---|---|---|
| Cover headline | 100 | 38dp | 12.7dp | borderline in grid |
| Kicker | 45 | 17dp | 5.7dp | fine in feed, gone in grid |
| Body line | **23** | **8.8dp** | 2.9dp | **UNREADABLE EVEN IN FEED** |
| Honesty label | **24** | **9.2dp** | 3.0dp | **unreadable, and it is a required disclosure** |

That is the defect, quantified.

---

## THE RULE (hard minimums on a 1080 x 1350 master)

| Element | Minimum | Target | Must be readable in |
|---|---|---|---|
| **Cover headline** (slide 1 of any carousel, and any single post's main line) | **120px** | 130 to 170px | **the profile GRID** |
| Headline on an inner slide | 70px | 80 to 110px | the feed |
| Body line, sub-head, any full sentence | **40px** | 44 to 56px | the feed |
| Tag, kicker, label | **40px** | 44 to 52px | the feed |
| Fine print, honesty label, disclosure | **32px** | 34 to 40px | the feed |
| **Absolute floor, anything at all** | **32px** | | if it is too small to read, do not put it on the slide |

**Nothing goes below 32px. Ever.** If a line will not fit at 32px, the line is too long: cut words, do not
shrink type. Shrinking to fit is the single most common way this rule gets broken.

**The cover is the one that earns the click.** It carries the strictest minimum on purpose. If the headline
does not read in a 137dp thumbnail, the post will not be opened, and everything else was wasted.

---

## HOW TO CHECK IT (do this, do not eyeball at 100%)

Run the previewer on every finished slide before QC:

```
python system/preview-at-real-size.py <image-or-folder>
```

It writes two extra files per slide into a `_size-check/` folder:
- `*-FEED.png` at 412px wide, how it looks when someone opens the post
- `*-GRID.png` at 137px wide, how it looks in the profile grid

**Then actually look at them.** The test is not "can I read it zoomed in", it is "can I read it there".
Judging text at full 1080px zoom is what let this ship in the first place.

## WIRED INTO
- `.claude/agents/08-visual-director.md`: build to these minimums, run the previewer before handing off.
- `.claude/agents/16-quality-controller.md`: **hard-fail** any slide breaching a minimum, and judge legibility
  from the GRID and FEED renders, never the full-size file.
- Supersedes the vague "pick the larger option" wording of Rule 12 in `system/prompt-writing-rules.md`.
