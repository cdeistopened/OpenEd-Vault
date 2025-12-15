# Podcast Wizard → Skills Conversion Plan

**Goal**: Convert Podcast Wizard frameworks into properly structured skills with verb gerund/noun-agent naming

---

## Naming Convention Decision

Following skill-creator patterns, we'll use **noun-agent pattern** (tool/agent with -er suffix):
- ✅ `podcast-transcript-polisher`
- ✅ `youtube-title-creator`
- ✅ `podcast-clip-optimizer`
- ✅ `social-caption-writer`

---

## Podcast Wizard Frameworks → Skills Mapping

### 🎯 **TIER 1: Core Production Skills** (Create First)

#### 1. `podcast-transcript-polisher`
**Source**: `Polished Transcript Generation Guide.md`
**Category**: `video-content/podcast-transcript-polisher/`
**Purpose**: Clean up raw podcast transcripts for readability
**Dependencies**: None
**References to create**:
- `editing-principles.md` (ruthless editing, frankenbite permission)
- `formatting-standards.md` (paragraph breaks, speaker labels)
- `quality-checklist.md` (filler word removal, flow assessment)

---

#### 2. `youtube-title-creator`
**Source**: `YouTube Title & Thumbnail Framework.md` + Andrew Muto insights
**Category**: `video-content/youtube-title-creator/`
**Purpose**: Generate high-CTR YouTube titles and thumbnails
**Dependencies**: `hook-and-headline-writing`
**References to create**:
- `title-formulas-library.md` (from Andrew: direct appeal, provocative, from-X-to-Y, numbered, universalization)
- `thumbnail-text-strategies.md` (complementarity principle, left-side placement)
- `ctr-benchmarks.md` (4% = needs work, 6%+ = strong)
- `creator-hooks-ranked.md` (extract from `Creator_Hooks_Ranked_Analysis.md`)
**Examples to add**:
- George Washington titles/thumbnails
- Katie Kimball anxiety video
- Dyslexia universalization example

---

#### 3. `podcast-clip-selector`
**Source**: `YOINK Framework.md` + `Social Media Clip Selection & Creation.md`
**Category**: `video-content/podcast-clip-selector/`
**Purpose**: Identify the best 15-30 second moments from podcast episodes
**Dependencies**: None
**References to create**:
- `yoink-criteria.md` (emotion, polarization, soundbites, rants)
- `clip-types.md` (emotional, science/psychology, how-to, controversial)
- `length-guidelines.md` (15-30 seconds sweet spot, retention rules)
**Examples to add**:
- Fire clips definition
- Podcast supercut format

---

