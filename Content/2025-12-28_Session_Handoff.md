# Session Handoff - December 28, 2025

## What We Did

### 1. Consolidated Writing Rules in CLAUDE.md

Moved scattered writing guidelines from individual skills into root CLAUDE.md. Key decisions from interview:

- **Hard rules (never break):**
  - Correlative constructions absolutely banned ("isn't just X, it's Y")
  - Dash consistency: hyphens with spaces, no em dashes
  - No emojis in body content

- **Soft rules (generally avoid):**
  - AI-ism words (delve, comprehensive, leverage, etc.) - OK sometimes
  - AI-ism phrases ("The best part?", "Let's be honest", etc.)

- **Exceptions:**
  - "Let's dive in" OK for Charlie's newsletter sign-off only
  - Bullet points and bold are fine
  - Hedging OK when genuinely uncertain

---

### 2. Created linkedin-content Skill

New skill with 118 frameworks organized into 6 categories:

| Category | Frameworks | Use For |
|----------|------------|---------|
| Engagement | 16 | Polls, agree/disagree, crowdsource |
| Story | 24 | Transformation, failure, values |
| List/Tips | 17 | How-tos, mistakes, numbered lists |
| Contrarian | 20 | Hot takes, calling BS, pattern interrupts |
| Authority | 26 | Expertise, research, process reveals |
| Community | 15 | Shoutouts, welcomes, connections |

**Key design decisions:**
- Progressive disclosure: load ONE category file at a time (each is 3-6k words)
- Concept-first workflow: discern concept → match category → find framework → adapt
- Added SCAMPER multiplication as Step 6

**Files created:**
- `.claude/skills/linkedin-content/SKILL.md`
- `.claude/skills/linkedin-content/references/engagement-frameworks.md`
- `.claude/skills/linkedin-content/references/story-frameworks.md`
- `.claude/skills/linkedin-content/references/list-frameworks.md`
- `.claude/skills/linkedin-content/references/contrarian-frameworks.md`
- `.claude/skills/linkedin-content/references/authority-frameworks.md`
- `.claude/skills/linkedin-content/references/community-frameworks.md`

---

### 3. Documented Hub-and-Spoke Workflow in CLAUDE.md

Added section explaining content production model:

- **Hub types:** Podcast, Deep Dive, Daily Newsletter
- **Natural spokes:** LinkedIn posts, Twitter threads, video clips, newsletter segments
- **Skill chaining diagram** showing how skills call each other
- **Proactive prompts** for offering derivative content after hub completion
- **Progressive disclosure** explanation for skills

---

### 4. Updated Skill Cross-References

Added `linkedin-content` to related skills in:
- `opened-daily-newsletter-writer`
- `open-education-hub-deep-dives`
- `social-content-creation`

---

### 5. Tested linkedin-content on Real Newsletter

Used NYT Unschooling Response newsletter (Dec 15). Results:

**Three posts created using framework fitting:**
1. "I Call BS" framework → NYT contradicting itself
2. "What Most People Get Wrong" → Block's experience isn't unschooling
3. "Call Out The Unspoken" → Nirvana Fallacy

**Verdict:** Posts were strong. Framework fitting worked well.

**SCAMPER test:** Created 7 variations of Post 1. Verdict: Mechanical, unclear if it improves the process.

---

### 6. Created January 2026 Content Strategy

File: `Content/January_2026_Content_Strategy.md`

- Week-by-week calendar
- Top performer refresh schedule
- Hub-and-spoke execution plan
- LinkedIn content focus areas

*Note: User deprioritized this - come back to it later.*

---

## Open Questions / Future Directions

### The Big Reframe (Not Done Yet)

User's ideal state is different from current skill architecture:

**Current skills are:**
- Template-heavy (fill in the blank)
- Reactive (wait to be invoked)
- No memory (don't learn from feedback)
- Static (don't track platform trends)

**User wants:**
- Proactive content spotting during hub workflows
- Learning from feedback ("that hit" / "that flopped")
- Awareness of what's working on each platform NOW
- Continuous creative partnership, not template filling

**Possible solutions discussed:**
1. **Performance Log** - Track what works so Claude can reference it
2. **Proactive prompts in hub skills** - Flag content opportunities during workflow
3. **Platform Playbook** - Living doc of current best practices per platform

This needs more thinking. The skills as designed are mechanical. What's needed is a different relationship.

---

## Commits Made

1. `Consolidate writing rules in CLAUDE.md`
2. `Add linkedin-content skill with organized framework references`
3. `Add hub-and-spoke workflow and skill cross-references`
4. `Add January 2026 content strategy`
5. `Add SCAMPER multiplication method to linkedin-content skill`

---

## PR Description (Copy/Paste Ready)

```
## Summary

- Consolidate writing rules from scattered skills into CLAUDE.md
- Create linkedin-content skill with 118 frameworks in 6 categories
- Document hub-and-spoke content workflow with skill chaining
- Add cross-references between social and newsletter skills
- Add SCAMPER multiplication method to linkedin-content

## Key Changes

### Writing Rules
Hard rules (correlatives banned, no em dashes, no emojis) now in CLAUDE.md root. Soft rules documented with exceptions.

### linkedin-content Skill
New skill for LinkedIn posts using framework fitting method. 118 frameworks split into 6 category files for progressive disclosure. Includes SCAMPER for post multiplication.

### Hub-and-Spoke Workflow
Documented content model in CLAUDE.md: create hub piece (podcast/deep dive/newsletter), spin off spoke content (social posts, clips). Added proactive prompts for derivative content.

## Test Results
Tested linkedin-content on Dec 15 NYT Unschooling newsletter. Framework fitting produced strong posts. SCAMPER multiplication worked but may be too mechanical.

## Open Items
Future session: rethink skill architecture for continuous learning and proactive content suggestions.
```

---

## Files Changed

- `CLAUDE.md` - Writing rules, hub-and-spoke workflow, skills reference
- `.claude/skills/linkedin-content/*` - New skill + 6 reference files
- `.claude/skills/opened-daily-newsletter-writer/SKILL.md` - Cross-references
- `.claude/skills/open-education-hub-deep-dives/SKILL.md` - Cross-references
- `.claude/skills/social-content-creation/SKILL.md` - Cross-references
- `Content/January_2026_Content_Strategy.md` - New file (deprioritized)
