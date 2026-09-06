# 🎨 Prompt-Writing Rules (image + carousel prompts)
**MANDATORY read for anyone who writes an image/carousel/video prompt: the Visual Director (08),
the Content Strategist (05, who writes the prompt packs in the calendar), and the Video Producer (09).
Read this BEFORE writing the first prompt, every time. QC (16) checks the output against it.**

*Created 2026-08-06 from user feedback on the agency P01 "one product / six worlds" test. The prompts
were too thin, produced six near-identical scenes, relied on the model to render headlines (it dropped
them 2 of 3 times), never specified fonts, and stamped the agency's own brand identity onto what is
supposed to be a client's product. This file exists so that never happens again.*

> These are ALL-CLIENT rules. A client can also have its own `clients/[name]/visual-remarks.md` that
> adds or overrides specifics for that brand (read it after this file; the client file wins on conflict).
> the agency's is `clients/[client]/visual-remarks.md`.

---

## ADOPTED WORKFLOW DECISIONS (locked 2026-08-06, all clients)
These four were approved by the user as standing practice, not one-off suggestions:
1. **Product hero FIRST, always.** Any multi-scene product post starts by generating + saving the product's
   hero reference image, then builds scenes from it. (Rule 1, step 0.)
2. **Reusable demo-product library for SERVICE brands.** A service brand with no real product keeps a small
   library of locked demo products, each with a written spec AND a saved hero image, reused across posts so
   they stay identical and build a recognizable portfolio over time. the agency: `clients/[client]/products/`.
3. **The text/logo pass is done IN CANVA (the Canva MCP), and the editable Canva design is KEPT.** Text + logo
   are composited, never model-generated. **Canva is THE compose tool for every slide's text/logo** (design +
   `export-design` → real editable SVG/PNG), not merely a "default": the reason is the user must be left an
   EDITABLE file he can open and tweak a word/position himself (a flat baked PNG can't be, and that is why we
   switched, user rule 2026-08-14). "Canva" ALWAYS means the Canva MCP, never "use nice fonts" (2026-08-11).
   HTML-to-image via headless Chrome is an EMERGENCY-ONLY fallback: use it solely if the Canva MCP is genuinely
   down, and in that case STOP and tell the user FIRST (never silently downgrade). When you do build in Canva,
   preserve/return the Canva design link/ID so the user has the editable original, not just the export.
6. **On-slide copy is CLIENT-FACING COPY and goes through the humanizer + QC before it is composed.** Any words a
   viewer READS on the finished image (headlines, sub-lines, callouts, coordinate labels, CTAs) are copy, exactly
   like a caption, and must come from the copywriter → humanizer → QC gate. The visual director does NOT write or
   improvise on-slide copy and does NOT lift raw planning text from a blueprint; it composes the APPROVED,
   humanized copy it is handed. (User rule 2026-08-14, after a planning-placeholder sub-line that had never been
   humanized shipped into a slide as broken English. The image PLATE PROMPT is instructions to the model and does
   NOT need humanizing; only the words that appear ON the slide do.)
4. **Consistent text-safe zones across a carousel.** Every slide reserves the SAME empty area (same corner,
   same size) for the composited headline/logo, so a swipe reads as one designed set. State the zone in every
   slide prompt.
5. **Use a reference-capable generator** when producing (so step 0's hero can actually be passed in as a
   reference). If the chosen free tool cannot accept a reference image, flag it to the user before producing.

---

## PROMPT VISIBILITY + IMPROVEMENT LOOP (user rule, 2026-08-11) — the prompt is ALWAYS saved where the user can see it
The user must be able to read every prompt we generate from, so when a picture is missing something we can find
the exact prompt, see what we forgot, and fix it (add/remove detail). So:
1. **SAVE EVERY PROMPT TO A FILE, VERBATIM.** Before or at generation, the producing agent writes the FULL final
   prompt to `clients/[name]/prompts/[YYYY-MM-DD]-[asset-slug].md` — the exact text sent to the model, the
   tool/model used, the reference image(s), and the palette + fonts. One file per asset. Never leave a prompt
   only in chat or only inside the agent.
2. **SHOW IT FOR SIGN-OFF (Rule 7).** That saved prompt file is what the user reviews BEFORE we generate.
3. **RESULT MISSING SOMETHING → UPGRADE THE PROMPT + THE RULES.** If the user or QC finds the image dropped a
   detail (a font, a texture, a small object, a safe-zone), the dispatcher (a) edits that prompt file to fix the
   miss, and (b) if it is a recurring lesson, adds it as a PERMANENT rule to THIS file so every future prompt
   includes it. This is how the agents' prompt-writing improves instead of repeating the same misses: this file
   is the agents' prompt-skill memory, the per-asset files are the record.

