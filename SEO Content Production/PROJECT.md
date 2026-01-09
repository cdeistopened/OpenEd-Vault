---
name: SEO Content Production
description: Consolidated SEO content strategy - articles, grade guides, tools directory, guest contributors
status: active
parent: OpenEd Vault
created: 2026-01-07
updated: 2026-01-08
last_session: "Created State Pages + Versus templates, connected Slack/Notion APIs, archived meeting notes"
---

# SEO Content Production

**Purpose:** Centralized hub for all SEO-driven content production at OpenEd.

**Q1 2026 Target:** 60+ SEO articles across all sub-projects

---

## Overview

This folder consolidates related SEO content initiatives that share:
- Similar workflows (research → draft → optimize → publish)
- Same distribution channel (Webflow blog, Open Education Hub)
- Shared tooling (DataForSEO, SEO skills)
- Related goals (organic traffic growth)

---

## Sub-Projects

### 1. Grade Level Guides
**Status:** Planning
**Target:** 8 guides (K, 1st-5th, Middle School, High School)

"OpenEd Recommended" curriculum stacks by grade. A parent lands on the K guide, sees exactly what to use for Math, Reading, Science, History.

**Location:** `Grade Level Guides/PROJECT.md`

---

### 2. Tools Directory
**Status:** Planning
**Target:** 20+ tool reviews

Parent-reviewed curriculum/tool database. Real voices, real opinions—not ChatGPT aggregation.

**Process:** Ella interviews parents → Extract 5+ reviews per interview → Publish with named author bylines.

**Location:** `Tools Directory/PROJECT.md`

---

### 3. Guest Contributors (Nearbound)
**Status:** Active
**Target:** 20 pitches → 5+ published pieces

Leverage trusted voices to publish on OpenEd. Draft first (Charlie Ghostwriter Method), then pitch.

**Location:** `Guest Contributors/PROJECT.md`

---

### 4. Article Factory
**Status:** Not yet started
**Target:** 40+ standalone SEO articles

Keyword-driven articles targeting high-intent searches (homeschool curriculum, how to start homeschooling, etc.)

**Location:** `Articles/` (to be created)

---

### 5. State Pages (Q1 Priority)
**Status:** Active
**Target:** 9 state guides (one per operating state)

"Homeschool Programs in [State]" guides. Legal requirements, funding options, local resources, OpenEd positioning.

**OpenEd Operating States (9 total):**
- Q1: Oregon, Nevada, Indiana, Utah
- Q2: Kansas, Arkansas, Iowa, Minnesota
- Q3: Montana

**Note:** Only create pages for states where we operate. See `State Pages/PROJECT.md` for full details.

**Location:** `State Pages/`

---

### 6. Versus Comparisons (January Priority)
**Status:** Planning
**Target:** 10 comparison articles

Head-to-head comparisons of popular curriculum and programs. High commercial intent.

**Examples:**
- Outschool vs OpenEd
- Khan Academy vs IXL
- Sonlight vs My Father's World

**Location:** `Versus/` (to be created)

---

## Content Calendar

### December 2025 (Current Sprint)
| Week | Content Type | Topic |
|------|--------------|-------|
| Week 1 | Grade Guide | Kindergarten Curriculum |
| Week 2 | Grade Guide | 1st-2nd Grade Curriculum |
| Week 3 | State Page | Oregon Homeschool Guide |
| Week 4 | Tool Review | Template Reformat (remove pricing, add screenshots) |

### January 2026
| Week | Content Type | Topic |
|------|--------------|-------|
| Week 1 | Versus | Outschool vs OpenEd |
| Week 2 | State Page | Nevada Homeschool Guide |
| Week 3 | Specialty | Military Families Homeschool Guide |
| Week 4 | Specialty | ADHD Homeschool Guide |

### Q1 2026 Priorities (from SEO Bi-Weekly)
1. **State pages** - Oregon, Nevada, Indiana first
2. **Tool reviews** - New template with author bylines, screenshots, no pricing
3. **Grade level guides** - Complete K-12 series
4. **Versus comparisons** - Start in January
5. **Specialty families** - Military, ADHD, traveling families

---

## File Structure

