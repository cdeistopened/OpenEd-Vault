# OpenEd NOW

**Last Updated:** 2026-01-08 (Evening)

---

## Current Focus

### Context Architecture Cleanup - COMPLETE
Major reorganization of OpenEd Vault structure:
- CLAUDE.md slimmed from 560 → 118 lines
- NOW.md created as living handoff
- PROJECT.md files added to all Studio projects/workflows
- References folder created for on-demand context

### Guest Contributor Pipeline - READY TO SEND
CRM audit complete (382/382 contacts). 4 email drafts ready:

| Contact | Company | Topic | Status |
|---------|---------|-------|--------|
| Mason Pashia | Getting Smart | Marketplace data | Ready |
| Kathleen Ouellette | VictoryXR | VR education | Ready |
| Robin Smith | Surge Academy | Coding/game design | Ready |
| Jon England | Libertas Institute | Microschools | Ready |

**Drafts:** `Studio/SEO Content Production/Guest Contributors/Drafts/`

---

## Active Work Streams

### This Week
- [ ] Send 4 contributor outreach emails
- [ ] Daily newsletters (Mon-Thu)
- [ ] Weekly podcast episode

### Blocked
- **GSC Access** - Need ops to add service account for SEO quick wins
  - Account: `opened-service-account@gen-lang-client-0217199859.iam.gserviceaccount.com`

### In Progress
- **Meta Ads** - 100 concepts written (V1 + V2), needs campaign selection
- **Eddie Awards** - Website planning phase
- **Lead Magnet** - Adaptive quiz in development
- **KPI Discussions** - Q1 bonus structure planning

---

## Folder Structure (Current)

```
OpenEd Vault/
├── CLAUDE.md                    # Slimmed navigation + writing rules
├── NOW.md                       # This file - living handoff
├── Master_Content_Index.md      # 406 published pieces indexed
│
├── Studio/                      # Active projects + workflows
│   ├── Eddie Awards/PROJECT.md
│   ├── Meta Ads/PROJECT.md
│   ├── SEO Content Production/PROJECT.md
│   ├── Lead Magnet Project/PROJECT.md
│   ├── Retargeting Strategy FY26-27/PROJECT.md
│   ├── KPI Discussions/PROJECT.md    # NEW
│   ├── OpenEd Daily/PROJECT.md       # Workflow
│   ├── Open Ed Podcasts/PROJECT.md   # Workflow
│   └── Open Education Hub/PROJECT.md # Workflow
│
├── Content/Master Content Database/  # Published archive
├── CRM/                              # Contact management
├── agents/                           # Python automation
│
└── .claude/
    ├── skills/          # 24 content production skills
    ├── references/      # On-demand context (SEO commands, etc.)
    └── sessions/        # Historical handoffs
```

---

## Key Contacts (High Engagement)

| Contact | Company | Opportunity |
|---------|---------|-------------|
| Sara Jean Kwapien | Outschool | Manuscript feedback done, pitch article |
| Ryhen Miller-Hollis | Education Reimagined | Reciprocal blog post |
| The Good and the Beautiful | - | MAJOR curriculum brand, revive |
| Rainbow Resource (Zach Smith) | - | LARGEST retailer, revive |

---

## Recent Session (2026-01-08 Afternoon) - SEO Content Production Deep Dive

### What Was Done

#### 1. Weekly SEO Report Enhanced
- **Removed fake "Content Gaps" section** - Was just keyword expansion, not real competitor analysis
- **Added Priority Keyword Tracking** - Tracks OpenEd's actual targets from content plan:
  - High-volume: montessori (63K), homeschool (21K), classical education (4.1K)
  - State pages: Oregon, Nevada, Indiana
  - Curriculum by grade level
- **Added relevance filtering** to Quick Wins
- Report script: `.claude/tools/seomachine/tools/weekly_seo_report.py`

#### 2. Created State Pages Sub-Project
- **Folder:** `Studio/SEO Content Production/State Pages/PROJECT.md`
- **Template created** for state pages with:
  - Legal nuance: OpenEd families are technically NOT homeschoolers legally, but still identify as such
  - Dual intent: "how to homeschool in X" + "homeschool program in X"
  - Competitor analysis (HSLDA structure documented)
  - Quality gates to avoid duplicate content
- **Operating states confirmed (9 total):** AR, IN, IA, KS, MN, MT, NV, OR, UT
- Created reference: `.claude/references/opened-program-details.md`

#### 3. Created Versus Sub-Project  
- **Folder:** `Studio/SEO Content Production/Versus/PROJECT.md`
- **Template with quality gates:**
  - Gate 1: Gap analysis (does this already exist?)
  - Gate 2: Content depth (1,500+ words, genuine differentiators)
  - Gate 3: Original value (insights not found elsewhere)
