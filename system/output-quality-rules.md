# Output Quality Rules
**Living document — updated every time we get feedback on any output.**
*This file is read by all production agents before creating anything.*

---

## How to use this file
Every rule has:
- **The rule** (what to do or never do)
- **Why** (what went wrong or what worked)
- **Apply when** (which outputs this affects)

---

## PRIVACY & PUBLIC-SAFETY RULES

### NEVER: reveal a client's precise location (town/village/street/landmark) in public content
**The rule:** In anything the public can see — captions, on-screen video text, hashtags, geotags, bios, outreach messages, GBP posts — name only the **country/broad region** (e.g. "Lebanon"), never the specific town, village, street, or landmark, **unless the client has explicitly told us that exact place is safe to broadcast.** Keep the phone/WhatsApp and delivery offer; those don't pin a neighborhood. The precise address stays internal (delivery, records, an existing Google Business Profile the client already runs).
**Why:** Client instruction, 2026-07-28 (a client). In Lebanon, naming the exact town can signal things about a shop (including religious/sectarian read) that quietly narrow who feels comfortable ordering. Staying general keeps every customer welcome. This generalizes: a small business's exact location is sensitive by default — treat it as opt-in, not automatic.
**Apply when:** Every public-facing output for every client. For a client specifically: no `#[town]`/`#[town]`, no "in [town] / ب[town]," no [town]/Abu-Alia geotag — use "Lebanon." Full rule in `clients/[client]/brand-profile.md` (PUBLIC LOCATION RULE) and `video-remarks.md`.

---

## WRITING & COPY RULES

### NEVER: use an em-dash (—) or "—" in any paragraph or copy
**The rule:** Do NOT use em-dashes (—), and avoid the spaced " — " connector, in ANY written content — website copy, captions, emails, WhatsApp, reports, headlines, anything a client or the public reads. Rewrite the sentence instead: use a period, a comma, a colon, parentheses, or split into two sentences. This is absolute across every agent and every client.
**Why:** Client instruction (2026-08-04, the agency). The em-dash reads as a tell-tale "AI wrote this" pattern and the user dislikes it in his brand's voice. Removing it keeps copy human and intentional.
**Apply when:** Every piece of written content, every agent (copywriter, humanizer, email/WhatsApp, campaign, analyst, publisher captions), every client. The Humanizer must strip every em-dash before QC. QC must reject any copy containing "—".

---

## VISUAL & SLIDE PRODUCTION RULES (added 2026-08-15, from the agency slide-review brief)
*The user reviewed the first a demo carousel slides and found the QC agent was handing 9/10 to slides with a wrong
wordmark, missing hex labels, a clipped logo, an empty placeholder, and a retired coordinate. These rules fix the
root causes. They are HARD FAILS: QC cannot score a slide ≥8 if any is violated, however pretty it looks.*

### RULE: Use the best tool for the job. AI is NOT mandatory for every slide.
**The rule:** Before generating anything, decide whether the slide actually benefits from AI. DETERMINISTIC slides
(colour palettes, hex codes, typography specimens, coordinates, lines, labels, simple grids, information/strategy
cards, geometric layouts) are built FULLY in Canva-native shapes/text, no AI plate. AI is for PHOTOGRAPHIC /
ATMOSPHERIC / ARTISTIC content only (landscapes, product/lifestyle scenes, art stills, textured backgrounds). If
only a background photo is needed, generate only that and build text/logos/shapes natively on top.
**Why:** The slide-4 palette was AI-generated and came back with mismatched blues, missing labels, and a clipped
logo. A palette is exact data; Canva makes it perfectly, AI approximates it badly and costs credits.
**Apply when:** Every slide, before any generation. (visual-director GATE 2; QC tool-choice check.)

### RULE: Use the real supplied brand asset exactly. Never approximate a logo/wordmark with a font.
**The rule:** If an official logo/wordmark/SVG/PNG/vector is supplied, use that exact file. Never re-typeset,
re-draw, or let a model render a brand mark. If the asset is awkward (e.g. a raster embedded in an SVG), repair the
asset (clean transparent PNG export), do not substitute a font.
**Why:** Slides 3 and 5 approximated the demo brand wordmark with a font instead of the supplied art. A client's mark
must be exact; even small changes mean it is no longer their logo.
**Apply when:** Any slide showing a brand mark. (the demo brand wordmark + the agency logo. QC brand-correctness hard fail.)