## RULE 0 — IDENTITY BEFORE THE PRODUCT SHOT (correct dependency order)
**The rule:** Build the brand identity FIRST, before generating any hero product image: the name, the palette
(named + hex), the fonts (real files), and the LOGO / label system. Only once the identity is locked do you
generate the product. You cannot brand a product before the brand exists. (User correction 2026-08-10: we
generated a blank bag before the demo brand even had a locked palette/font/logo. That is backwards.)

**Then, for the PRODUCT HERO, prefer GENERATING IT ALREADY BRANDED** (not blank-then-paste), when the subject
is a fictional/demo product and we control the identity:
- Hand the model the EXACT specs (font name + spacing, palette hex, the logo/label layout), and generate the
  bag/bottle already wearing its label, so the branding wraps the product's real 3D form and lighting and
  looks genuinely printed. A flat label pasted onto an angled product looks stuck-on; a printed-in label does
  not. Feed the deterministic label design (built per the two-step below) as the PRINT-SPEC / reference image.
- Then INSPECT closely (zoom every letter, Rule: verify text placement) and regenerate until the text/logo are
  correct. For a fictional demo brand, minor iteration is fine and cheap.
- This branded hero (product on a neutral set, no slide/marketing overlay) becomes the LOCKED REFERENCE fed
  into every later world/slide prompt, so the product stays identical everywhere.

**ANTI "AI-LUXURY" RULE (all clients, 2026-09-05).** The fastest way to make a product look AI-generated is
decorative filler standing in for real design. Do not add, and actively negative-prompt: decorative horizontal
rules / hairlines / underlines / wordmark frames / borders / separator graphics; dots, stars, sunbursts,
emblems, crests, monograms, seals, ornaments; over-spaced generic serif lettering; pseudo-editorial fonts;
fake engraved-looking type; unnecessary tiny text and fake packaging-detail clutter. Image models add these
unprompted, so state them as explicit negatives in every product prompt. **Strength comes from typography,
scale, proportion and restraint, not from added devices.** A branded product should look like it could
genuinely exist and be photographed in a real campaign. Per-house overrides live in that house's own file;
a demo house has stricter permanent rules (MV-1..MV-5) in `clients/[client]/products/[product]/product.md`.

**FOR the agency DEMO HOUSES specifically (2026-09-05):** the operational detail lives in ONE place,
`clients/[client]/products/README.md` (pipeline + live status) plus each `[house].md` (that house's
locked identity and hero). Read those; do not restate their contents here. Build the identity from
`templates/demo-product-identity-kit.md`. And use the HOUSE's palette: never stamp the agency's own
your agency's own palette onto a demo product or its world (serve the subject, not the agency).

**When to still use blank-then-composite instead (the two-step below):** flat graphic slides with no 3D form
(brand-board grids, palette slides, infographics, quote/hook cards), AND any REAL client's trademarked logo,
where letter-exactness is mandatory and a generation gamble is unacceptable. Product heroes of our own demo
brands = generate branded. Flat graphics + real logos = composite the real asset.

---

## The two-step we always use for FLAT graphics: GENERATE the plate, then COMPOSE the text
Every finished graphic is built in two passes, never one:
1. **Generate a clean, text-free image PLATE** from the prompt, with deliberate empty negative space
   reserved where text and the logo will go.
