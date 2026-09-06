# 🔤 FONTS: why Canva could not do it, and what we do instead

**User, 2026-09-06, and he was right:** *"I feel the fonts used on the text are as much important as the whole
picture. When you put the font as fun, creative, or you change the boldness, or certain word size, and you play
with those details, what comes out would be amazing, but we cannot do this right now. So we need to fix this."*

He also correctly pushed back that the proposed fix (hand-build a donor design in Canva) was one he had
**already done once and it still failed.** This file exists so nobody proposes it a third time.

---

## THE DIAGNOSIS: three separate problems, not one

**1. The Canva MCP has no font parameter at all.**
`add_text` always uses the default sans. `format_text` can change size, colour and weight-ish styling, but has
no font-family field. There is no call anywhere in the connector that says "set this text to Sora." The only
way a non-default font ever appears is by **inheriting** it from a design that already contains it.

**2. There is a real, isolated bug in the inherit-then-edit path.**
`replace_text` on an element carrying certain fonts (reproduced on Cinzel, and on Dancing Script during the
a demo carousel slide-8 build) **silently corrupts the exported PNG to a fallback sans, while the live Canva preview
AND the saved design JSON both still look correct.** Isolated with a minimal single-edit repro. This is why the
user's hand-built donor design did not solve anything: the font was there, and the export still lost it.

Note it is not universal. The geometric sans used across the 13 a demo house slides survived `replace_text`
fine. The behaviour is font-dependent and therefore unpredictable, which is worse than a clean failure.

**3. The proper Canva route is unavailable on this account.**
Canva's real answer to "one design, many versions" is a **Brand Template plus autofill**, which is a different
code path from `replace_text`. Checked 2026-09-06: `search-brand-templates` returns an empty list, so there are
no brand templates, and autofill cannot be used. Creating them is a paid-tier feature and would still need
per-template manual setup, which is exactly the per-client manual work the user refuses (correctly).

**Why the earlier the demo brand posts had no font problem:** those designs already carried the right fonts and were
copied wholesale. We were never choosing a font, we were inheriting one that happened to be correct.

---

## THE FIX: render text locally with the real font files

**Verified working 2026-09-06.** The real fonts are free and now vendored in this repo:

| File | Source | Verified |
|---|---|---|
| `infra/fonts/_retired/Sora.ttf` | Google Fonts (OFL) | RETIRED 2026-09-06, see below |
| `infra/fonts/_retired/Inter.ttf` | Google Fonts (OFL) | RETIRED 2026-09-06, see below |

Proof render: `infra/fonts/_retired/PROOF-real-fonts-cover.png` rebuilt the P01 cover with a genuine
**Sora ExtraBold** headline and **Inter SemiBold** kicker, including manual letterspacing.
Script: `infra/fonts/README.md`.

**What this buys us, which is the whole point:**
- The client's ACTUAL brand fonts, not a lookalike.
- Any weight on the axis, any size, real letterspacing and leading control. The user explicitly named this:
  playing with boldness, size and emphasis on specific words is where the design lives.
- Works for **every client with zero manual preparation.** No donor design, no per-client Canva file. This is
  the requirement the Canva route kept failing.
- Deterministic and repeatable. What we render is what exports, with no preview-versus-export divergence.

**The tradeoff, stated honestly:** a locally rendered PNG is not an editable Canva file. The standing rule
preferred Canva *because* it leaves the user something to tweak by hand. That reason is real, but it is
defeated when the tool cannot apply the brand font in the first place. A wrong-font editable file is worth
less than a right-font flat one.

---

## THE RULE GOING FORWARD

- **Text on a photograph** (carousel slides, covers, quote cards, captions burned into an image):
  render locally with the vendored fonts. This is now the default.
- **Vector and brand assets** (logos, wordmarks, anything the user will hand-edit, anything needing real SVG
  export): still Canva MCP. That is what it is genuinely good at.