### RULE: Typeset text uses the client's locked faces, weights, case and tracking. No synthetic styling. (added 2026-09-06)
**The rule:** Every word of typeset text pulls its face, weight, size, case and tracking from the **TYPOGRAPHY
section of `clients/[name]/brand-profile.md`**, read at build time. Never from memory, never from an old brief,
never from a job ticket that disagrees (the file always wins, and the producing agent STOPS to flag the conflict).
**Three hard fails:** (1) a face not in that file, (2) **synthetic bold or synthetic italic applied to a single-weight
display face** (the agency's DM Serif Display has exactly one weight; hierarchy is built in the sans, never faked in
the serif), (3) a display serif set below its stated floor, or set for body, labels, kickers or fine print.
**Why:** the agency's fonts were a paper spec (Sora) that no tool could actually produce, so builds silently
substituted whatever was to hand and every slide set drifted. The 2026-09-06 relock fixed the spec; this rule is
what makes it bite. A single-weight serif is only safe if nobody fakes a bold on it.
**Apply when:** Any slide, cover, PDF, thumbnail or overlay with typeset text. QC brand-correctness hard fail.

### RULE: the agency logo — identical size + position on every slide, never clipped.
**The rule:** the agency signature sits bottom-right in a fixed 180×120px clear zone, ~48px margin, the SAME size
on every slide, fully inside the artboard, never clipped by the edge or crossing a frame line, never on a
cream/greige patch.
**Why:** Slide 8's logo ran off the canvas edge and was a different size than the rest of the deck.
**Apply when:** Every deck. Consistency across the carousel is mandatory.

### RULE: Judge and finish at FINAL viewing size; no empty placeholders; no background seams.
**The rule:** Text must be comfortably readable at normal phone-feed size (not just zoomed into Canva); keep a clear
hierarchy; the logo must be readable. Every placeholder shape must hold its content before export. The Canva ground
colour must equal the plate colour exactly (no two-blues seam).
**Why:** Slides 1/2/5 had text too small to read; slide 3 left empty squares; slide 4 had a visible blue seam.
**Apply when:** Every slide, at export and at QC (final-viewing-size check).

### RULE: Text/background COLOUR CONTRAST is a hard-fail dimension, not a design nitpick. (added 2026-08-24)
**The rule:** On-slide text must be genuinely legible against whatever sits behind it — check actual contrast
(luminance + hue difference), not just "is it a different colour." Two near-identical hues (e.g. orange text on an
orange/yellow-toned background) can be technically distinct colour values and still be functionally invisible.
Also applies to text sitting across a busy photo, a map graticule line, or any element crossing it.
**Why:** a demo carousel slides 11/12 used text too small AND in a colour too close to its background to read at feed
size — caught by the client, not QC, on the second review pass. His own words: "if you put unreadable text then
the whole picture should get 0."
**Apply when:** Every slide with on-image text, at final-viewing-size QC. **Unreadable text caps the slide's score
at 0** — same severity tier as a wrong logo or an invented spec, not a minor deduction. (visual-director finish
check; QC hard-fail gate.)