2. **Compose the text + the real logo on top IN CANVA (the Canva MCP)** using the actual brand fonts and the
   actual logo file, and keep the editable Canva design (see workflow decision #3: Canva is the compose tool
   because it leaves the user an editable file; HTML-to-image is emergency-only, stop-and-tell-the-user first).
   The on-slide text you compose must be the humanized, QC-passed copy (workflow decision #6), never raw
   planning text.

Why: image models drop, misspell, or garble text and mangle logos. In the agency test the exact same
prompt rendered the headline only 1 of 3 times. Text and logos are a design job, not a generation gamble.
This also satisfies our standing rule: never let a model re-draw a logo or wordmark, always composite the
real asset (see `output-quality-rules.md` → "use the client's REAL brand assets").

**Exception:** if a specific effect truly needs text baked into the generation, put the exact words in
"quotes" in the prompt, state their position and font intent, and QC every single generation frame-by-frame
for correct, complete, legible text. Even then, prefer compositing.

---

## RULE 1 — REFERENCE-FIRST for any multi-scene set of one product
**The rule:** When a post shows the SAME product in several scenes/slides (a carousel, a "X worlds" set,
a before/after), you must produce the product's HERO REFERENCE IMAGE as its own FIRST STEP, save it as a
file, get it approved, and only THEN build every scene FROM that saved reference (as an image reference /
img2img / edit base). The product is never re-invented per slide.
**Why:** The root cause of the agency P01 miss was process, not tooling: we wrote six scene prompts but
never generated the product FIRST, so each scene invented its own bottle and nothing matched. A saved
reference file also carries the product across different chats/sessions and lets the user drop it straight
into ChatGPT (or any tool) as the reference. This is the fix the user insisted on (2026-08-06).

**The mandatory order (do NOT skip step 0):**
0. **IDENTITY FIRST (Rule 0), THEN THE PRODUCT HERO.** Lock name + palette + fonts + logo/label BEFORE the shot.
   Then generate one clean hero of the product ON A SIMPLE NEUTRAL SET, and for a demo/own product generate it
   ALREADY BRANDED (Rule 0), not blank. Save it to the product's folder as the locked reference. Approve it
   (and inspect the printed text/logo up close) before any scene.
1. Build each scene/slide by passing that saved hero in as the reference image, changing only the world
   around it. Keep the product's scale, angle logic, and crop consistent so the swipe reads as one set.
2. Only after the plates are done, run the compose pass (text + logo), per the two-step above.

**How, per client type:**
- Real PRODUCT brands: the reference IS the client's real product photo (already the product-brand rule in
  `output-quality-rules.md`). Reuse the same photo/cutout in every slide.
- SERVICE brands using a demo/spec product: generate the hero ONCE, save it, and write a short product spec
  (shape, material, finish, cap, colour, label). Reuse that exact reference everywhere. For the agency this
  lives in the **demo-product library** (`clients/[client]/products/` — one spec + one saved hero per
  demo house; see `clients/[client]/visual-remarks.md`).

---

## RULE 2 — FONTS are mandatory in every prompt and every text spec
**The rule:** Never leave typography unspecified. For every piece of on-image text, name the exact typeface,
weight, case (UPPER/sentence), rough size in the hierarchy, tracking if it matters, and placement.
**Why:** Fonts carry identity; the right typeface can change a picture's whole feeling. the agency prompts
never named a font once. That is a missing ingredient, not a small detail.
**How:** Specify fonts for the COMPOSITING pass (that is where text lives). Use the brand's real font files,
never a lookalike. The wordmark is always the custom asset, never re-typeset. **Pull the exact fonts, weights,
sizes, case and tracking from the TYPOGRAPHY section of `clients/[name]/brand-profile.md`, every time.** Never
carry a font name from memory or an old brief; the agency's changed on 2026-09-06 and Sora/Inter are retired.

---

## RULE 3 — RIGOR: a prompt covers ALL of these, or it is not finished
A finished image prompt names every one of these. A prompt missing several of them produces generic output:
- **Subject** — the product, described exactly (for a demo product, copy it verbatim from its spec/reference).
- **Scene / world** — where it is, what surrounds it, the story implied.
- **Composition & framing** — placement, crop, rule-of-thirds/centred, foreground/background.
- **Camera feel** — lens/focal length feel, depth of field, angle, distance.
- **Lighting** — direction, quality (hard/soft), time of day, colour of the light, shadow behaviour.
- **Palette of the WORLD** — the scene's colours (this is per-scene and should VARY across a set, see Rule 4).
- **Materials & textures** — surfaces, and the small hero details. If a detail is the point (sand grains,
  water droplets, ripples), say it must be PROMINENT and in focus, not subtle. Thin details vanish otherwise.
- **Mood / emotion** — the single feeling the frame should give.
- **Aspect ratio + dimensions** — IG feed 4:5 (1080x1350) unless told otherwise.
- **Reserved negative space** — exactly where and how big the empty area is for the composited text + logo.
- **Negatives** — what must NOT appear (no text, no logos, no purple/blue AI tints, no extra products, etc.).

---

