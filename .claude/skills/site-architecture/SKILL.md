---
name: site-architecture
description: "When the user wants to plan a website structure, design page hierarchies, create navigation systems, plan URL patterns, or design internal linking. Also use when the user mentions 'site structure,' 'website architecture,' 'page hierarchy,' 'navigation design,' 'URL structure,' 'sitemap,' 'what pages do I need,' 'website pages,' 'site map,' or 'how should I organize my website.' Use this when planning a website from scratch or restructuring an existing one. Best used at Month 3+ for this project."
metadata:
  version: 1.0.0
---

# Site Architecture

You are an information architecture expert focused on planning website structure, page hierarchy, navigation, URL patterns, and internal linking for optimal user experience and SEO performance.

## Before Planning

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions.

Gather this context (ask if not provided):

1. **Business context** — Company purpose, primary audiences, top 3 site goals
2. **Current state** — New site or restructuring? What exists now?
3. **Site type** — Business/service, e-commerce, content, portfolio
4. **Content inventory** — What pages/content do you have or plan to have?

---

## Core Design Principles

### The 3-Click Rule
Users should reach any important page within 3 clicks from the homepage.

### Hierarchy Depth
- **Flat (2 levels)** — Homepage → Pages: simple sites with few pages
- **Moderate (3 levels)** — Homepage → Sections → Pages: most business sites
- **Deep (4+ levels)** — Homepage → Categories → Subcategories → Pages: large e-commerce or content sites

### Navigation Design
- **Header nav**: 4-7 items maximum
- **CTA button**: Position rightmost in header
- **Footer**: Group links into logical columns (Products, About, Contact)
- **Breadcrumbs**: Mirror your URL hierarchy

---

## Site Type Templates

### Small Business / Service Site (Best for 3D LAB)

**Typical structure:**
```
Homepage (/)
├── Products (/products)
│   ├── Custom Gifts (/products/gifts)
│   ├── Home Decor (/products/home-decor)
│   ├── Replacement Parts (/products/replacement-parts)
│   └── Custom Orders (/products/custom)
├── How It Works (/how-it-works)
├── Gallery (/gallery)
├── About (/about)
└── Contact (/contact)
```

**Navigation:** Home | Products | Gallery | How It Works | Contact Us (button)

### E-Commerce Site

```
Homepage (/)
├── Shop (/shop)
│   ├── Category 1 (/shop/category-1)
│   └── Category 2 (/shop/category-2)
├── About (/about)
├── FAQ (/faq)
└── Contact (/contact)
```

---

## URL Structure

### Principles
- Use hyphens not underscores: `/custom-gifts` not `/custom_gifts`
- Lowercase everything: `/products` not `/Products`
- Keep URLs short and descriptive
- Reflect hierarchy: `/products/gifts` not `/gifts-products`

### URL Patterns by Page Type

| Page Type | URL Pattern |
|-----------|-------------|
| Homepage | `/` |
| Main section | `/products` |
| Subsection | `/products/gifts` |
| Blog post | `/blog/post-title` |
| About | `/about` |
| Contact | `/contact` |

### Common Mistakes
- Date-based blog URLs (`/blog/2024/01/post`) — hard to maintain
- IDs in URLs (`/page?id=123`) — not human-readable
- Changing URLs without 301 redirects — destroys backlink equity

---

## Navigation Design

### Header Navigation
- 4-7 items maximum
- Most important page first
- CTA (contact/order) as button, rightmost
- Avoid dropdown menus with 20+ items

### Footer Navigation
Group into 2-4 columns:
- **Products** — list main product categories
- **Company** — About, How It Works, Gallery
- **Connect** — Contact, Instagram, WhatsApp

### Breadcrumbs
Show the user's location in the site hierarchy:
```
Home > Products > Custom Gifts
```

---

## Internal Linking Strategy

### Link Types

| Type | Purpose |
|------|---------|
| **Navigational** | Header and footer links |
| **Contextual** | Links within page content to related pages |
| **Hub-and-spoke** | Pillar page links to supporting pages and back |
| **Cross-section** | Links between different content areas |

### Best Practices

- No orphan pages — every page needs at least one inbound internal link
- Use descriptive anchor text, not "click here" or "learn more"
- Link important pages more frequently throughout the site
- Implement hub-and-spoke for product categories

---

## Deliverables

When planning site architecture, provide:

### 1. Page Hierarchy
ASCII tree showing full page structure with URLs

### 2. Visual Sitemap
Mermaid diagram or table showing relationships and navigation zones

### 3. URL Map

| Page | URL | Parent | Description |
|------|-----|--------|-------------|
| Homepage | / | — | Main landing page |
| Products | /products | / | Product overview |

### 4. Navigation Spec
- Header: [items listed]
- Footer: [columns listed]
- Breadcrumbs: [yes/no, pattern]

### 5. Internal Linking Plan
- Hub pages: [list]
- Key cross-links: [list]
- Pages needing more inbound links: [list]

---

## Task-Specific Questions

1. What's the primary goal of the website? (leads, orders, information)
2. Who are the main audiences and what do they want to do?
3. How many pages do you expect to have?
4. Do you have existing content to organize?
5. What's your CMS or platform? (WordPress, Squarespace, custom)

---

## Related Skills

- **content-strategy**: For planning what content to create
- **seo-audit**: For technical SEO once site is live
- **page-cro**: For optimizing individual pages after site is built
- **copywriting**: For writing page content
