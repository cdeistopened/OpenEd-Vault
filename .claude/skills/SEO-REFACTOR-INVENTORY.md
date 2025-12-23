# SEO Skills Refactor - Complete Inventory

This document catalogs EVERY unique capability from all SEO-related assets to ensure nothing is lost during consolidation.

---

## Source 1: `seo-content-writer` (Existing OpenEd Skill)

**Location:** `.claude/skills/seo-content-writer/SKILL.md`

### Unique Capabilities (KEEP)

| Capability | Notes |
|------------|-------|
| **Live GA4 Commands** | Top pages, declining content, engagement metrics |
| **Live DataForSEO Commands** | Keyword ideas, SERP analysis, OpenEd rankings |
| **Blog-Index.csv Integration** | 406 indexed articles for internal linking |
| **Proprietary Source Gathering** | Podcast transcripts, newsletter archive, Slack insights |
| **OpenEd-Specific CTA Guidance** | Links to info sessions, community |
| **Post-Writing Analysis Commands** | Keyword density, readability, content scrubbing |
| **Module Location Reference Table** | Where to find each Python tool |
| **Content Scrubber Integration** | Removes em-dashes, AI watermarks |
| **CLAUDE.md AI-ism Enforcement** | References forbidden phrases |
| **Example Workflow (Art Curriculum)** | Step-by-step real example |
| **Content Database Sync Instructions** | How to pull latest from Webflow |

### Elements to Preserve
- All bash command snippets (GA4, DataForSEO, scrubber)
- Internal linking workflow with `grep -i` commands
- Pre-writing checklist (research → sources → targets)
- Post-writing analysis workflow
- SEO checklist format
- Reference files table

---

## Source 2: `seo-content` (New Skill)

**Location:** `.claude/skills/seo-content/SKILL.md`

### Unique Capabilities (KEEP)

| Capability | Notes |
|------------|-------|
| **AI-ism Detection (Word Level)** | 25+ specific words to kill: delve, leverage, tapestry, etc. |
| **AI-ism Detection (Phrase Level)** | 15+ phrases: "In today's fast-paced...", "It's important to note..." |
| **AI-ism Detection (Structure Level)** | Triple pattern, perfect parallelism, hedge stack, fake objectivity |
| **AI-ism Detection (Voice Level)** | No opinions, no mistakes, distance from subject |
| **Before/After Examples** | 3 full transformations with explanations |
| **Voice Injection Points** | Personal experience, opinions, limitations, uncertainty, tangents |
| **Rhythm Variation Guide** | Vary sentence length, fragments, parenthetical asides |
| **Detection Checklist** | 10-point self-check for AI tells |
| **Read-Aloud Test** | Final voice validation |
| **E-E-A-T Examples Reference** | 20+ best-in-class examples by vertical (Paul Graham, Matt Levine, etc.) |
| **Content Type Templates** | Pillar Guide, How-To, Comparison, Listicle structures |
| **Featured Snippet Optimization** | Definition, list, table snippet formats |
| **"So What?" Chain** | Write from bottom of chain, not top |
| **SERP Analysis Framework** | What to extract from each result |
| **Content Brief Template** | Comprehensive brief format |
| **The Test (7 Questions)** | Pre-publish validation questions |

### Elements to Preserve
- Complete AI detection word/phrase lists
- All Before/After examples
- Voice injection techniques
- E-E-A-T reference list
- Content type templates with word counts
- Featured snippet optimization methods
- Quality review checklists

---

## Source 3: `keyword-research` (New Skill)

**Location:** `.claude/skills/keyword-research/SKILL.md`

### Unique Capabilities (KEEP)

| Capability | Notes |
|------------|-------|
| **6 Circles Method** | What you sell, problems, outcomes, positioning, adjacent, entities |
| **Pillar Validation (4 Tests)** | Search volume, market-centric, competitive reality, proprietary advantage |
| **Priority Matrix** | Business value × Opportunity × Speed to win |
| **90-Day Content Calendar Output** | Tier 1-4 placement |
| **Expansion Patterns** | Question, modifier, comparison patterns |
| **Clustering Framework** | Hub-and-spoke model |
| **Output Templates** | Executive summary, pillar overview, calendar |
| **Speed to Win Assessment** | Fast/Medium/Long estimates |
| **Content Type Mapping** | Type → Intent → Word count matrix |
| **Full Example (AI Marketing)** | Complete worked example |