## RULE 4 — VARIETY discipline for "one product / N worlds" posts
**The rule:** The whole point of a "same product, different worlds" post is dramatic RANGE. Design the N
scenes as a deliberate set that differs on real axes: environment, dominant colour story, light, materials,
scale, era/mood. Write the set together and confirm no two read the same BEFORE generating.
**Why:** the agency P01 was meant to show six different results and instead showed six near-identical dark
scenes. When the worlds look the same, the post makes the opposite of its point.
**How:** Before prompting, list the N worlds in a table with their distinct axis (e.g. 1 = brutalist concrete /
cool grey, 2 = tropical garden / warm green, 3 = desert / bone + amber, 4 = water / teal, 5 = studio red, 6 =
snow / white). Each gets its own palette and light. Diversity is the deliverable.

---

## RULE 5 — SERVE THE SUBJECT, not the producing agency
**The rule:** When the image showcases a client's product (or a demo product standing in for one), the scene
serves the PRODUCT and its world. Do NOT impose the producing agency's own brand palette or graphic devices
(signature lines, brand colours) onto the product's worlds. The product keeps its own identity; the worlds
stay diverse. The agency signs the work only with (a) a subtle logo/tag, (b) the wrapper frames (cover slide,
CTA slide), (c) the caption voice, and (d) the text typography.
**Why:** User feedback 2026-08-06: the agency's red line + palette were stamped onto every P01 scene, so the
agency's identity was "too embedded in the product." But the product is supposed to be a client's, shown to
prove range. Painting our brand over it buries the message and misrepresents whose product it is.
**Where feed consistency actually comes from:** the "one visual universe" grid look lives in the WRAPPER
(cover/CTA slides, logo tag, caption voice, on-image typography), NOT in palette-stamping the showcase scenes.
Wrapper = consistent brand; showcase scenes = deliberately varied. That is how you get both at once.
**Subtle tag:** a small, tasteful logo/wordmark in a consistent corner as a credit/watermark. This is NOT the
big co-brand lockup used on formal deliverables (PDFs/reports); it is a light signature. Composite the real
logo asset (never model-drawn).

