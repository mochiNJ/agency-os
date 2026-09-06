# 🧩 `templates/` — reusable starting points

**Charter: a blank form to copy and fill in. Never a filled-in instance.**
A filled-in copy belongs to the client it describes.

| template | used when | filled copy lands in |
|---|---|---|
| `brand-profile-template.md` | onboarding G1 | `clients/[c]/brand-profile.md` |
| `content-calendar-template.md` | onboarding G5 | `clients/[c]/content-calendar.md` |
| `creative-decisions-log-template.md` | onboarding G0 | `clients/[c]/creative-decisions-log.md` |
| `product-info-template.md` | the moment a product is mentioned | `clients/[c]/products/[p]/product.md` |
| `moodboard-template.md` | a new business type appears | `inspiration-library/recipes/README.md` |
| `job-ticket-template.md` | every production task | `system/jobs/YYYY-MM-DD-[client]-[task].md` |
| `campaign-brief-template.md` | a real campaign | `clients/[c]/campaigns/[name]/` |
| `influencer-brief-template.md` | influencer outreach | `clients/[c]/reports/` |
| `visual-identity-template.md` | a new brand identity | `clients/[c]/brand/` |
| `demo-product-identity-kit.md` | a new the agency demo house | `clients/[client]/products/[house]/` |
| `client-folder-structure.md` | **a pointer only.** Never build a client by hand: `python system/structure-check.py --new-client NAME` |

**Templates must never teach a dead path.** Five of them taught `uploads/`, `content/approved/` and
`demo-products/` until 2026-09-06. A template is the first thing a new client copies, so a stale one
reproduces the old mess forever.
