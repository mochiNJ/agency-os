---
name: analytics-tracking
description: "When the user wants to set up, improve, or audit analytics tracking and measurement. Also use when the user mentions 'set up tracking,' 'GA4,' 'Google Analytics,' 'conversion tracking,' 'event tracking,' 'UTM parameters,' 'tag manager,' 'GTM,' 'analytics implementation,' 'tracking plan,' 'how do I measure this,' 'track conversions,' or 'analytics isn't working.' Best used at Month 3+ when a website exists."
metadata:
  version: 1.1.0
---

# Analytics Tracking

You are an expert in analytics implementation and measurement. Your goal is to help set up tracking that provides actionable insights for marketing and product decisions.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions.

Before implementing tracking, understand:

1. **Business Context** — What decisions will this data inform? What are key conversions?
2. **Current State** — What tracking exists? What tools are in use?
3. **Technical Context** — What's the tech stack? Any privacy/compliance requirements?

---

## Core Principles

### 1. Track for Decisions, Not Data
- Every event should inform a decision
- Avoid vanity metrics
- Quality > quantity of events

### 2. Start with the Questions
- What do you need to know?
- What actions will you take based on this data?
- Work backwards to what you need to track

### 3. Name Things Consistently
- Naming conventions matter
- Establish patterns before implementing
- Document everything

### 4. Maintain Data Quality
- Validate implementation
- Monitor for issues
- Clean data > more data

---

## Tracking Plan Framework

### Structure

```
Event Name | Category | Properties | Trigger | Notes
```

### Event Types

| Type | Examples |
|------|----------|
| Pageviews | Automatic, enhanced with metadata |
| User Actions | Button clicks, form submissions |
| System Events | Signup completed, purchase |
| Custom Conversions | Goal completions, funnel stages |

---

## Event Naming Conventions

### Recommended Format: Object-Action

```
signup_completed
button_clicked
form_submitted
purchase_completed
```

### Best Practices
- Lowercase with underscores
- Be specific: `cta_hero_clicked` vs. `button_clicked`
- Include context in properties, not event name
- Avoid spaces and special characters
- Document decisions

---

## Essential Events

### Marketing Site

| Event | Properties |
|-------|------------|
| cta_clicked | button_text, location |
| form_submitted | form_type |
| contact_requested | — |
| whatsapp_clicked | page_location |

### E-Commerce / Orders

| Event | Properties |
|-------|------------|
| product_viewed | product_name, category |
| order_started | — |
| order_completed | total_value, product_list |
| inquiry_submitted | product_interest |

---

## GA4 Implementation

### Quick Setup

1. Create GA4 property and data stream
2. Install gtag.js or Google Tag Manager
3. Enable enhanced measurement
4. Configure custom events
5. Mark conversions in Admin

### Custom Event Example

```javascript
gtag('event', 'whatsapp_clicked', {
  'page_location': 'homepage_hero',
  'product_interest': 'custom_gifts'
});
```

---

## Google Tag Manager

### Container Structure

| Component | Purpose |
|-----------|---------|
| Tags | Code that executes (GA4, pixels) |
| Triggers | When tags fire (page view, click) |
| Variables | Dynamic values (click text, data layer) |

### Data Layer Pattern

```javascript
dataLayer.push({
  'event': 'form_submitted',
  'form_name': 'contact',
  'form_location': 'contact_page'
});
```

---

## UTM Parameter Strategy

Use UTM parameters to track where your customers come from:

### Standard Parameters

| Parameter | Purpose | Example |
|-----------|---------|---------|
| utm_source | Traffic source | instagram, whatsapp, tiktok |
| utm_medium | Marketing medium | social, direct, referral |
| utm_campaign | Campaign name | launch_week, eid_gifts |
| utm_content | Differentiate versions | bio_link, story_swipe |

### Example UTM URLs

```
yoursite.com/?utm_source=instagram&utm_medium=social&utm_campaign=launch_week
yoursite.com/?utm_source=whatsapp&utm_medium=direct&utm_campaign=eid_2026
```

### Naming Conventions
- Lowercase everything
- Use underscores or hyphens consistently
- Document all UTMs in a spreadsheet

---

## Debugging and Validation

### Testing Tools

| Tool | Use For |
|------|---------|
| GA4 DebugView | Real-time event monitoring |
| GTM Preview Mode | Test triggers before publish |
| Browser Extensions | Tag Assistant, dataLayer Inspector |

### Validation Checklist

- [ ] Events firing on correct triggers
- [ ] Property values populating correctly
- [ ] No duplicate events
- [ ] Works across browsers and mobile
- [ ] Conversions recorded correctly

---

## Privacy and Compliance

### Considerations
- Cookie consent may be required in your region
- No personal information (PII) in analytics properties
- Data retention settings
- User deletion capabilities

---

## Output Format

### Tracking Plan Document

```markdown
# [Site] Tracking Plan

## Tools: GA4, GTM

## Key Events

| Event Name | Description | Properties | Trigger |
|------------|-------------|------------|---------|
| contact_requested | User submits contact form | form_type | Form success page |
| whatsapp_clicked | User clicks WhatsApp button | page_location | Button click |

## Conversions

| Conversion | Event | Goal |
|------------|-------|------|
| Contact | contact_requested | Lead capture |
| WhatsApp | whatsapp_clicked | Direct inquiry |
```

---

## Task-Specific Questions

1. What tools are you using (GA4, Mixpanel, etc.)?
2. What key actions do you want to track?
3. What decisions will this data inform?
4. Who implements — dev team or marketing?
5. What's already tracked?

---

## Related Skills

- **seo-audit**: For organic traffic analysis
- **page-cro**: For conversion optimization (uses this data)
- **site-architecture**: For planning trackable page structure
