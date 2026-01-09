# OpenEd Vault - Master Context

**Content production system for OpenEd** - Alternative education company creating newsletters, podcasts, social media, SEO content, and educational resources.

**Operating States:** AR, IN, IA, KS, MN, MT, NV, OR, UT (9 states)
**Program Details:** `.claude/references/opened-program-details.md`

---

## Where Things Live

| Need | Go To |
|------|-------|
| **Daily/Weekly newsletter** | `Studio/OpenEd Daily/` + skill: `opened-daily-newsletter-writer` |
| **SEO content** | `Studio/SEO Content Production/PROJECT.md` |
| **Podcast workflow** | `Studio/Open Ed Podcasts/` + skill: `podcast-production` |
| **Social posts** | skill: `social-content-creation` or `linkedin-content` + `.claude/references/social-media-strategy.md` |
| **Meta ads** | `Studio/Meta Ads/PROJECT.md` |
| **Published content** | `Content/Master Content Database/` (406 files) |
| **Content index** | `Master_Content_Index.md` (tags, tools, summaries) |
| **Current state** | `NOW.md` |
| **All skills** | `.claude/skills/` (24 total) |
| **References** | `.claude/references/` (SEO commands, KPIs, etc.) |

---

## Studio Projects

Each project has a `PROJECT.md` with full context. Navigate there first.

| Project | Location | Status |
|---------|----------|--------|
| **Eddie Awards** | `Studio/Eddie Awards/PROJECT.md` | Active |
| **Meta Ads** | `Studio/Meta Ads/PROJECT.md` | Active |
| **SEO Content Production** | `Studio/SEO Content Production/PROJECT.md` | Active |
| **Lead Magnet** | `Studio/Lead Magnet Project/` | Active |
| **Retargeting Strategy** | `Studio/Retargeting Strategy FY26-27/PROJECT.md` | Planning |
| **KPI Discussions** | `Studio/KPI Discussions/PROJECT.md` | Active |

### Ongoing Workflows (no end state)

| Workflow | Location | Cadence |
|----------|----------|---------|
| **OpenEd Daily** | `Studio/OpenEd Daily/` | Mon-Thu |
| **Podcasts** | `Studio/Open Ed Podcasts/` | Weekly |
| **Open Education Hub** | `Studio/Open Education Hub/` | As needed |

---

## Writing Rules

**CRITICAL: Apply to ALL public-facing content.**

### Hard Rules (Never Break)

**No correlative constructions:**
- Never: "X isn't just Y - it's Z"
- Never: "It's not about X, it's about Y"
- This is the #1 AI tell - find another way

**Dash consistency:**
- Use: hyphens with spaces - like this
- Never: em dashes

**No emojis** in body content (rare exceptions for social captions).

### AI-isms to Avoid

**Words:** delve, comprehensive, crucial, vital, leverage, landscape, navigate, foster, facilitate, realm, paradigm, embark, journey, tapestry, myriad, multifaceted, seamless, cutting-edge

**Phrases:**
- "The best part? ..." / "The secret? ..."
- "What if I told you..." / "Here's the thing..." / "Let's be honest..."
- "In today's fast-paced..." / "In the ever-evolving..."
- "In conclusion" / "In summary"
- Staccato patterns: "No fluff. No filler. Just results."

### Quote Handling

Edit like a smart journalist:
- Paraphrase to tighten facts
- Keep original wording for memorable quotes
- Never hallucinate or misquote

### Internal Linking

Target 3-5+ internal links per article. Use `Master_Content_Index.md` to find related content by tag.

### Deeper Voice Guidance

Load these skills for writing tasks:
- `ghostwriter` - Anti-AI patterns, authentic voice
- `opened-identity` - Sarah persona, brand voice
- `hook-and-headline-writing` - Power words, formulas

---

## Hub-and-Spoke Model

Create one **hub piece**, spin off derivative **spokes**.

| Hub | Skill | Natural Spokes |
|-----|-------|----------------|
| Podcast | `podcast-production` | Blog, clips, LinkedIn, newsletter |
| Deep Dive | `open-education-hub-deep-dives` | 3-5 LinkedIn, Twitter, newsletter |
| Daily Newsletter | `opened-daily-newsletter-writer` | LinkedIn post, Twitter thread |

After completing a hub, **proactively offer spokes**.

---

## Maintenance

- Update this CLAUDE.md when folder structure changes
- Update `NOW.md` at session end with current state
- Use `/handoff` to capture session context to `.claude/sessions/`
- When structural changes are made, update relevant PROJECT.md files
- Periodically sync from Webflow: `python3 agents/webflow_sync_agent.py`

---

*Last Updated: 2026-01-08*