- **Never approximate a brand font with a lookalike again.** If the exact font is unavailable, STOP and say so
  before building, per the never-silently-downgrade rule.
- When a client's brand font is not already vendored, fetch it from its real source into `infra/fonts/` and
  record it here. Google Fonts direct raw URLs work; the `fonts.google.com/download?family=` endpoint returns
  an HTML page, not a zip, so do not use it.

## KNOWN DEBT
The 13 finished a demo house slides (2026-09-05) were built in Canva with a substituted geometric sans, not
Sora and Inter. They are QC-approved and shippable, but they do not match `brand-profile.md`. Rebuilding their
text layers through this pipeline is the obvious first job once it exists.

---

## ⛔ DECISIVE FINDING 2026-09-06: SORA IS NOT IN CANVA AT ALL

The user searched Canva's own font picker. **"sora" returns: "We couldn't find any results for 'sora'."**
Not a Pro-tier restriction. The font is simply not in Canva's library. ("inter" returns an ambiguous group
plus a Pro-crowned "Inters"; the real Inter was not confirmed.)

Canva's Apps SDK docs also state plainly: **"Apps can't upload or otherwise define custom fonts."**

**Therefore editable Canva text in Sora is permanently impossible.** Not a tooling gap, not a plan-tier issue,
not something a custom Canva app could ever solve. The proposed typography app was shelved on this basis.

**This turns a technical problem into a brand decision, and only the user can make it:**
- **Keep Sora and Inter** as the agency's fonts, and accept that finished slides are flat rendered images with
  perfect typography but no in-Canva editing.
- **Move the agency's typography to fonts Canva actually carries**, and keep full in-Canva editability forever.

**Worth knowing before he decides:** the agency's own LOGO already uses **Poppins SemiBold** for the descriptor
and small caps (see `brand-profile.md`). Poppins is a common Canva font. Aligning the brand's type system with
the font already inside its own logo is arguably better branding than Sora, which appears nowhere in the mark.

**✅ RESOLVED 2026-09-06: Path B was taken and the agency's typography is relocked.** The user confirmed Canva
availability, then delegated the choice ("this shouldn't be my job"), and the brand-strategist decided it.
**Sora and Inter are RETIRED.** The live spec, including the faces, weights, the full 1080x1350 type scale and
the three hard rules, is the **TYPOGRAPHY** section of `clients/[client]/brand-profile.md`. Do not restate it
here or anywhere else. The three directions considered are kept as reasoning only in
`clients/[client]/brand/typography-directions-2026-09-06.md`.

**Still owed before the first production build:** the `replace_text` smoke test in the section above must be run
once on each new face (the Cinzel and Dancing Script defect is font-dependent, so a new face proves nothing until
tested). `brand-profile.md` names the fallback if it fails. The new font files are not yet vendored into
`infra/fonts/`; the retired `Sora.ttf` and `Inter.ttf` there are kept only for reading pre-2026-09-06 builds.

**Note this is a [client]-only problem so far.** Client fonts may be fine: the demo brand's Cormorant and Dancing
Script both exist in Canva. Check each client's fonts against Canva's picker before assuming.

---

## 🧪 SMOKE TEST 2026-09-06: DM Serif Display + Poppins, before the 13-slide rebuild

**Requested test:** put DM Serif Display and Poppins on a throwaway design, export, run `replace_text` on both,
export again, compare pixels. Goal: confirm neither face suffers the Cinzel/Dancing Script export-corruption
defect before rebuilding the demo house slides.

**Result: the test could not be run. It failed at step 2, before `replace_text` was ever called.**

### What was tried