### Elements to Preserve
- 6 Circles expansion method
- 4-test pillar validation
- Priority matrix framework
- 90-day calendar template
- Intent matching table
- Complete worked example

---

## Source 4: SEO Machine Commands

**Location:** `Content/Misc. Utilities/seomachine/.claude/commands/`

### /research Command

| Capability | Notes |
|------------|-------|
| **Keyword Research Process** | Volume, difficulty, variations, questions, intent, clusters |
| **Competitive Analysis** | Top 10 SERP, word count, themes, gaps, angles, featured snippets |
| **Context Integration** | Brand voice, internal links, target keywords cross-reference |
| **Hook Development** | Introduction angle, value prop, contrarian elements, story opportunities |
| **Output Format** | SEO foundation, competitive landscape, outline, supporting elements, linking strategy, meta preview |
| **File Management** | Auto-save to `research/brief-[topic]-[date].md` |

### /write Command

| Capability | Notes |
|------------|-------|
| **Pre-Writing Review** | Research brief, brand voice, examples, style guide, SEO guidelines |
| **Content Structure Template** | H1, intro (150-200w), body (1800-2500w), conclusion |
| **Keyword Placement Checklist** | H1, first 100, 2-3 H2s, 1-2% density, meta, URL |
| **Internal/External Linking Targets** | 3-5+ internal, 2-3 external |
| **Readability Targets** | <25 words avg, 8th-10th grade, active voice |
| **Auto Content Scrubbing** | Runs scrubber automatically after save |
| **Auto Agent Execution** | Triggers 5 agents after writing |
| **Quality Standards** | 11-point minimum requirements |
| **File Management** | Auto-save to `drafts/[topic]-[date].md` |

### /optimize Command

| Capability | Notes |
|------------|-------|
| **Keyword Analysis** | Density check, placement verification, LSI keywords |
| **Heading Structure Audit** | H1-H6 hierarchy validation |
| **Link Optimization** | Internal/external count, quality, anchor text, broken links |
| **Meta Element Optimization** | 3-5 title options, 3-5 description options |
| **Featured Snippet Opportunity** | Question, list, table, definition formats |
| **Schema Markup Suggestions** | Article, FAQ, How-To schema |
| **SEO Score (0-100)** | Keyword, technical, content, UX subscores |
| **Publishing Decision Matrix** | 90-100 excellent, 80-89 good, etc. |
| **Keyword Distribution Map** | Visual representation of placement |
| **Internal Link Finder** | `grep -i` against blog-index.csv |

### /analyze-existing Command

| Capability | Notes |
|------------|-------|
| **Content Health Score** | 0-100 multi-factor score |
| **URL/File Input** | Works with live URLs or local files |
| **5 New Analysis Tools** | Search intent, keyword clustering, length comparison, readability, SEO quality |
| **Quick Wins Section** | Immediate improvements |
| **Strategic Improvements** | Longer-term enhancements |
| **Rewrite Recommendations** | Priority level, effort estimate, expected impact |
| **Research Brief Output** | If rewrite recommended |

### /rewrite Command

| Capability | Notes |
|------------|-------|
| **Scope Classification** | Light (20-30%), Moderate (40-60%), Major (70-90%), Complete (90%+) |
| **What to Keep/Update/Add/Remove** | Decision framework |
| **Change Summary Format** | Before/after tracking |
| **Auto Scrubbing** | Removes AI watermarks |
| **Auto Agent Execution** | 4 agents post-rewrite |

---

## Source 5: SEO Machine Agents

**Location:** `Content/Misc. Utilities/seomachine/.claude/agents/`

### content-analyzer Agent

| Capability | Notes |
|------------|-------|
| **5 Python Module Integration** | search_intent, keyword_analyzer, content_length, readability, seo_quality |
| **Executive Summary Output** | Publishing readiness assessment |
| **Search Intent Analysis** | Primary/secondary intent, confidence scores |
| **Keyword Distribution Heatmap** | By section visualization |
| **Topic Cluster Detection** | TF-IDF and K-means clustering |
| **Competitive Positioning** | Length/optimization comparison |
| **Priority Action Plan** | Critical → High → Optimization |
| **Publishing Checklist** | Comprehensive pre-publish checklist |

### editor Agent