```
SEO Content Production/
├── PROJECT.md                  ← You are here (master overview)
│
├── Grade Level Guides/         ← K-12 curriculum recommendation guides
│   └── PROJECT.md
│
├── Tools Directory/            ← Parent-reviewed curriculum tools
│   └── PROJECT.md
│
├── Guest Contributors/         ← Nearbound author pipeline
│   └── PROJECT.md
│
├── Articles/                   ← Standalone SEO articles (future)
│   └── [article drafts]
│
└── _archive/                   ← Old credentials, deprecated work
```

---

## Shared Resources

### Skills to Chain
- `seo-content-writer` - SEO optimization
- `ghostwriter` - Voice adaptation, anti-AI patterns
- `hook-and-headline-writing` - Titles
- `verified-review` - Review format (Tools Directory)

### Data Sources
- **DataForSEO:** Keyword research (API configured)
- **GA4:** Performance tracking (Property 451203520)
- **GSC:** Search Console data (pending access)

### Credentials
Archived credentials: `Archived Large Files/seo-article-factory-credentials/`

---

## Content Philosophy (NON-NEGOTIABLE)

Every piece of SEO content must do TWO things:

### 1. Leverage Our Unfair Advantage

We have something competitors don't: **real teacher conversations happening daily in Slack.** Our content should be soaked in genuine first-hand experience.

**Wrong approach:**
> "Saxon Math uses a spiral approach where concepts are reviewed repeatedly."

**Right approach:**
> "I am a big fan of Saxon because it is such a solid curriculum," says one OpenEd mentor teacher, "but to some students, it is dry." For kinesthetic learners, she recommends Math-U-See instead.

**Weave quotes throughout** - not in a single "What Teachers Say" section at the end.

### 2. Position OpenEd as the Trusted Authority

Every page should subtly reinforce: *OpenEd is how smart families access these resources.*

- We're not a random blog aggregating reviews
- We work with 125,000+ families and have seen what actually works
- Many of these tools are FREE in our marketplace

**Don't be salesy.** Be the knowledgeable friend who happens to have a solution.

### Writing Principles

| Don't | Do |
|-------|-----|
| Walls of text | Tables, callouts, scannable structure |
| Generic descriptions | Specific examples from real families |
| "Both are great options!" | Clear, opinionated recommendations |
| Separate "What Teachers Say" section | Quotes woven throughout |
| Fluffy transition sentences | Get to the point |
| "In this article, we will..." | Just say it |

### The Test

Before publishing, ask:
1. Could this appear on any generic homeschool blog? → Rewrite
2. Is there real teacher/parent voice in every section? → Add quotes
3. Does it position OpenEd as the trusted guide? → Strengthen
4. Can I cut 30% without losing meaning? → Cut it

---

## Workflow

### For All Sub-Projects:
1. **Research:** Use DataForSEO or SEO skill for keyword targeting
2. **Mine Slack:** Pull real teacher quotes for the topic
3. **Draft:** Write using appropriate skill (ghostwriter, seo-content-writer)
4. **Apply Philosophy:** Check against principles above
5. **Optimize:** Apply on-page SEO, internal links
6. **Publish:** Push to Webflow via sync script
7. **Track:** Monitor in GA4/GSC

---

## Metrics

| Sub-Project | Target | Current | Status |
|-------------|--------|---------|--------|
| Grade Level Guides | 8 | 0 | Planning |
| Tools Directory | 20 | 0 | Planning |
| Guest Contributors | 5 | 0 | Active |
| Article Factory | 40 | 0 | Not started |
| State Pages | 9 | 0 | Active |
| Versus Comparisons | 10 | 0 | Planning |
| **Total** | **92** | **0** | |

---

## Dependencies

- [ ] Andrea sign-off on Grade Level Guide recommendations
- [ ] Ella interview pipeline for Tools Directory
- [ ] GSC access for quick wins data
- [ ] Guest contributor outreach (Matt Boudreau first)

---

## Next Steps

1. **Grade Level Guides:** Get Andrea's curriculum recommendations
2. **Tools Directory:** Send interview template to Ella
3. **Guest Contributors:** Draft pitch for Matt Boudreau
4. **Article Factory:** Identify first 10 keyword targets

---

*Created: 2026-01-07*
