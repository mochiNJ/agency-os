# Client Onboarding — 13 Questions

Used by Agent 01 (Brand Strategist). Ask one question at a time. Wait for each answer before proceeding.

**Core rule:** Only ask what ONLY THE CLIENT can know. Never ask about competitors, audience platforms, audience psychology, or market data. The agency's agents research all of that. The client's job is to describe THEIR business.

---

## SECTION 1: THE BUSINESS

**Q1.** What is your business name, and in one sentence, what do you sell?

**Q2.** What are your top 3 products or services you want us to promote?
For each: name and what it does. (Price is optional and only for our records. It is never required to start work.)

**Q2b.** Do you want prices shown publicly in your posts, or would you rather your content drive people to comment, message, or contact you?
By default we do NOT put prices in public content. Sharing a price publicly is your choice, and can be decided per product. A missing price never delays anything.

**Q3.** What makes you different from others selling something similar?
What is your single biggest advantage?

**Q4.** Have you worked with a marketing agency before?
If yes — what worked? What did not?

---

## SECTION 2: THE BRAND

**Q5.** Describe your brand in 3 words.
How do you want people to feel when they see your content?

**Q6.** What tone should your content have?
Choose: Professional / Casual / Bold / Inspirational / Humorous / Luxury / Friendly / Educational / Edgy

**Q7.** What should your content NEVER include?
Topics, styles, words, or visuals that are completely off-limits.

**Q8.** Do you have a brand visual identity you'd like us to use? This is entirely your choice.
- Brand colors (hex codes if you have them, e.g. #FF5733, or just describe them)
- Specific fonts you want used
If you give us these and want them used, we will use them exactly. If you'd rather give us creative freedom, that is completely fine, we will design a look that fits your brand.

---

## SECTION 3: ASSETS

**Q9.** If you have a logo you'd like on your content, upload it (PNG or SVG preferred). Optional.
If you provide it, we use the real file exactly, never a hand-made recreation. If you'd rather we keep posts logo-light or design freely, that is fine too.
`[FILE UPLOAD]`

**Q10.** Do you sell physical products people can hold, wear, use, or consume?
Examples: skincare, jewelry, clothing, food, candles, accessories.
YES or NO.

> **IF YES:** Upload product photos now. Required — we cannot create accurate content without real photos of your products. Phone photos are fine.
> `[MULTI-FILE UPLOAD — JPG, PNG, HEIC]`

> **IF NO:** Upload brand photos, team photos, location photos, or past content.
> `[MULTI-FILE UPLOAD]`

**Q11.** Share up to 3 examples of content you love — your brand or any other.
Links or file uploads. For each: why do you love it?
`[LINK FIELDS x3 + FILE UPLOAD]`

---

## SECTION 4: GOALS

**Q12.** Rank these platforms by importance to you:
Instagram / TikTok / LinkedIn / Facebook / X (Twitter)

**Q13.** What is your #1 goal for the next 90 days?
More Sales / Brand Awareness / Grow Followers / Generate Leads / Build Authority

And: any product launches, promotions, or events in the next 90 days?

---

## After Collecting All Answers

1. Determine client type: **PRODUCT BRAND** (physical items) or **SERVICE BRAND** (no physical product) — see `system/client-types.md`
2. Save: `clients/[name]/brand-profile.md` using `templates/brand-profile-template.md`
   - Include: `client-type` (PRODUCT/SERVICE), `product-photos-uploaded` (YES/NO + count)
   - `show-prices-publicly`: NO (default) | YES (per product, only if the client asked)
   - `brand-identity-provided`: logo YES/NO · fonts YES/NO · colors YES/NO · use-them YES/NO
     (if YES, the real logo file + exact hex + exact fonts are mandatory in every visual; if NO, agents have creative freedom)
3. Log the new client in: `system/active-clients.md`
4. Trigger simultaneously: `competitor-researcher` + `trend-spotter` + `seo-aeo-agent`