**Case-study / full-brand showcase carousels (refinement, user 2026-08-13):** when the WHOLE piece is a case
study of ONE (demo) client brand (for example the demo coffee brand flagship on the agency's own feed), the ENTIRE
carousel wears the SUBJECT brand's identity, its palette, fonts and motifs, on EVERY slide including the hook,
premise, strategy and sign-off. The producing agency does NOT brand the bookend / wrapper slides in its own
palette or graphic devices; its ONLY presence on the image is a subtle LOGO signature (the small corner tag),
like an artist signing the work. The agency's pitch is carried by the COPY and the logo, never by stamping its
colours over the case study. Rationale: the post is ABOUT the client brand and must read as a real, complete
brand world, not an agency-coloured thing. (This refines the "wrapper = agency brand" note above, which applies
to a mixed own-feed, not to a single-brand case study.)

---

## RULE 6 — Never alter the client's product to match a look
The product's real colours, branding, shape, and label stay true, always. Do not recolour or restyle a
product to fit a scene's palette or a trend. (Ties to the real-product-only rule and "stay true to brand
assets" in `output-quality-rules.md`.) For a fictional demo product, lock its look in its reference/spec and
keep it identical everywhere.

---

## RULE 7 — SHOW THE USER THE ACTUAL PROMPTS AND GET SIGN-OFF BEFORE GENERATING (hard gate)
**The rule:** Before ANY image/video is generated, the full written prompt(s) are shown to the user in plain
view and the user approves them. No generation runs on an unreviewed prompt. For a multi-asset post, show the
hero prompt first (it gets built + approved first anyway); show each subsequent scene prompt before that scene
is generated. The user reads to confirm nothing is lacking (detail, fonts, the world, negatives, safe zones).
**Why:** User feedback 2026-08-10. The user wants to read the prompt to understand what we are about to make
and to catch gaps BEFORE we spend a generation (and before a weak asset reaches QC). Reviewing the prompt is
the cheapest place to fix a picture. Skipping it is how the P01-style misses happen.
**How:** The producing agent writes the prompt to full Rule-3 rigor, the dispatcher surfaces it to the user
verbatim (not a paraphrase), the user signs off (or edits), THEN generation proceeds. Treat this like the
copy sign-off gate: a passing prompt is the user's call, not the agent's. Log the approved prompt with the asset.

## PROMPT SKELETON (fill every slot)
```
[Subject: exact product] in [scene/world], [composition/framing], [camera/lens feel + depth of field],
[lighting: direction + quality + time of day + colour], [world palette — specific hex or named colours],
[materials + the hero small details, made PROMINENT], [single mood word]. [aspect ratio + dimensions].
Leave clean negative space at [where + size] for composited text and a logo mark.
Negatives: no text, no logos, [no unwanted colours], [no extra objects], no purple/blue AI tint.
```
Then, separately, the COMPOSITION spec: headline text + font/weight/case/size/position · body text + font ·
logo asset + corner + size · exact brand hex.

---

## SELF-CHECK before handing off (and QC re-checks)
- [ ] Multi-scene set: one approved product reference reused in every slide (product identical)?
- [ ] Worlds genuinely distinct (palette/light/environment) across the set?
- [ ] Every prompt covers all of Rule 3 (esp. reserved negative space + negatives)?
- [ ] Text + logo are COMPOSITED in a design pass, not left to the model? Fonts named + real logo asset used?
- [ ] Showcase scenes serve the product, NOT stamped with the agency's palette? Subtle tag present?
- [ ] Product's real identity untouched?
- [ ] **Prompt(s) shown to the user and signed off BEFORE generating (Rule 7)?**

---

## RULE 8 — a MULTI-IMAGE GRID is built tile-by-tile, NEVER as one AI image faking a grid
**Rule:** when a slide shows several photos in a grid / feed-mockup / moodboard (e.g. the launch-feed slide),
NEVER prompt the AI for one image that *contains* the whole grid. The model renders the little pictures with
wrong, inconsistent details (garbled pack labels, a generic beach instead of the real origin, a basic off-brand
cup). Instead: **generate each tile as its OWN separate image** (one clean subject per generation, correct and
on-brief), then place each into a Canva square/frame. Consistent, high quality, every detail correct.
**Why:** the slide-8 launch-feed defect — one AI plate faked a 3×3 grid, so the coffee-bag labels were all wrong,
the "origin" tile was a random beach (not Ethiopia), and the cup was generic. User caught every one.
**How:** (a) list the tiles; (b) generate each separately per the reference-first rules (real bag from the locked
hero, the real origin = Ethiopia/Yirgacheffe, an ICONIC branded object not a generic one — e.g. a mug carrying the
the demo brand wordmark/coordinate, like a Starbucks-cup signature); (c) compose the grid in Canva with the tiles dropped
into square frames; (d) one generation per turn (usage limits). A grid slide is a COMPOSITION job, not a single gen.

## RULE 9 — feed the exact HEX to the AI only for the BRAND-PALETTE colours that must be exact
**Rule:** when an AI-generated image must contain an exact brand-identity colour (the navy ground, a gold rule,
the brand's own palette), put the exact hex in the prompt (e.g. "deep navy `#0D1B2A`") so the model targets it.
Do this ONLY for the locked brand-palette colours that matter for identity — NOT for every colour in a photo
(natural scene colours stay natural; over-specifying kills realism).
**Why:** AI models drift off-brand on colour; naming the hex pulls them back for the colours we actually lock.
**How:** name the hex for brand grounds/devices/palette elements; leave photographic/natural colours described in
words. Still verify the result and, where a colour must be pixel-exact (a palette chip, a ground behind text),
prefer building it natively in Canva over trusting the model (see BRAND-LOCK §10 item 3).

## RULE 10 — a HERO PRODUCT SHOT shows, it does not explain; let the eyes do the reading
**Rule:** not every slide needs callout labels, anatomy breakdowns, or explanatory text. When the slide's whole job
is "make the product look incredible," show the REAL product as the hero object inside a real environment it
belongs in (a styled coffee-shop table, a retail stand/shelf, a considered surface) — one clean, believable scene.
Minimal or NO on-slide text. The audience looks with their eyes; they don't need every detail narrated.
**Why:** a demo carousel slide 6 (the bag) crowded 8 anatomy callout labels onto what should have been a beautiful product
photograph. The user's point: a hero shot proves quality by BEING beautiful, not by captioning itself.
**How:** before writing an anatomy/label/callout layout, ask "does this need words, or does it need to just look
good?" Product-hero slides (the bag reveal, a lifestyle world, an art shot) default to show-don't-explain; only
genuinely educational slides (an infographic, the palette, the strategy) earn callouts/labels.

## RULE 11 — ONE uniform background per image, never a stitched patchwork of different grounds
**Rule:** an image must read as ONE consistent environment/background throughout. Never let an AI plate (or a Canva
composite) visibly cut between two different backgrounds — e.g. an orange/warm field on one side and a black/navy
field on the other, stitched together with a hard seam down the middle. If a slide needs product + a demonstrative
device (like a mini range-lineup), unify them in ONE considered scene/ground, not a collage of clashing fields.
**Why:** a demo carousel slide 7 stitched multiple mismatched backgrounds (an orange product background cut against a
black/blue one) — the user flagged this as something to never see again, on top of the concept itself being
retired (BRAND-LOCK §4/§8).
**How:** when reference-composing multiple product instances or scenes, generate them against the SAME ground/
lighting/palette, or build the composite natively in Canva with one deliberate shared background — never crop-paste
two AI outputs with different grounds side by side and call it one image.

## RULE 12 — TEXT SIZE: default bigger, never the cautious/small option
**Rule:** whenever a producing agent (or the dispatcher) has a choice of on-slide text size, pick the LARGER
option. Text has repeatedly come out too small to read comfortably at real feed viewing size, across multiple
clients and slides. When in doubt between two sizes, take the bigger one.
**Why:** standing user feedback (2026-09-04, the agency/a demo carousel slide 8): "whenever you choose how big is the
text, always make it bigger because they're always too small the ones you make." This echoes the earlier
2026-08-15 slide-1 finding (text + DB logo slightly too small, readability first) — a recurring pattern, not a
one-off.
**How:** QC must treat "text is legible but smaller than it needs to be" as a design-quality deduction, not just
a binary legibility pass/fail (legibility itself is already a Rule/hard-fail elsewhere — this rule is about
sizing UP even when something technically reads fine). Producing agents should err toward the larger end of any
size range in a template or layout, all-client, all formats.

## RULE 13 — PALETTE SWATCH HEX LABELS must be matched to the correct colour, always double-checked
**Rule:** when a slide shows a row of palette-swatch colour chips with hex-code labels underneath, the label
order MUST be verified against the actual chip order before export, every time. A hex code sitting under the
wrong-coloured chip is a hard, embarrassing, easy-to-miss defect.
**Why:** standing user feedback (2026-09-04, the agency/a demo carousel slide 8 rebuild): the hex codes were "written
under the wrong sync[c]... not under the right color."
**How:** after placing/editing swatch + label elements, the producing agent must do a left-to-right visual
cross-check (chip colour vs. its label's hex value) before exporting, not just trust that the elements moved
together. QC must independently re-verify this same left-to-right match, not just confirm the 5 hex strings
exist somewhere on the slide.

## RULE 14 — DON'T FORCE ON-SLIDE TEXT ONTO EVERY IMAGE
**Rule:** a strong image does not automatically need a headline/copy card composited onto it. Some shots (product
lifestyle photography, texture/mood pieces) read better and more premium as just the image plus the client's logo
mark, the same minimal treatment already used successfully elsewhere (e.g. the flagship demo carousel slides 11/12/13,
which carry no on-slide copy block beyond their short header line and the agency/brand logo).
**Why:** standing user feedback (2026-09-04, the agency): "we don't even have to add text on them... it does not
make sense. The only thing we add is the DB logo, same as the other pictures." Applies especially to a backlog of
already-strong images (e.g. unused ChatGPT plates) that don't need to be retrofitted with copy to be postable.
**How:** when a producing agent (content-strategist planning a post, or visual-director building one) is deciding
whether a slide/post needs a full copy treatment, default to asking "does this image need words to work?" rather
than assuming every post needs a headline. If the image alone carries the idea, ship it with just the logo. This
does not override Rule 7 sign-off or the copywriter→humanizer→QC gate for whatever text IS used — it just means
not every asset needs text at all.

## How to update this file
When any image/prompt feedback comes in, add or refine a rule here (Rule / Why / How), and tell the user.
Do not delete rules; mark superseded ones ~~struck~~ with a note.

*Last updated: 2026-09-04 — Rule 12 (SUPERSEDED 2026-09-06 by `system/text-size-rules.md`, which replaces 'pick the larger option' with hard numeric minimums, because 'larger' is not a number and the vague version did not work) (text size: always bigger), Rule 13 (palette hex labels must match their
chip's actual colour), and Rule 14 (don't force on-slide text onto every image) added from the demo brand feedback.*
*Prior: 2026-08-10 — added Rule 0 (identity BEFORE the product shot; generate demo product heroes already branded,
not blank-then-paste; blank-then-composite is for flat graphics + real trademarked logos). Earlier same day:
added Rule 7 (user reviews + signs off prompts before any generation).*