1. `generate-design` (design_type `instagram_post`, brand kit `kAGSnQ9zEOU`, query explicitly named "DM Serif
   Display" for the headline and "Poppins" for the body, asked for a plain two-text-element layout).
   Result: Canva ignored the font instructions entirely and returned an unrelated stock testimonial template
   (a beach photo, a quote, "John Smith, Customer Satisfaction Specialist"). Design `DAHUado9YSU`. Text ran on
   two opaque font refs (`YAFdJhem5V8,1` and `YAFdtQi73Xs,0`), neither identifiable as either requested face.
   Cancelled, not kept.
2. `generate-design` again (design_type `poster`, same brand kit, query repeated "DM Serif Display" and
   "Poppins" by name, asked for pure typography with no photography). Result: same two opaque font refs
   reappeared (`YAFdJhem5V8,1` for the serif headline, `YAFdtQi73Xs,0` for the sans body), confirming these are
   just whatever fonts happen to live in the matched stock template, not a response to the named fonts. The one
   place the literal words "Display" and "BODY" appeared styled like the two target faces was a baked-in stock
   PHOTO asset in the layout, not an editable text element, so it proves nothing about text handling and cannot
   be used for `replace_text`. Design `DAHUaSj2LQE`. Cancelled, not kept.

Both attempts passed a `brand_kit_id`. `list-brand-kits` returns only `{"id":"kAGSnQ9zEOU"}` with no font
metadata, so there is no evidence this brand kit has DM Serif Display or Poppins configured as its type styles.

### Why no donor-copy fallback was available

The established workaround (copy a design that already carries the target font, then `replace_text` on the
copy) needs a donor that already has the font. No such donor exists yet: DM Serif Display and Poppins were
decided today (2026-09-06) and have never been placed in any Canva design in this account. `search-brand-templates`
was already confirmed empty in the section above. So this run had no donor to copy from, and generating one was
the thing that failed.

### Confirmed, again, directly from the tool schema

`edit-design`'s `format_text` operation exposes `font_size`, `font_weight`, `font_style`, `decoration`,
`line_height`, `list_level`, `list_marker`, `strikethrough`, `text_align`, `color`, `link`. **No `font_family`
field exists.** `add_text` has no font parameter either. This matches the diagnosis already on record above:
the MCP cannot set a font directly, ever, on any face, only inherit one.

### Answers to the specific questions asked

- **Which route successfully applied each font:** none. Neither `generate-design` attempt, with or without the
  brand kit, applied DM Serif Display or Poppins to an editable text element.
- **Does DM Serif Display survive `replace_text` in the export?** Not testable. The font was never successfully
  placed on a text element to begin with.
- **Does Poppins survive `replace_text` in the export?** Same: not testable, for the same reason.
- **Did the Canva preview agree with the export, or diverge?** N/A, no divergence to check, since step 2 never
  produced the target fonts in the first place.
- **Design IDs for reproducibility:** `DAHUado9YSU` (instagram_post attempt), `DAHUaSj2LQE` (poster attempt).
  Both cancelled/uncommitted, kept only as evidence, not for reuse.

### Read: is the Canva MCP path viable for the 13-slide rebuild, or do we render locally?

**Render locally.** This is a harder finding than the replace_text bug it was meant to test for: that bug
requires the font to be present in a design first, and there is currently no working route in this Canva MCP
account to get DM Serif Display or Poppins onto a text element at all, brand kit included. Until a human
manually sets one of these fonts on a text box inside the Canva editor UI itself (creating a first donor to
copy from forever after), the MCP route is not just risky, it is blocked outright for these two faces.

This does not reopen the brand-profile.md font decision. It means the 13-slide rebuild should render text
locally with the vendored font files (the same pipeline already proven for Sora/Inter, described earlier in
this file), using genuine DM Serif Display and Poppins files, rather than trusting Canva to apply or preserve
them. Vector/logo work stays on Canva per the existing rule; this finding is about slide TEXT specifically.

**Before the rebuild starts:** vendor `DM Serif Display` and `Poppins` (Google Fonts, OFL) into `infra/fonts/`
(ticket stage 4c), and update the font-file table near the top of this document once that is done.