- **Slack as unfair advantage** - Real teacher perspectives from #recommendations

#### 4. Extracted Fred's Methodology (SEO Guy)
- Uses SEMrush for keyword research + site health
- Produces outlines with H2s, word counts, meta descriptions
- Charlie builds automation with DataForSEO
- Meeting notes archived to `_archive/meetings/`

#### 5. API Connections Established
- **Slack:** ✅ Working via direct API (xoxc/xoxd tokens)
  - Found 247+ curriculum discussions in #recommendations
  - Key channels: #recommendations (154), #team-curriculum (90), #teachers-state-specific-feedback (116)
- **Notion:** ✅ Working - "Claude MCP" integration connected to "OpenEd Content Engine"
  - 30 databases accessible including: Curriculum List, Oregon Homeschool Hubs, Master Content Database
- **MCP Note:** OpenCode in Zed uses different MCP config than Claude desktop app. Direct API calls work.

#### 6. Neil Patel 2026 SEO Research
- "Search Everywhere Optimization" - TikTok, Reddit, YouTube are search engines now
- Topical depth > keywords (validates hub-and-spoke approach)
- AI-first search requires quotable, specific, authoritative content
- For scaled content: need 40%+ unique per page, local resources, genuine expertise

### Key Files Created/Modified
```
SEO Content Production/
├── PROJECT.md (updated - 92 target articles)
├── State Pages/
│   └── PROJECT.md ← NEW (template + 9 states)
├── Versus/
│   └── PROJECT.md ← NEW (template + quality gates)
├── _archive/
│   └── meetings/
│       ├── SEO-Meetings-Summary.md ← NEW (extracted insights)
│       └── SEO Meetings notes.md (moved)
└── Lead Magnet Project/PROJECT.md (updated - quiz keyword added)

.claude/references/
└── opened-program-details.md ← NEW (9 states, program features)

OpenEd Vault/CLAUDE.md (updated - added operating states line)
```

### Decisions Made
- **State pages only for operating states** - 9 states, not arbitrary high-volume keywords
- **Versus pages need quality gates** - No mass replication without gap analysis
- **Slack is the unfair advantage** - Real teacher perspectives differentiate our content
- **Fred provides strategy, Charlie builds automation** - Complement, don't replace (yet)
- **Direct API calls work in OpenCode** - Don't need MCP for Slack/Notion

### Ready for Next Session
1. **Oregon state page** - Template ready, have local resources database, Notion has "Oregon Homeschool Hubs"
   - Notion DB: `376a31a1-1c61-4406-82b1-8f9ed163f7ce`
   - Slack: Query `#teachers-state-specific-feedback` for Oregon
   - Charlie has additional local resources database
2. **Versus pilot page** - Can pull Slack data for any curriculum (e.g., Saxon Math had 10+ discussions)
3. **Fellow MCP** - Configured via OAuth (`claude mcp add --transport http fellow https://fellow.app/mcp`)
   - ⚠️ **Blocked:** Admin must enable "Allow users to create MCP connections" in Fellow Workspace Settings → Security
   - Once enabled, authenticate via `/mcp` in Claude Code
4. **Notion knowledge capture** - Can save structured content to Notion databases

### Detailed Handoff
See: `.claude/sessions/2026-01-08-seo-content-production-handoff.md`

### API Access Summary
| Service | Status | Token Location |
|---------|--------|----------------|
| Slack | ✅ xoxc/xoxd tokens | In this chat (save to .env if needed) |
| Notion | ✅ ntn_* token | `.claude/settings.local.json` |
| DataForSEO | ✅ | `.claude/tools/seomachine/data_sources/config/.env` |
| GSC | ⚠️ Need ops | Service account pending |
| GA4 | ✅ | Same config as DataForSEO |

---

## Previous Session (2026-01-08 Morning)

### What Was Done
- Reorganized entire OpenEd Vault context architecture
- Slimmed CLAUDE.md to navigation + writing rules only
- Created NOW.md pattern (replaces accumulating handoffs)
- Added PROJECT.md to: OpenEd Daily, Podcasts, Open Education Hub, Lead Magnet
- Moved SEO commands and KPI discussions to references/

### Architecture Established
```
CLAUDE.md = Stable map + universal rules (rarely changes)
NOW.md = Living handoff (update each session)
PROJECT.md = Per-project context
.claude/references/ = On-demand deep context
.claude/skills/ = Auto-loading capabilities
```

---

*Update this file at session end. For project-specific context, see PROJECT.md in each Studio folder.*