### RULE: ANY locked brand device with a real asset file must be composited from that file — not just the wordmark.
**The rule:** The "never approximate the wordmark with a font" rule above extends to every recurring brand device
that has its own locked source file — a coordinate mark, a compass rose, a custom icon, a repeating graphic motif.
If it exists as a real file once it's been built/approved, every later slide that needs it composites that exact
file. QC must diff the actual asset file against what's on the slide, not eyeball "looks about right."
**Why:** the demo brand's coordinate device (`06°15'N`, locked as
`campaigns/[product]-flagship/identity/[product]-slide.png` after slide 5) got
re-rendered/re-typed on slides 9, 10, 11, and 12 instead of reused — the same class of mistake as the wordmark
violation that already sank slides 3/5 once, this time missed by QC across two separate passes.
**Apply when:** Any slide reusing a device that already has a locked asset from an earlier approved slide.

### RULE: Two-stage QC — asset first (before Canva), final slide always (after Canva).
**The rule:** QC the raw AI plate for artifacts/fake-text/wrong-mark BEFORE composing in Canva, then ALWAYS QC the
final exported slide. Nothing passes on the strength of the raw asset alone.
**Why:** Clipped logos, seams, wrong positioning, unreadable text only appear in the final composition.
**Apply when:** Every composited slide. (visual-director asset-QC step; QC agent Stage A + Stage B.)

---

## ✅ PRODUCTION READINESS — what actually blocks production, and what does NOT (per client)
**Read from `clients/[client]/brand-profile.md` before producing. This corrects an earlier over-strict reading that treated missing prices and missing brand assets as blockers. They are not.**

### Client type decides what is needed (PRODUCT vs SERVICE)
- **PRODUCT brand** (sells physical items): real photos of the SPECIFIC product we are featuring are required, because we never invent a client's product. No photo for a given product = that product's posts wait until a real photo exists; re-sequence the calendar around what is shootable now. See `system/client-types.md`.
- **SERVICE brand** (no physical product): NO product photos needed, ever. Visuals are generated from scratch around the service outcome. A service client is NEVER blocked on "product photos."

### Prices are NOT a blocker and NOT public by default
- It is not our job to advertise prices on social. **A missing price NEVER blocks production.**
- Even when we know the price, we do NOT put it in public content unless the client explicitly asked us to (decided per product). Default posts drive people to comment / DM / WhatsApp / contact, not "buy for $X."
- Read `show-prices-publicly` in brand-profile.md. If it is NO or unset, no price appears in public copy, full stop.

### Brand visual identity is the client's CHOICE, not a requirement
- We always ASK whether the client wants us to use their own logo, specific fonts, and brand colors (onboarding Q8/Q9).
- If they provided them and want them used (`brand-identity-provided … use-them: YES`): use them EXACTLY, the real logo file, exact hex, exact fonts, never recreated by hand (the real-brand-asset rule).
- If they did not, or prefer creative freedom: design a look that fits the brand. Not having a logo/font/colour on file is NOT a blocker.

---

## 🎯 HOUSE TASTE — the point of view every producing agent works from
**Added 2026-08-05. Read this before building. Skills give you craft; this gives you a spine.**
Our agents were executing steps correctly and still shipping forgettable work. A skill tells you HOW; this tells you what we REFUSE to ship and what we AIM at. Every producing agent (copywriter, visual-director, video-producer, campaign-manager, email/whatsapp) adopts this stance:

- **Have ONE idea per asset.** Not three half-ideas, not a checklist of features. If you cannot say the idea in one sentence, it isn't one yet. Clean execution of no idea is the definition of "mid."
- **Earn the first 1.5 seconds.** The hook is the whole job on a scroll feed. A tasteful, obvious opening loses to a specific, surprising one.
- **Specific beats generic, always.** Real detail (a real name, a real number we're allowed to use, a real moment) reads as true. Vague aspiration reads as AI filler.
- **Confidence over decoration.** Premium brands say less and trust the product. Effects, extra text, and busy layouts are usually fear that the idea is weak. Fix the idea, not the polish.
- **Would I be proud to sign this?** If the honest answer is "it's fine," it is not done. "Fine" is what the Creative Ambition Gate rejects. Aim for "the client will want to post this immediately."
- **We refuse to ship:** generic stock-feeling work, copy that could belong to any brand, a video with no idea behind the edits, anything that only clears the checklist. Correct is the floor, not the goal.

---

## UNIVERSAL RULES — THE MAXIMUM QUALITY MANDATE
**Added 2026-07-17 after a client reel v3 failure. These apply to EVERY task, EVERY agent, EVERY output type. They override convenience, speed, and habit.**

### ALWAYS: Run a TOOL AUDIT before building anything
**Why:** a client reel v3 was built with basic zoom + crossfade while 21 professional Remotion packages (light leaks, motion blur, real film grain, 3D, sound effects, captions) sat installed and unused. The result looked amateur because the build defaulted to the easiest path, not the best one.
**Apply when:** Every task — video, image, copy, email, report, everything.
**How:** Before writing a single line of code or content, list every installed tool, package, and skill relevant to this task. State which ones will be used and why. If a relevant installed tool is NOT being used, that requires a written justification. "I didn't think of it" is not a justification — it's the failure mode this rule exists to prevent.

### ALWAYS: Tell the user when a better tool exists that we don't have
**Why:** The user cannot know what tools exist. The agent can. If the best possible result requires a tool, package, or paid service we don't have, the agent must proactively say so BEFORE building — with the tool name, what it adds, and the cost — so the user can decide. Silently settling for less is a violation.
**Apply when:** Any task where the achievable quality is capped by missing tooling.

### NEVER: Settle for "it works"
**Why:** "It renders without errors" is not the goal. The goal is the best result possible with everything at our disposal. Content that merely works but doesn't impress is a failure even if it's technically correct.
**Apply when:** Always.
**How:** Before calling any output done, ask: "Is this the absolute best I can produce with the tools installed? Would a top-tier professional studio ship this?" If the answer is no, it is not done.

### ALWAYS: Enforce skill mandates as hard requirements, not suggestions
**Why:** The /video-director skill mandated a 7-layer cinematic stack. The v3 build implemented ~3 layers and shipped anyway. Skill requirements described in words were treated as optional inspiration. Never again.
**Apply when:** Any task governed by a skill with explicit requirements (e.g., video-director's 7 layers, prompt-engineer's full prompt structure).
**How:** Before saving output, check off every mandated element by name. Any missing element = the output is incomplete and must not leave the agent.

### ALWAYS: Run the creative gate BEFORE building, and expect the Creative Ambition Gate at QC
**Why:** a client reel scored a perfect 10/10 in QC four separate times (v3, v4, v5, v6) and the client rejected every one as "mid / basic." Our old rubric measured whether work was correct, safe, on-brand, and on-platform. It never measured whether the work was actually GOOD. Correct-but-boring was scoring 10 and still failing the only judge that matters: the client.
**Apply when:** Every produced asset (video, image, copy, campaign, ad).
**How:** (1) BEFORE the first build, run `creative-director` (or `video-director`, which includes it): find the insight, the idea, the reason this will stop a scroll. Do not skip to execution. A build with no idea is a slideshow. (2) At QC, Agent 16 now applies a CREATIVE AMBITION GATE on top of the /10 score: STANDOUT (no cap), COMPETENT (capped at 9, cannot be perfect), or MID/BASIC (capped at 7 = automatic reject, with creative direction). A flawless checklist score no longer guarantees a pass. Aim for STANDOUT on the first pass, not through client-rejection cycles. Full rubric: `system/qc-rubric.md`.

### NEVER: Deliver anything to the user without QC actually running
**Why:** As of 2026-07-17, system/qc-log.md showed 0 reviews EVER — the 8/10 gate had never once been exercised. The user personally caught garbage that Agent 16 was supposed to catch.
**Apply when:** Every single deliverable, zero exceptions.
**How:** The delivery pipeline is: build → self-check against this file + skill mandates → Agent 16 QC review with score logged in system/qc-log.md → only then show the user. A deliverable with no qc-log entry does not exist and must not be presented.

### ALWAYS: Use the client's REAL brand assets — never recreate them by hand
**Why:** a client's reel outro had the client wordmark and its sub-line re-typed by hand in a lookalike font with a wrong
3D-LAB gradient, instead of using the actual logo file the client supplied (with exact hex + lettering).
The client rejected it and made this a permanent rule for every future project.
**Apply when:** Any deliverable that uses a logo, wordmark, brand colour, or brand font — videos, images, everything.
**How:** Composite the real supplied asset image verbatim. NEVER rebuild a logo/wordmark in code/drawtext/CSS
with an approximated font or guessed colours. Use the client's exact hex codes and exact fonts. If the needed
asset is missing or too low-res, STOP and ask the client — do not approximate.

### ALWAYS: Put the real logo ON every branded deliverable (co-brand client work)
**Why:** the session-31 agency competitor-report PDF had no logo — "the agency" was just typeset in Sora, so it
did not read as a real branded document. A deliverable without its logo looks unfinished.
**Apply when:** Any deliverable a client or consumer sees: reports, PDFs, decks, one-pagers, images, video covers.
**How:** Place the real logo asset (cover, ideally repeated small in the footer). For CLIENT work, co-brand:
show BOTH our agency logo AND the client's logo. Pull the actual file from the client's brand/uploads folder;
never retype the name in a font. For our own agency (the agency) use `clients/[client]/brand/logo/primary/
[client]-primary-navy.png` (dark backgrounds) or `[client]-primary-black.png` (light/documents) — see
`clients/[client]/brand-profile.md` for the full asset list. **The old `[client]-wordmark.svg` + M·E mark are
RETIRED and archived in `brand/_archive/old-[client]-identity/` — never reference them as current (fixed
2026-08-22, this rule was pointing agents at a dead file).** This is the presence half of the "use REAL brand
assets" rule above.

### ALWAYS: Write deliverables FOR the client and consumer, not in internal agent voice
**Why:** Our research/strategy `.md` files (competitor-report, brand-profile, trend-report, etc.) are brain files
for the agents, but their PDF/image/video versions are client deliverables and a real value-add extra ("we made
this for you"). Session-31: the agency PDF's page-2 kicker "READ THIS BEFORE ANYTHING ELSE" leaked straight from
the MD and read like an instruction to Claude, not to the client.
**Apply when:** Turning any brain doc into a client-facing PDF, image, or video.
**How:** Strip every internal directive and pipeline reference: "read this first," "hand to content-strategist,"
"for the paid-ads-manager," "brain file," "every downstream agent reads this," gate labels, and any "STEAL THIS /
IMPROVE THIS"-style framing aimed at us. Reframe in client-facing voice, addressing the client or their audience.
The internal `.md` stays as-is for the agents; the deliverable is a separate, polished, client-ready artifact.

### ALWAYS: Screenshot every text/graphic frame to confirm it doesn't cover the subject
**Why:** a client requires that any on-screen text/label/chip never sits on the subject or important info.
A "safe corner" isn't safe on every frame when the subject moves (e.g. a rotating bust whose hair sweeps across).
**Apply when:** Any video with an overlay.
**How:** Extract and VIEW frames across the overlay's entire on-screen window; nudge/time it out if it overlaps. Dispatcher re-verifies during VERIFY.

### ALWAYS: Videos must have sound
**Why:** a client reel v3 shipped with zero audio. Instagram Reels and TikTok are sound-first platforms — a silent video is disqualified before anyone judges the visuals.
**Apply when:** Every video, no exceptions.
**How:** Music track and/or sound design (@remotion/sfx, licensed audio, or trending audio noted by trend-spotter) is a mandatory layer. A silent render is an automatic QC rejection.

---

## VIDEO RULES

### NEVER: Put text on top of images that already contain text
**Why:** Product photos from clients often have branded text baked in (headlines, taglines, labels). Adding additional text overlays creates two competing layers — neither is readable. This was the core flaw in a client reel v1.
**Apply when:** Any video using client-uploaded product photos as scenes.
**Fix:** Either (a) crop tightly to remove the embedded text area from the visible frame, or (b) use a pure-dark background for text moments and let product images be text-free.

### NEVER: Flash cuts for premium brands
**Why:** Violet overlay flash cuts between scenes look flashy and cheap. Big brands (Apple, Tesla, Nike) use smooth crossfades or clean hard cuts from black. Flash = low quality signal.
**Apply when:** All videos. Flash cuts are acceptable ONLY for high-energy content (hype reels, EDM-synced edits) — never for premium product videos.
**Fix:** Use `@remotion/transitions` with `fade()` presentation and `linearTiming`. 30-frame crossfade is the standard premium dissolve.

### NEVER: Show full product photos with multiple products when one product is the subject
**Why:** Client product photos show an entire product tableau (8-12 products on a table). Showing the full image makes every scene look cluttered and unfocused. Premium brands always show ONE product at a time — hero shots.
**Apply when:** Any video using multi-product tableau photos.
**Fix:** Use tight crops (`transform: scale(2.0-2.5)` + `transformOrigin` centered on the specific product). This isolates one product, removes the embedded text areas, and creates a professional hero shot feel.

### ALWAYS: Crop product scenes to isolate a single product
**How:** In Remotion, set `objectFit: cover` on the `<Img>` component, then apply `transform: scale(X)` + `transformOrigin: 'Y% Z%'` where Y/Z is the focal point of the specific product within the image. The scale zooms in; the transformOrigin sets the center of the zoom.
**Rule:** Scale 2.0-2.5 removes the embedded text areas (top logo + bottom labels) that typically occupy the top 15% and bottom 20% of client product photos.

### ALWAYS: Premium videos have minimal text
**Why:** Apple, Rolex, Tesla — their product videos rarely show more than one or two text moments. Text is EARNED by product silence. Too much text = lack of confidence in the product.
**Apply when:** Premium/luxury/aspirational brand videos.
**Rule:** Maximum 3 text moments per video: (1) brand signature/hook, (2) product category or insight, (3) final CTA with handle. Product scenes should be text-free.
> ⚠️ **CLIENT OVERRIDE — a client:** this minimal-text rule does **NOT** apply to a client. The
> client explicitly wants on-screen STORY text throughout the video (viral-TikTok style) to drive
> engagement. For a client, QC must NOT penalize on-screen text — see `clients/[client]/video-remarks.md`.
> A text-less "premium" a client edit is a REJECT, not a pass. (Added 2026-07-18 from client feedback.)

### NEVER: Cross-dissolve between two shots of the SAME object
**Why:** a client reel v1 crossfaded the print timelapse into the just-off-the-printer clip. Both showed the same support-covered bust at different scale/angle, so the 1s dissolve **ghosted the figure into a double exposure** — the client saw it immediately ("the image is repeating itself"). Confirmed on the frame at ~4.35s.
**Apply when:** Any cut between two shots of the same subject/product.
**Fix:** Use a **hard cut**, or a quick **dip-to-black**, between same-subject shots. Reserve cross-dissolves for genuinely different scenes. Always extract and view the frames either side of every transition before shipping — a dissolve that reads fine in motion can still ghost on the frame.

### NEVER: Stabilize footage that was shot on a tripod or stand
**Why:** a client's support-removal clip was filmed on a phone **on a stand** (already steady). v1 ran `deshake` on it anyway; the filter chased the moving hands and **added** motion — measured inter-frame movement rose 5.8 → 7.6 (~31% shakier than the source). The client noticed. Stabilizers assume global camera motion; when hands/objects fill the frame and move, the model breaks and the result warps or swims.
**Apply when:** Every clip. Ask/assume how it was shot before touching it.
**Fix:** Only stabilize genuinely handheld clips. If you do stabilize, **re-measure inter-frame motion and confirm it went DOWN** — if it went up, revert. When in doubt, leave the original motion alone. (Related: `vidstab` can also corrupt clips with no coherent camera motion into macroblocks — `deshake` is a different model, but neither is a default.)

### ALWAYS: Measure audio true peak AFTER encoding, never before
**Why:** a client v3 set its limiter from the pre-encode WAV (−1.3 dBTP, looks fine) but the encoded MP4 came back at **+0.5 dBTP** — lossy AAC added ~1.8 dB of inter-sample overshoot on dense broadband ASMR. A "clean" pre-encode measurement would have shipped a file that crackles once Instagram/TikTok re-encodes it. The limiter had to sit at 0.60, far below the naive 0.89.
**Apply when:** Every video with audio.
**Fix:** Master to **≤ −1.0 dBTP measured on the final encoded file** (`ffmpeg -af ebur128=peak=true` or `loudnorm=print_format=summary`). Iterate the limiter and re-measure the encoded output until it passes. Target ~−14 LUFS integrated.

### ALWAYS: Verify font glyph coverage before rendering non-Latin text
**Why:** a client v2's Arabic was set in a Dubai-Bold file that was **missing the isolated forms of و and ز** — so "[the product]" (the product's whole subject) rendered as "فير□□" tofu boxes. It shipped into a render before being caught. Connected forms worked, which is why an earlier phrase looked fine and masked the gap.
**Apply when:** Any video/image with Arabic, Hebrew, Persian, Urdu, CJK, or any non-Latin script.
**Fix:** Render a **test frame containing the exact strings** and visually confirm every glyph before the full render. If glyphs are missing, switch to a font with full coverage (Arial Bold, Tahoma, Segoe UI all cover Arabic). Correct spelling beats a prettier typeface — always. Also: ffmpeg `drawtext` on Windows chokes on the `C:` drive-colon in filter paths — run from the working dir with relative filenames and put text in `textfile=` files to dodge quoting issues.

### ALWAYS: Smooth pacing for premium
**Rule:** 4-5 seconds per product scene minimum. Quick cuts signal cheap content. Slow, confident dwell time signals premium quality.
**Ken Burns:** Scale 1.0→1.07 for subtle movement. For tight-crop scenes: scale X.0→X.06 (same delta, just on a larger base).

---

## IMAGE RULES

> **Full prompt-writing craft lives in `system/prompt-writing-rules.md`** (mandatory for the Visual
> Director, Content Strategist, and Video Producer when they write prompts) **plus the client's
> `clients/[name]/visual-remarks.md`.** The rules below are the ones QC enforces on the finished image.

### ALWAYS: Compose text + logo in a design pass — never let the model render them
**Why:** Image models drop and garble text and mangle logos. On the agency P01 test the same prompt
rendered the headline only 1 of 3 times, and fonts were never specified. Text and logos are a design job.
**Apply when:** Every graphic with text or a logo.
**How:** Two-step: (1) generate a clean text-free PLATE with reserved negative space; (2) composite the text
(named brand fonts, exact hex) and the REAL logo asset on top. This also satisfies the "use REAL brand
assets, never re-draw a logo" rule above. QC rejects model-rendered/garbled text or a model-drawn logo.

### ALWAYS: One product across a multi-scene set must be the SAME product (reference-first)
**Why:** Generating each slide independently gives a slightly different product each time. the agency P01.
**Apply when:** Any carousel / "N worlds" / before-after showing one product across slides.
**How:** Create/approve ONE hero reference first, build every slide from it. Product brands: the reference is
the client's real photo. Demo products: generate the hero once + a short spec, reuse it. QC checks the
product is identical across slides.

### ALWAYS: "One product / N worlds" posts must look GENUINELY different per world
**Why:** the agency P01 showed six near-identical dark scenes; the post's whole point is range, so sameness
inverts the message.
**Apply when:** Any "same product, different scenes" set.
**How:** Each world gets its own environment, dominant palette, and light. QC rejects a set where the scenes
read the same.

### NEVER: Stamp the producing agency's brand identity onto a client's product/showcase scene
**Why:** User feedback 2026-08-06. On P01 the agency's red line + palette were baked into every scene, but the
product is meant to be a CLIENT's, shown to prove range. Our brand drowned both the product and the "different
results" message.
**Apply when:** Any showcase image of a client (or demo) product.
**How:** The scene serves the PRODUCT; let each world keep its own colour story. The agency signs it only with
a SUBTLE logo tag (consistent corner) + the wrapper cover/CTA slides + caption voice + typography. Feed
consistency lives in the wrapper, not in palette-stamping the product. (Own-brand frames — covers, CTA,
educational slides — DO use full house style. See the client's visual-remarks.md for the split.) QC checks the
showcase scenes are not forced into the agency palette and that the subtle tag is present.

### ALWAYS: Check text legibility against its background before shipping any image/graphic
**Why:** the agency homepage shipped with the word "into" invisible (dark text on a dark section) and had to be caught and fixed. Low-contrast text reads as broken, not stylish.
**Apply when:** Any image, graphic, or web section with text on it.
**How:** View the actual rendered result and confirm every word is readable. Dark-on-dark and light-on-light are automatic fails. If unsure, add a scrim/shadow or change the text colour.

### PRODUCT BRANDS: the image must show the client's REAL product, never an invented one
**Why:** Core product-brand rule. AI generates the SCENE around the real product photo; it never invents the product itself. (Same rule as video.)
**Apply when:** Every image for a product brand.
**How:** Composite/base on the client's uploaded product photo. If no usable photo exists, STOP and ask, do not generate a fake version.

### ALWAYS: Correct platform dimensions + exact brand hex/fonts
**Why:** Wrong size gets cropped badly; approximated brand colours/fonts read as off-brand. The real-brand-asset rule applies to images too, never rebuild a logo/wordmark by hand.
**Apply when:** Every image.
**How:** Use the platform's native aspect ratio (IG feed 4:5, Reels/Stories 9:16, etc.), the client's exact hex codes, and the real supplied logo/font files.

---

## CAPTION / COPY RULES

### ALWAYS: Earn the first line (it is the hook)
**Why:** On a feed, the first line decides whether anyone reads the rest. A generic opener wastes the post. (House Taste: specific beats generic; earn the first 1.5 seconds.)
**Apply when:** Every caption, every platform.
**How:** Open with something specific and true (a real moment, a real detail, a sharp question), never "We are excited to announce."

### ALWAYS: One clear CTA per post; prices are opt-in, never invent a spec
**Why:** Multiple asks dilute action. Agents must never invent specs/prices (anything not in `clients/[client]/products/[product].md` is UNKNOWN and stays out). And even a KNOWN price stays out of public copy unless the client asked for it publicly, see PRODUCTION READINESS.
**Apply when:** Every caption.
**How:** One thing to do (DM, WhatsApp, save, comment). Default CTA drives contact, not a price. Only include a price if `show-prices-publicly: YES` for that product; otherwise omit it and invite people to message. Cross-check any number against the product file before it goes in.

### ALWAYS: On-slide copy is COPY too — it goes through copywriter → humanizer → QC before it is composed
**The rule:** Any words a viewer READS on a finished image or carousel slide (headlines, sub-lines, callouts,
coordinate/label text, on-slide CTAs) are client-facing copy, exactly like a caption. They must be written by the
copywriter, humanized by Agent 07, and QC'd, BEFORE they are composed onto the slide. The visual director does not
write or improvise on-slide copy and does not lift raw planning/blueprint text; it composes the approved humanized
copy it is handed. (The image PLATE PROMPT is model instructions, not copy, and does NOT need humanizing — only
the words that end up ON the slide do.)
**Why:** User caught it 2026-08-14 (the agency / the demo brand). A carousel sub-line ("So we built the brand out of the
line itself") had been parked in the planning blueprint months earlier, never went through the humanizer, and read
as broken, un-English filler. On-slide copy had been quietly treated as "not really copy." It is copy.
**Apply when:** Every image/carousel/video-overlay with words on it, every client. QC HARD-FAILS a slide whose
on-slide copy has no humanizer pass logged (same standing as caption copy).

### ALWAYS: Compose slide text/logos in Canva (the Canva MCP) and keep the editable design
**The rule:** The text + logo compositing pass is done in the Canva MCP (`generate-design` / `edit-design` /
`export-design`), and the editable Canva design is preserved for the user, not just a flat export. Canva is THE
compose tool for slide text, because it leaves the user a file he can open and tweak himself. HTML-to-image (or a
Remotion still) is EMERGENCY-ONLY: use it solely if the Canva MCP is genuinely down, and STOP and tell the user
first (never a silent downgrade).
**Why:** User rule 2026-08-14. A baked HTML-to-image PNG (how a demo carousel slide 1 was made) can't be edited by the
user; he wants an editable original so he can nudge a word or position without coming back to us. This is also our
standing "Canva = the Canva MCP, never just nice fonts" rule made the required path, not merely the default.
**Apply when:** Every slide/graphic with composited text or a logo. QC checks the build was done in Canva and that
an editable design (link/ID) exists; a flat-only PNG with no Canva original is a fail unless Canva was down and the
user was told.

### ALWAYS: Run the Canva quality-enhance pass on every image before it's ready to post
**The rule:** Any picture used in a Canva design (an uploaded AI plate, a photo, an element) gets its quality
enhanced inside Canva's photo editor (the "Enhance" tool on the image) BEFORE composing, AND the final PNG export
itself is downloaded with Canva's "enhance quality" download option turned on. Both passes, every time, no
exceptions. This is a required production step, not an optional nice-to-have.
**Why:** User test 2026-08-22 (the demo brand). The user enhanced every picture inside the Canva editor, then also
downloaded with the quality-enhance option checked, and compared that file against an un-enhanced export of the
same design. The difference was clearly visible: sharper overall image, and the agency logo noticeably crisper
and more legible. An un-enhanced export is a lower-quality deliverable even when everything else about the design
is correct.
**Apply when:** Every image/carousel slide/graphic exported from Canva, every client, no exceptions.
**How:** (1) In the Canva editor, select each photo/plate on the canvas → Edit photo → apply the quality/Enhance
tool. (2) When exporting, use Download → PNG → enable the enhance-quality option before downloading. QC checks the
final file for visible softness/logo blur consistent with a skipped enhance pass and rejects if the enhance step
looks skipped.

### (Also enforced everywhere) No em-dashes; Humanizer runs before QC; public location = country only
**Why:** Global rules, see the sections above. Listed here so caption work has them in one place.

---

## EMAIL RULES

*(To be added as real email/WhatsApp outputs are produced and reviewed. When we build the first sequence via Agent 12, load the `email-marketing-bible` skill first per `system/skill-router.md`, then codify the lessons here: subject-line/preview discipline, one CTA per email, deliverability basics, unsubscribe compliance.)*

---

## CONTENT CALENDAR / STRATEGY RULES

### ALWAYS: Sequence the calendar by what is physically producible NOW, not by ideal narrative order
**Why:** a client's first 30-day calendar (2026-07-18) put functional gadgets ("useful things you can't buy on a shelf") in Week 2 — but those products weren't designed or printed yet. You cannot shoot posts for a product that doesn't exist. The calendar looked strategically clean but was unbuildable in week order.
**Apply when:** Every content calendar, every client. Especially product brands where posts depend on physical items being made/photographed.
**How:** Before assigning any week, check the brand-profile and with the client which products actually have photos/video ready TODAY. Front-load the weeks with what's already producible; push not-yet-made products to later weeks that have real lead time to design/print/photograph them. When a "concrete launch/sales event" moves week, move its promotional weight with it — don't leave the promo beat stranded on a week whose product isn't ready.
**a client example:** Re-sequenced to Week 1 = the client's product figurine (printed, assets in hand) → Week 2 = masks → Weeks 3–4 = gadgets + NEST (still to be made).

### ALWAYS: List per-week production blockers on the calendar itself
**Why:** The dispatcher needs to know, at a glance, which weeks can start production and which are blocked — otherwise it spawns copywriter/visual-director/video-producer on rows that can't be shot.
**Apply when:** Every calendar.
**How:** At the top of content-calendar.md, mark each week ✅ producible or ⛔ blocked, and name the blocker (missing photos, product not printed, prices unset, etc.). Only ✅ weeks are eligible for production spawn.

---

## HOW TO UPDATE THIS FILE

After any piece of content is reviewed — by the user, QC agent, or after going live — add the learning here. Format:
```
### [NEVER/ALWAYS]: [Short rule]
**Why:** [What happened]
**Apply when:** [Which content types]
**Fix/How:** [Specific technical solution]
```

Do not delete old rules. Mark outdated rules with ~~strikethrough~~ and add a note if a rule changes.

---

*Last updated: 2026-08-06 — Added 4 IMAGE rules + a pointer to the new `system/prompt-writing-rules.md` and per-client `visual-remarks.md`, from the agency P01 "one product / six worlds" feedback: compose text/logo in a design pass (never model-rendered); reference-first product consistency across a set; genuine per-world variety; and never stamp the agency's own brand identity onto a client's showcase product (subtle logo tag only).*
*Prior: 2026-07-20 — Added 4 universal VIDEO rules from a client reel v1 to v3 cycle: never cross-dissolve same-object shots (ghosting); never stabilize tripod/stand footage (adds motion); always measure audio true peak AFTER encoding (AAC adds inter-sample peaks — master ≤ −1 dBTP); always verify font glyph coverage for non-Latin text with a test frame before rendering.*
