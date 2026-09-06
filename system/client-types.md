# Client Types: Product Brand vs Service Brand

Every client is classified at onboarding. This classification controls how the Visual Director and Video Producer operate.

---

## How to Classify

Ask Q10 during onboarding:

> "Do you sell physical products people can hold, wear, use, or consume?
> Examples: skincare, jewelry, clothing, food, candles, accessories."

- **YES** → PRODUCT BRAND
- **NO** → SERVICE BRAND

Save the classification in `brand-profile.md` as:
```
client-type: PRODUCT
product-photos-uploaded: YES (12 files)
```

---

## PRODUCT BRAND

The client sells physical items. Real product photos are **required** — you cannot create accurate content without them.

**Visual Director rules:**
- Client's real product MUST appear in every product image
- Never invent or generate a fake version of the product
- AI generates the SCENE and CONTEXT around the real product

**Workflow:**
1. Load product photo from `products/[product]/source-photos/`
2. Isolate the product (clean background)
3. Place real product in AI-generated lifestyle scene
4. Scene matches brand colors, aesthetic, audience, tone

**Examples by product type:**
- Skincare → real bottle on marble shelf with soft morning light
- Jewelry → real necklace on textured fabric or model, brand palette
- Clothing → real garment on AI-generated model, styled environment
- Food → real packaging in kitchen or lifestyle scene
- Candle → real candle in cozy interior scene

**Prompt formula:**
```
[Client's actual product described accurately] placed in [lifestyle scene],
[brand colors hex], [audience aesthetic], [platform format],
professional product photography, photorealistic, brand-consistent lighting,
product details and logo preserved
```

**Preferred tools:** Claid.ai MCP (preserves logos/shapes) → Higgsfield MCP → mcp-image/Gemini

---

## SERVICE BRAND

The client sells services, expertise, or digital products — nothing physical.

**Visual Director rules:**
- Generate all visuals from scratch
- Focus on scenes representing the service outcome or result
- Show the transformation, environment, or emotion — not a product

**Examples by service type:**
- Coaching/consulting → professional person, confident body language, clean environment
- Software/SaaS → UI mockups, people at screens, abstract tech visuals
- Fitness → transformation shots, training environments, motion
- Real estate → property exteriors/interiors, lifestyle of the area
- Finance → clean modern office, charts, confident professional settings

**Prompt formula:**
```
[Scene representing the service or result], [brand tone],
[color palette hex], [platform format], [audience demographic feel],
professional commercial photography, photorealistic, brand-consistent
```

**Tools:** All tools available — no product photo dependency.

---

## Why This Matters

**For product brands:** If the Visual Director generates an invented product instead of using the real one, the QC will reject it immediately. The client's product has specific logos, colors, shapes, and packaging that cannot be guessed. Real photos must be uploaded at onboarding.

**For service brands:** There is no physical product to anchor visuals to, so full creative generation is appropriate and expected.
