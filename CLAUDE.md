# OpenEd Vault - Master Context

This vault is the content production system for OpenEd, an alternative education company. It contains skills, frameworks, and tools for creating newsletters, podcasts, social media, SEO content, and more.

---

## Content Publishing Schedule

| Day | Content Type | Skill to Use |
|-----|--------------|--------------|
| Monday | OpenEd Daily (Thought-Tool-Trend) | `opened-daily-newsletter-writer` |
| Tuesday | OpenEd Daily (Thought-Tool-Trend) | `opened-daily-newsletter-writer` |
| Wednesday | Deep Dive article or special feature | `open-education-hub-deep-dives` |
| Thursday | Podcast episode release + assets | `podcast-production` |
| Friday | Weekly Summary newsletter | `opened-weekly-newsletter-writer` |

**Ongoing:** Social media, tool/curriculum reviews, Day-in-the-Life posts

---

## Content Database

**Local Database:** `Content/Master Content Database/`

406 Obsidian-style markdown files with YAML frontmatter (title, url, type, date, meta_description, summary). Synced from Webflow CMS.

```
Master Content Database/
├── Announcements/      (3 files)
├── Blog Posts/         (50 files)
├── Daily Newsletters/  (286 files)
└── Podcasts/           (67 files)
```

### Sync Content Database

Run this at the start of podcast/daily/weekly sessions to pull latest content from Webflow:

```bash
cd "Content/Misc. Utilities/seomachine" && python3 -c "
from dotenv import load_dotenv
load_dotenv('data_sources/config/.env')
from data_sources.modules.webflow import sync_content_database
sync_content_database()
"
```

### Search Content

Find content by title or keyword:
```bash
grep -ril "keyword" "Content/Master Content Database/"
```

### Live URLs

| Type | URL |
|------|-----|
| Blog Articles | https://opened.co/blog?type=blog |
| Podcasts | https://opened.co/blog?type=podcast |
| Daily Newsletters | https://opened.co/blog?type=daily |

**CSV Index:** `Content/Misc. Utilities/seomachine/context/blog-index.csv`

---

## Vault Structure

```
OpenEd Vault/
├── .claude/skills/                # 22 content production skills
├── Content/
│   ├── Master Content Database/   # Synced Webflow content (Obsidian-style)
│   ├── Open Ed Podcasts/          # Podcast transcripts and assets
│   ├── OpenEd Daily/              # Newsletter drafts by date
│   ├── Open Education Hub/        # Hub pages and deep dives
│   ├── Articles/                  # Long-form content
│   └── Misc. Utilities/
│       └── seomachine/            # SEO tools and analytics
└── CLAUDE.md                      # This file
```

---

## Skills Quick Reference

### Foundational
- `opened-identity` - Brand voice, Sarah persona, strategic narrative
- `guidelines-brand` - Visual identity (colors, typography)
- `ghostwriter` - Convert source material to authentic human voice

### Newsletters
- `opened-daily-newsletter-writer` - Mon-Thu (5-checkpoint workflow)
- `opened-weekly-newsletter-writer` - Friday summary

### Long-Form Content
- `seo-content-writer` - SEO articles with live GA4/DataForSEO analytics
- `open-education-hub-deep-dives` - Hub pages with proprietary insights
- `podcast-blog-post-creator` - Podcast transcripts to blog posts
- `day-in-the-life` - Family schedule/curriculum narratives
- `verified-review` - Product reviews from real families

### Video & Podcast
- `podcast-production` - Full workflow: transcript to assets (4 checkpoints)
- `transcript-polisher` - Clean raw transcripts
- `cold-open-creator` - 25-35 second podcast cold opens
- `youtube-title-creator` - High-CTR titles (119 frameworks)
- `youtube-clip-extractor` - Download, analyze, cut clips
- `video-caption-creation` - On-screen text and captions
- `youtube-downloader` - Download YouTube transcripts

### Social Media
- `social-content-creation` - Transform content to platform posts
- `hook-and-headline-writing` - Headlines (15 proven formulas)
- `dude-with-sign-writer` - Punchy one-liners

### Utilities
- `image-prompt-generator` - AI images with Gemini
- `skill-creator` - Create new skills

---

## SEO Machine

Location: `Content/Misc. Utilities/seomachine/`

### Live Analytics Commands

**Top Performing Content:**
```bash
cd "Content/Misc. Utilities/seomachine" && python3 -c "
from dotenv import load_dotenv
load_dotenv('data_sources/config/.env')
from data_sources.modules.google_analytics import GoogleAnalytics
ga = GoogleAnalytics()
for i, p in enumerate(ga.get_top_pages(days=30, limit=10), 1):
    print(f\"{i}. {p['title'][:50]} - {p['pageviews']} views\")
"
```

**Declining Content (Refresh Candidates):**
```bash
cd "Content/Misc. Utilities/seomachine" && python3 -c "
from dotenv import load_dotenv
load_dotenv('data_sources/config/.env')
from data_sources.modules.google_analytics import GoogleAnalytics
ga = GoogleAnalytics()
for p in ga.get_declining_pages(comparison_days=30)[:5]:
    print(f\"- {p['title'][:50]}: {p['change_percent']:.0f}%\")
"
```

**Keyword Research:**
```bash
cd "Content/Misc. Utilities/seomachine" && python3 -c "
from dotenv import load_dotenv
load_dotenv('data_sources/config/.env')
from data_sources.modules.dataforseo import DataForSEO
dfs = DataForSEO()
for kw in dfs.get_keyword_ideas('YOUR KEYWORD', limit=10):
    print(f\"- {kw['keyword']}: {kw.get('search_volume', 'N/A')} vol\")
"
```

### Analysis Modules

| Module | Purpose |
|--------|---------|
| `google_analytics.py` | GA4 traffic, declining pages |
| `dataforseo.py` | Keyword research, SERP analysis |
| `keyword_analyzer.py` | Keyword density check |
| `readability_scorer.py` | Flesch-Kincaid scoring |
| `content_scrubber.py` | Remove AI watermarks |

---

## Writing Rules

These rules apply to ALL content written in this workspace.

### Dash Usage

Use regular hyphens with spaces for parenthetical breaks - like this - not em dashes.

- "Education is changing - and parents are noticing"
- NOT: "Education is changing—and parents are noticing"

### Forbidden AI-isms

**Rhetorical Flourishes:**
- "It's not just [X], it's [Y]."
- "The best part? ..." / "The secret? ..."
- "What if I told you..." / "Here's the thing..."
- "Let's be honest..." / "The truth is..."
- "At the end of the day..."

**Staccato Phrasing:**
- "No fluff. No filler. Just results."
- "Simple. Clear. Effective."

**Openers:**
- "In the ever-evolving world of..."
- "In today's fast-paced..."
- "Gone are the days when..."

**Other:**
- No corporate buzzwords
- No bullet points unless asked
- No boldface, emojis, decorative formatting
- No "In conclusion" or "In summary"
- No em dashes for dramatic effect

### Good Writing

- Concise and straightforward
- Natural cadence like a skilled human writer
- Clarity and rhythm over cleverness
- Clean, confident sentences that sound human

---

## Internal Linking Strategy

When writing new content:

1. Search blog index: `grep -i "keyword" seomachine/context/blog-index.csv`
2. Target 3-5+ internal links per article
3. Use descriptive anchor text (not "click here")
4. Prioritize hub pages, related approaches, relevant podcasts