| Capability | Notes |
|------------|-------|
| **Humanity Check Framework** | Robotic red flags vs. human green flags |
| **5-Level Readability Analysis** | Sentence, paragraph, section, voice, specificity |
| **Show Don't Tell Examples** | Before/after transformations |
| **Personality Injection Guide** | Parentheticals, rhetorical questions, direct address, fragments |
| **Corporate Speak Kill List** | Leverage→Use, Utilize→Use, etc. |
| **Generic → Specific Transformations** | Recently → March 2024, Many → 73% |
| **Sentence Structure Variation** | Breaking monotony |
| **Actionable List Transformation** | Generic → specific list items |
| **Humanity Score (0-100)** | Voice, specificity, flow, engagement subscores |
| **Critical Edits Format** | Current → Why It Fails → Rewritten → Why This Works |
| **Pattern Analysis** | Recurring issues across article |
| **Before/After Readability Metrics** | Projected improvement |

### Other Agents (Summarized)

| Agent | Key Capabilities |
|-------|------------------|
| **seo-optimizer** | On-page SEO analysis, optimization recommendations |
| **meta-creator** | 5 title variations, 5 description variations, SERP preview |
| **internal-linker** | 3-5 specific placements, anchor text, user journey mapping |
| **keyword-mapper** | Density, distribution, critical placement checklist, cannibalization risk |
| **performance** | GA4/GSC integration, quick wins, declining content, trending topics, week-by-week roadmap |

---

## Source 6: Python Modules

**Location:** `Content/Misc. Utilities/seomachine/data_sources/modules/`

| Module | Capabilities |
|--------|-------------|
| **google_analytics.py** | get_top_pages(), get_declining_pages(), engagement metrics |
| **dataforseo.py** | get_keyword_ideas(), get_serp_data(), get_rankings() |
| **keyword_analyzer.py** | analyze_keywords() - density, distribution, stuffing risk, clustering |
| **readability_scorer.py** | analyze_readability() - Flesch scores, grade level, sentence length |
| **content_scrubber.py** | scrub_file() - removes em-dashes, Unicode watermarks |
| **seo_quality_rater.py** | rate_seo_quality() - 0-100 with category breakdowns |
| **content_length_comparator.py** | compare_content_length() - vs top 10-20 SERP |
| **search_intent_analyzer.py** | analyze_intent() - informational/commercial/transactional |

---

## Consolidation Plan

### Proposed: `seo-research` Skill

Combines:
- 6 Circles Method (from keyword-research)
- Pillar Validation 4 Tests (from keyword-research)
- Priority Matrix (from keyword-research)
- Live DataForSEO integration (from seo-content-writer)
- Live GA4 integration (from seo-content-writer)
- /research command workflow (from seomachine)
- Content database sync (from seo-content-writer)
- NotebookLM integration for proprietary insights (NEW)

### Proposed: `seo-content-writer` (Refactored)

Combines:
- Content type templates (from seo-content)
- AI-ism detection (word/phrase/structure/voice) (from seo-content)
- E-E-A-T framework with examples (from seo-content)
- Voice injection techniques (from seo-content)
- Before/After humanization examples (from seo-content)
- Editor agent humanity framework (from seomachine)
- Live post-analysis commands (from seo-content-writer)
- Content scrubber integration (from seo-content-writer)
- Blog-index.csv internal linking (from seo-content-writer)
- OpenEd proprietary sources (from seo-content-writer)
- /write, /optimize command workflows (from seomachine)
- All 5 analysis Python modules (from seomachine)

---

## Skills to Delete After Refactor

1. `.claude/skills/seo-content/` - Absorbed into seo-content-writer
2. `.claude/skills/keyword-research/` - Absorbed into seo-research

## Files to Keep As-Is

- `Content/Misc. Utilities/seomachine/` - Python modules remain unchanged
- All `/data_sources/modules/*.py` files
- `context/blog-index.csv`

---

## Verification Checklist

After refactor, verify these capabilities work:

- [ ] Live GA4 queries return data
- [ ] Live DataForSEO queries return data
- [ ] Content scrubber removes em-dashes
- [ ] Keyword density analysis works
- [ ] Readability scoring works
- [ ] 6 Circles expansion method documented
- [ ] Pillar validation 4 tests documented
- [ ] All AI-ism word/phrase lists preserved
- [ ] All Before/After examples preserved
- [ ] E-E-A-T reference list preserved
- [ ] Content type templates preserved
- [ ] Editor humanity framework preserved
- [ ] Internal linking with blog-index.csv works
- [ ] NotebookLM can be queried for proprietary insights
