# 🎨 Inspiration Library

**Purpose: show the agents what *good* looks like, instead of describing it in words.**
The user saves posts he loves; we decode each into a reusable **move** so every visual, video and caption
lands on a look he is actually happy with. This fixes the old failure mode (the client reel v3, the
"basic" client reels) where agents built from their own heads with nothing showing them the target.

## 🥇 THE GOLDEN RULE
**Steal the technique. Adapt it to THIS client and THIS product. Never clone the source.**
Copy the *how* (composition, lighting, mood, pacing, caption energy). Never the *what* (their logo, their
exact colours, their literal subject).

---

## How it is organised, and why

| folder | what it holds | why |
|---|---|---|
| [`sources/`](sources/) | **every screenshot, exactly once**, in a folder named for the account it came from | a screenshot's source never changes, so it never needs re-filing |
| [`recipes/`](recipes/) | **one card per technique**, tagged by business type, product type, format and technique | the technique is the thing worth keeping |
| [`by-business-type/`](by-business-type/) | **index files that POINT at cards** | a move can serve three business types while being stored once |

**Start at [`recipes/README.md`](recipes/README.md).** That table is also the "browse by product type / by
format" view: filter the columns.

### Why technique is the folder and business type is only a label

> *Restructured 2026-09-06.* The library used to be folders per business type. Every one of the 13 cards
> sat inside `ai-creative-agency/`, yet look at what they are: "the big-word poster hook", "mockup on a real
> surface", "playful 3D accent". **None of those is about creative agencies.** Filing them under a business
> type hid them from the coffee brand and the jewellery brand that needed them most.

Business type governs **register and taste**, not technique. A fragrance house and a 3D printing lab can use
the identical lighting move and should still not look alike. So type is a filter you apply while choosing,
never a wall you file behind.

And one file has one home; every other view points at it. That is RULE A of
[`system/doc-dependencies.md`](../system/doc-dependencies.md), and it is why nothing here is ever duplicated.

---

## Who reads this

Every producing agent reads **[`recipes/README.md`](recipes/README.md)** plus the
**[`by-business-type/`](by-business-type/) file for that client's type**, before the first draft.
QC checks that the output actually reflects them.

**There is no per-client board.** `clients/*/inspiration/` does not exist, and
`python system/structure-check.py` fails if one reappears. A rule that is specific to one client is not
inspiration, it is a brand rule, and it belongs in that client's `brand-profile.md` or `visual-remarks.md`,
which always win over anything here.

## Adding to it

1. Drop the screenshot in [`sources/`](sources/), under the account it came from. Any filename is fine,
   Claude renames it.
2. **Decode it into a card** in [`recipes/`](recipes/), named for the MOVE, never for the brand.
3. Add a row to [`recipes/README.md`](recipes/README.md) and a line in the matching business-type index.

**An undecoded screenshot teaches nobody anything.** a client's onboarding research sat here for seven weeks
as raw notes; six genuinely useful moves were in it, and no agent could reach any of them until they were
decoded on 2026-09-06.