#### 4. `social-caption-writer`
**Source**: `Short-form Video Captions.md` + Andrew Muto caption insights
**Category**: `video-content/social-caption-writer/`
**Purpose**: Write on-screen captions for short-form video
**Dependencies**: `hook-and-headline-writing`
**References to create**:
- `hook-formulas.md` (2-second rule, McDonald's Test)
- `caption-sizing.md` (mobile-first, left-alignment for UI)
- `punchline-first.md` (start with payoff, add context after)
**Examples to add**:
- Katie Kimball: "The number one reason kids are so anxious"
- George Washington: "George Washington was a screw-up"
- List format with visual numbering

---

### 📊 **TIER 2: Strategic Planning Skills** (Create Second)

#### 5. `podcast-asset-planner`
**Source**: `OpenEd_Podcast_Asset_Creation_Workflow.md` + June 20 pre-production meeting
**Category**: `video-content/podcast-asset-planner/`
**Purpose**: Plan podcast episodes for maximum clip potential BEFORE recording
**Dependencies**: `youtube-title-creator`, `podcast-clip-selector`
**References to create**:
- `pre-recording-checklist.md` (brainstorm 1-3 titles/thumbnails first)
- `question-frameworks.md` (frame questions to create soundbites)
- `visual-planning.md` (plan thumbnail moments during recording)
**Examples to add**:
- Corey DeAngelis episode planning
- Daryl Stinson "one finger" visual moment

---

#### 6. `social-media-asset-creator`
**Source**: `Social_Media_Assets_Creation_Guide.md` + `Social_Media_Plan_Guide.md`
**Category**: `social-media/social-media-asset-creator/`
**Purpose**: Create full social media rollout plan from podcast episode
**Dependencies**: `podcast-clip-selector`, `social-caption-writer`
**References to create**:
- `platform-distribution.md` (Instagram/TikTok/YouTube/Facebook simultaneous)
- `proliferation-methods.md` (already exists in social-media skill)
- `collaboration-strategy.md` (Coach Meg Thomas model)

---

#### 7. `cold-open-creator`
**Source**: `Cold Open Creation Guide.md`
**Category**: `video-content/cold-open-creator/`
**Purpose**: Create compelling podcast cold opens
**Dependencies**: `podcast-clip-selector`
**References to create**:
- `cold-open-structures.md`
- `hook-techniques.md`
**Note**: May be low priority depending on current production needs

---

### 🔍 **TIER 3: Reference Material** (Not Skills - Support Existing Skills)

These should become **reference documents** in other skills' `/references/` folders:

#### Moving to `youtube-title-creator/references/`:
- `Creator_Hooks_Ranked_Analysis.md` → `creator-hooks-ranked.md`
- Portions of `YouTube Title & Thumbnail Framework.md`

#### Moving to `social-media-asset-creator/references/`:
- `Social_Media_Plan_Guide.md` portions

#### Moving to `podcast-clip-selector/references/`:
- `YOINK Framework.md` → `yoink-criteria.md`

#### Moving to `podcast-transcript-polisher/references/`:
- `Polished Transcript Generation Guide.md` portions

---

## Style Frameworks → Skills Conversion

### Option A: Create New Skills

#### 8. `newsletter-style-applier`
**Sources**:
- `The Justin Mikolay Writing Guide Compelling Simplicity.md`
- `OpenEd Newsletter Style Guide The Art of Impactful Writing.md`
- `The Packy McCormick Writing Style.md`
- `Pirate Wires Imitation Style Guide.md`

**Category**: `newsletter/newsletter-style-applier/`
**Purpose**: Apply specific writing styles to newsletter content
**References to create**:
- `mikolay-principles.md` (compelling simplicity)
- `packy-mccormick-style.md` (narrative approach)
- `pirate-wires-style.md` (punchy takes)
- `opened-style.md` (brand voice)

---

### Option B: Add to Existing Newsletter Skills

More likely: These should be **references** in the existing:
- `newsletter/daily-newsletter-workflow/references/style-guides/`
- `newsletter/weekly-newsletter-workflow/references/style-guides/`

Move:
- `mikolay-style.md`
- `packy-style.md`
- `pirate-wires-style.md`
- `opened-voice.md`

---

## Creator Hooks Ranked Analysis → Breakdown Strategy

Current file: `Creator_Hooks_Ranked_Analysis.md`

### Problems:
1. Too large to be a single reference
2. Contains multiple hook types mixed together
3. Needs to feed into multiple skills

### Solution: Break into modular references

Create in `youtube-title-creator/references/`:
```
/creator-hooks/
  ├── ranked-examples.md (top 20 hooks with metrics)
  ├── emotional-hooks.md (validation, identity, concerns)
  ├── tactical-hooks.md (how-to, tools, guides)
  ├── psychological-hooks.md (curiosity gaps, pattern interrupts)
  └── hook-analysis-framework.md (how hooks were ranked)
```

Also reference from:
- `hook-and-headline-writing/references/` (copywriting skill)
- `social-caption-writer/references/` (video captions)

---

## Conversion Workflow (Per Skill)

### Step 1: Create Directory Structure
```
Skills/video-content/podcast-transcript-polisher/
  ├── SKILL.md (main skill file with YAML frontmatter)
  ├── references/
  │   ├── README.md
  │   ├── editing-principles.md
  │   ├── formatting-standards.md
  │   └── quality-checklist.md
  └── examples/
      ├── before-after-transcript.md
      └── polish-walkthrough.md
```

### Step 2: Extract from Framework
- Read original framework file
- Identify core instructions (→ SKILL.md)
- Identify reference material (→ /references/)
- Identify examples (→ /examples/)

### Step 3: Add Andrew Muto Insights
- Review relevant meeting notes
- Extract applicable insights
- Integrate into appropriate sections
- Add as new examples

### Step 4: Write YAML Frontmatter
```yaml
---
skill_name: podcast-transcript-polisher
category: video-content
difficulty: intermediate
time_to_complete: 20-30 minutes
dependencies: []
related_skills:
  - video-content/podcast-clip-selector
  - copywriting/hook-and-headline-writing
source_material:
  - Polished Transcript Generation Guide.md
  - Andrew Muto sessions (July 2025)
last_updated: 2025-10-28
version: 1.0
---
```

### Step 5: Test & Refine
- Use skill on actual podcast transcript
- Note any gaps or confusions
- Update references/examples as needed

---

## Proposed Execution Order

### Week 1: Core Production (4 skills)
1. ✅ `podcast-transcript-polisher`
2. ✅ `youtube-title-creator`
3. ✅ `podcast-clip-selector`
4. ✅ `social-caption-writer`

### Week 2: Strategic Planning (2 skills)
5. ✅ `podcast-asset-planner`
6. ✅ `social-media-asset-creator`

### Week 3: Reference Consolidation
7. Break down Creator Hooks Ranked Analysis
8. Move style guides to appropriate /references/ folders
9. Archive obsolete frameworks

### Week 4: Optional/Advanced
10. `cold-open-creator` (if needed)
11. `newsletter-style-applier` (if needed)
12. Create master orchestrator skill (if needed)

---

## File Management Strategy

### Keep as Active Frameworks (Don't Convert):
- `Podcast README.md` (overview/index)
- `/Basic Context/` files (brand identity, not skills)

### Archive After Conversion:
- Move to `/Frameworks/Podcast Wizard/Archived/`
- Keep originals for reference
- Update Podcast README with links to new skills

### Delete After Conversion:
- Duplicates (like simplified versions if fully integrated)

---

## Questions to Answer

1. Should `youtube-show-notes-guide.md` become its own skill or a reference in `podcast-asset-planner`?
2. Should we create a master `podcast-producer` orchestrator skill that calls all the sub-skills?
3. Do we want separate skills for different video lengths (short-form vs mid-form vs long-form)?
4. Should Andrew Muto insights live in skills OR stay in their own reference documents?

---

## Success Criteria

A skill is "done" when:
- ✅ Has proper YAML frontmatter
- ✅ Clear, actionable instructions in SKILL.md
- ✅ All reference material organized in /references/
- ✅ At least 2-3 examples in /examples/
- ✅ Successfully used to create actual content
- ✅ No dependencies on frameworks (only other skills)
