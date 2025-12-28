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
- `linkedin-content` - LinkedIn posts with 118 frameworks in 6 categories
- `hook-and-headline-writing` - Headlines (15 proven formulas)
- `dude-with-sign-writer` - Punchy one-liners

### Utilities
- `image-prompt-generator` - AI images with Gemini
- `skill-creator` - Create new skills

---

## Hub-and-Spoke Content Workflow

Content production follows a hub-and-spoke model: create one substantial hub piece, then spin off derivative spoke content.

### Hub Types and Their Spokes

| Hub Type | Primary Skill | Natural Spokes | Spoke Skills |
|----------|--------------|----------------|--------------|
| **Podcast Episode** | `podcast-production` | Blog post, 3 social clips, LinkedIn posts, newsletter segment | `podcast-blog-post-creator`, `video-caption-creation`, `linkedin-content`, `social-content-creation` |
| **Deep Dive Article** | `open-education-hub-deep-dives` | LinkedIn posts, Twitter threads, newsletter feature | `linkedin-content`, `social-content-creation` |
| **Daily Newsletter** | `opened-daily-newsletter-writer` | LinkedIn post, Twitter thread | `linkedin-content`, `social-content-creation` |

### Skill Chaining

Skills call other skills when needed. The dependency flows naturally:

```
podcast-production
├── Checkpoint 2: video-caption-creation, cold-open-creator
├── Checkpoint 3: youtube-title-creator, opened-identity
└── Checkpoint 4: transcript-polisher, podcast-blog-post-creator

social-content-creation
├── Phase 1-2: Extract concepts, match frameworks
├── Phase 3: Apply ghostwriter voice
└── LinkedIn-specific: linkedin-content (progressive disclosure)

linkedin-content
├── Match category (engagement, story, list, contrarian, authority, community)
└── Load ONE reference file, apply ghostwriter voice
```

### Session Workflow

**After completing a hub piece, proactively offer spoke content:**

1. **Podcast session ends** → "Want me to create LinkedIn posts from the key concepts? I identified 3-5 standalone ideas that would work well."

2. **Deep dive published** → "Ready to spin off social posts? The [specific insight] would make a strong contrarian LinkedIn post."

3. **Daily newsletter done** → "This 'Tool' section would translate well to a quick Twitter thread. Want me to draft it?"

**Flexibility for social-first:**
Sometimes social content has a higher creativity bar and should be developed first. If a concept is clearly social-first (punchy, visual, engagement-driven), develop the social angle before or alongside the hub piece.

### Progressive Disclosure for Skills

Skills use a three-level loading system to save context:

1. **Always loaded:** Skill name + description (~100 words)
2. **When triggered:** SKILL.md body (<5k words)
3. **As needed:** Reference files from `references/` folder

For skills with large reference libraries (linkedin-content, social-content-creation), load only the relevant category file - not all of them.

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

### Hard Rules (Never Break)

**Correlative constructions are absolutely banned:**
- Never write "X isn't just Y - it's Z" or "It's not about X, it's about Y"
- This is the #1 AI tell. Find another way to make the point.

**Dash consistency:**
- Use hyphens with spaces - like this - for parenthetical breaks
- Never use em dashes (—). They're an AI tell and we want consistency.

**No emojis** in body content (rare exceptions for social captions only).

### Soft Rules (Generally Avoid)

**AI-ism words** - generally avoid but OK sometimes:
- delve, comprehensive, crucial, vital, leverage, landscape, navigate, foster, facilitate, realm, paradigm, embark, journey, tapestry, myriad, multifaceted, seamless, cutting-edge

**AI-ism phrases** - generally avoid:
- "The best part? ..." / "The secret? ..."
- "What if I told you..." / "Here's the thing..." / "Let's be honest..."
- "In today's fast-paced..." / "In the ever-evolving world of..."
- "In conclusion" / "In summary"
- Staccato phrasing: "No fluff. No filler. Just results."

**One exception:** "Let's dive in" is OK for Charlie's daily newsletter sign-off only.

### What's Fine

- Bold for key terms, stats, and quotes
- Bullet points and lists
- Hedging when genuinely uncertain

### Handling Quotes from Sources

Edit like a smart journalist:
- Paraphrase to tighten facts or make them clearer
- Keep original wording for spicy/memorable quotes
- Never hallucinate or put words in someone's mouth they didn't say

### For Deeper Guidance

Invoke these skills when you need more:
- `ghostwriter` - comprehensive anti-AI patterns and voice techniques
- `hook-and-headline-writing` - sticky sentences, power words, headline formulas
- `opened-identity` - Sarah persona, brand voice, strategic narrative

---

## Internal Linking Strategy

When writing new content:

1. Search blog index: `grep -i "keyword" seomachine/context/blog-index.csv`
2. Target 3-5+ internal links per article
3. Use descriptive anchor text (not "click here")
4. Prioritize hub pages, related approaches, relevant podcasts
