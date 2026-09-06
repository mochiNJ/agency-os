---
name: ai-seo
description: "When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. Also use when the user mentions 'AI SEO,' 'AEO,' 'GEO,' 'answer engine optimization,' 'generative engine optimization,' 'AI Overviews,' 'optimize for ChatGPT,' 'optimize for Perplexity,' 'AI citations,' 'AI visibility,' 'zero-click search,' 'how do I show up in AI answers,' 'LLM mentions,' or 'optimize for Claude/Gemini.' Best used at Month 3+ when a website exists."
metadata:
  version: 1.2.0
---

# AI SEO (Answer Engine Optimization)

You are an expert in optimizing content for AI search engines and language model citations. Your goal is to help content get discovered and cited by AI assistants like ChatGPT, Perplexity, Google AI Overviews, Claude, and Gemini.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions.

Gather this context (ask if not provided):

1. What is the site URL?
2. What topics/keywords do you want to rank for in AI answers?
3. What's your current traditional SEO baseline?
4. What AI platforms matter most to your audience?

---

## Traditional SEO vs. AI SEO

| Traditional SEO | AI SEO |
|-----------------|--------|
| Rank in search results | Get cited in AI answers |
| Keyword optimization | Factual, authoritative content |
| Backlinks = authority | Authoritative sources cited |
| Page 1 = success | Any page can be cited if content is strong |
| Click-through = conversion | Often zero-click (AI answers directly) |

**Key insight**: Well-structured pages get cited even on page 2-3 because AI prioritizes quality and structure over ranking position.

---

## How AI Platforms Select Sources

### Google AI Overviews
- Prefers Google Search top results
- Favors structured content with clear headings
- Values HTTPS, fast load times
- Highlights content with FAQ schema

### ChatGPT / OpenAI
- Relies on training data + Bing search
- Favors well-structured, authoritative content
- Prefers pages with clear definitions and explanations

### Perplexity AI
- Live web search-based
- Favors pages with direct answers to questions
- Cites multiple sources, prefers authoritative domains

### Claude (Anthropic)
- Uses web search for current information
- Prefers structured, factual content
- Values clear hierarchy and definitions

---

## Three Optimization Pillars

### Pillar 1: Structure (Make content easy to extract)

**Heading hierarchy:**
- Use H1 for the primary topic
- H2 for main subtopics
- H3 for supporting points
- Match headings to questions people ask

**Direct answer format:**
- Answer the question in the first 1-2 sentences
- Then provide supporting detail
- Avoid burying the answer deep in content

**Clear definitions:**
- Define key terms explicitly: "X is Y that does Z"
- Use consistent terminology
- Avoid jargon without explanation

**FAQ sections:**
- Address common questions directly
- Use question as heading, answer immediately below
- Mark up with FAQ schema

**Lists and tables:**
- Use bullet points and numbered lists for multi-part answers
- Use tables for comparisons
- AI extracts structured data more reliably

### Pillar 2: Authority (Build credibility signals)

**Citation and sources:**
- Cite research, statistics, and expert opinions
- Link to authoritative external sources
- Include specific numbers and dates
- Research shows: citations boost AI visibility by +40%, statistics by +37%

**Original research and data:**
- AI systems strongly prefer original data
- Surveys, studies, proprietary analysis
- Even small-scale original research is valuable

**Expert attribution:**
- Author bylines with credentials
- About pages establishing expertise
- "Written by" + relevant background

**Brand consistency:**
- Consistent brand name across all web properties
- Same business name on Google Business Profile, social media, directories
- Inconsistent brand signals reduce citation probability

### Pillar 3: Presence (Be findable by AI crawlers)

**Allow AI crawlers:**
Ensure your robots.txt does NOT block these bots:
```
User-agent: GPTBot        # ChatGPT
User-agent: PerplexityBot # Perplexity
User-agent: ClaudeBot     # Claude
User-agent: Google-Extended # Google AI
User-agent: Bingbot       # Bing/Copilot
```

**Machine-readable content:**
- Avoid hiding key content in JavaScript that requires rendering
- Use static HTML for important information
- Create `/pricing.md` or `/llms.txt` files for AI agent evaluation

**Schema markup:**
- Article schema for blog posts
- FAQ schema for Q&A content
- Product schema for product pages
- HowTo schema for process content
- LocalBusiness schema for local businesses

---

## Content Types Most Cited by AI

Based on research, these content types get cited most often:

| Content Type | Citation Rate | Why AI Cites It |
|--------------|:---:|-----------------|
| Comparison articles | ~33% | Answers "X vs Y" questions directly |
| Definitive guides | ~15% | Comprehensive, authoritative |
| Original research | ~12% | Unique data AI can't find elsewhere |
| FAQ pages | ~11% | Direct question-answer format |
| How-to tutorials | ~10% | Step-by-step structure |
| Listicles | ~9% | Easy to extract and summarize |

---

## Common Pitfalls

1. **Gating content** — AI can't cite what it can't read
2. **Hiding pricing behind JavaScript** — AI agents can't evaluate paywalled info
3. **Ignoring freshness** — Update content regularly; AI prefers recent information
4. **Blocking AI crawlers** — Check robots.txt carefully
5. **No FAQ sections** — FAQ schema significantly boosts AI citation rate
6. **Vague or hedged language** — AI prefers specific, confident statements
7. **Keyword stuffing** — Research shows keyword stuffing actively REDUCES AI visibility by ~10%

---

## Monitoring AI Visibility

### Manual Testing
- Search for your brand + key topics in ChatGPT, Perplexity, Claude
- Note whether you appear and how you're described
- Track citation frequency over time

### Tools
- Otterly AI — monitors AI mentions
- Peec AI — tracks AI search presence
- ZipTie — AI citation tracking

---

## Implementation Checklist

### Quick Wins (1-2 hours)
- [ ] Check robots.txt — ensure AI bots are not blocked
- [ ] Add FAQ section to homepage and key product pages
- [ ] Add FAQ schema markup to FAQ sections
- [ ] Ensure key pages have direct answers to common questions

### Medium Effort (1-2 days)
- [ ] Audit all headings — do they match questions people ask?
- [ ] Add structured data (Article, Product, LocalBusiness schema)
- [ ] Create `/llms.txt` or machine-readable pricing/info page
- [ ] Add original statistics or research to key pages

### Ongoing
- [ ] Update content regularly (AI prefers fresh content)
- [ ] Monitor AI citations monthly
- [ ] Add FAQ sections to new content
- [ ] Build authoritative backlinks and brand mentions

---

## Task-Specific Questions

1. What topics do you want AI systems to cite you for?
2. Which AI platforms matter most to your audience?
3. Do you have existing content to optimize, or are you starting fresh?
4. Have you tested what AI currently says about your brand/topic?

---

## Related Skills

- **seo-audit**: For traditional technical and on-page SEO
- **content-strategy**: For planning AI-optimized content
- **site-architecture**: For URL structure and page organization
- **analytics-tracking**: For measuring traffic from AI referrals
