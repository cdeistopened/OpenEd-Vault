---
name: opened-daily-newsletter-writer
description: Creates Monday-Thursday OpenEd Daily newsletters (500-800 words) with Thought-Trend-Tool structure. Use when the user asks to create a daily newsletter, write daily content, or transform source material into newsletter segments. Not for Friday Weekly digests.
---

# OpenEd Daily Newsletter Writer

Creates Monday-Thursday daily newsletters (500-800 words) that challenge standardized education with contrarian angles and authentic voice. Structured workflow with approval checkpoints.

**Not for:** Friday Weekly digests (use `weekly-newsletter-workflow`), social media only, or blog posts.

## Workflow

### Phase 1: Content Curation

Select 3 segments (Thought/Tool/Trend) ensuring orthogonality and thematic coherence.

**Segment types:**
- **THOUGHT:** Contrarian takes, educational philosophy
- **TREND:** Current developments, research, student stories
- **TOOL:** Practical resources readers can use immediately

**Critical:** Thought and Trend must be related but NOT repetitive.

Create working folder:
```bash
mkdir "Content/OpenEd Daily/[YYYY-MM-DD] - [Brief Theme]/"
```

Create `Source_Material.md` with URLs, key quotes, and angle notes.

---

### Phase 2: Angle Development (Checkpoint 1)

Create `Checkpoint_1_Angles.md` - **DO NOT proceed to Phase 3 without approval.**

For each segment, generate 3-4 angles using:
- What's the contrarian but obviously true take?
- How does this challenge standardized education?
- Would Sarah (our One True Fan) forward this?

See [OpenEd Identity Framework](../../Frameworks/Basic Context/OpenEd Identity Framework.md) for core beliefs.

**Segment structure:**
- **THOUGHT:** Story first, insight second (~100-120 words)
- **TREND:** Data and concrete examples (~100-120 words)
- **TOOL:** Lead with benefit, not description (~100-120 words)

**Section titles:** ALL CAPS H2, 2-6 words. Use sticky techniques (alliteration, contrast, curiosity).

**Subject lines:** Generate 10 options (8-10 words max):
- 3-4 Curiosity-Based
- 3-4 Specificity-Based
- 2-3 Hybrid

See [Subject Line Guide](../../Frameworks/Newsletter/Subject Line Guide.md) for formulas.

**Preview text:** 40-100 characters. Formula: [Detail] + [Intrigue] + "PLUS: [Value]"

**Checkpoint 1 template:**
```markdown
# Checkpoint 1: Angles & Structure - [Date]

## SUBJECT LINE OPTIONS (10 total)
[Organize by type: Curiosity, Specificity, Hybrid]

## PREVIEW TEXT
[Draft]

## SEGMENT 1: [TITLE] (Type)
**Source:** [URL]
**Angle Options:** [3-4 options]
**Recommended:** [Which and why]
**Structure:** Hook / Substance / Insight

## SEGMENT 2: [TITLE] (Type)
[Same format]

## SEGMENT 3: [TITLE] (Type)
[Same format]

## ORTHOGONALITY CHECK
- [ ] Thought and Trend are distinct
- [ ] Aligns with OpenEd beliefs
- [ ] Would Sarah forward this?
```

🛑 **PAUSE:** Get user approval before Phase 3.

**User feedback notation:**
- `***` = preferred choice
- `<>` = extrapolate contextually
- `{question}` = answer directly
- `~~text~~` = delete

---

### Phase 3: Newsletter Writing

Create `Newsletter_DRAFT.md` after Checkpoint 1 approval.

### Opening Letter Strategy (~100-150 words)

The opening letter establishes the relationship with the reader. It should be personal, encouraging, and slightly contrarian or curious.

**Key Elements:**
1.  **Greeting:** "Greetings Eddies!", "Welcome Eddies!", or "Greetings!".
2.  **The Hook:** Start with a story, a startling statistic ("20,000 subscribers", "$16,000 per child"), a contrarian question ("Why do students find science boring?"), or a community milestone.
3.  **The Pivot:** Connect the hook to the broader mission of "opening up education" or the specific value in today's issue.
4.  **The Tease:** Mention what's coming (Deep Dive, etc.) without summarizing it.
5.  **The Sign-off:** Almost always ends with "Let's dive in." (or occasionally "Read on...").

**Style Notes:**
-   **Voice:** Encouraging ("you've got this!"), authentic (admits to "silly gimmicks"), and mission-driven.
-   **Format:** Short paragraphs (1-2 sentences).
-   **Signature:** The opening is a prelude; sign off with "Let's dive in." The actual signature ("– Charlie") comes at the end of the newsletter.

**Examples:**
- *Milestone/Community:* "Greetings Eddies! It just came to my attention that the OpenEd Daily hit a new milestone... We take this as a sign of the growing appetite for trustworthy content... Onward & upward,"
- *Contrarian/Data:* "Greetings! An education expert recently published something that's making a lot of parents nervous... The data sounds brutal, but is he interpreting it correctly? Let's dive in."
- *Story-Driven:* "Greetings! Ken Danford had spent six years teaching... In it, he found case studies of teens who left school and turned out... fine! Let's dive in."

**Opening Checklist:**
- [ ] Greetings Eddies! (or variation)
- [ ] Hook (Story/Stat/Question)
- [ ] Pivot to mission/value
- [ ] "Let's dive in." sign-off
- [ ] ❌ No spoiling the segments

**Write 3 segments (each ~100-120 words):**

Apply voice from:
- [Pirate Wires Style Guide](../../Frameworks/Style/Pirate Wires Imitation Style Guide.md)
- [OpenEd Writing Guide](../../Frameworks/Style/OpenEd Newsletter Style Guide The Art of Impactful Writing.md)

**Format requirements:**
- NO EMOJIS (non-negotiable)
- ALL CAPS H2 titles for segments
- **Bold** for key quotes/stats
- Hyperlinks throughout (not just at ends)
- `---` between sections

**Complete structure:**
```markdown
**SUBJECT:** [From Checkpoint 1]
**PREVIEW:** [From Checkpoint 1]
---

[Opening]
---

## [SEGMENT 1 TITLE]
[100-120 words]
---

## [SEGMENT 2 TITLE]
[100-120 words]
---

## [SEGMENT 3 TITLE]
[100-120 words]
---

That's all for today!

– Charlie (the OpenEd newsletter guy)

P.S. [Optional announcement]
```

**Target:** 500-800 words total.

Submit as `Newsletter_DRAFT.md`. Iterate based on user feedback using notation from Phase 2.

---

### Phase 4: Social Media (Optional)

For social repurposing, use the `social-content-creation` skill or create `Social_Media_Plan.md`.

See [Social Media frameworks](../../Frameworks/Social Media/) for templates.

---

### Phase 5: QA & Archive

**Final checklist:**
- [ ] Segments are orthogonal
- [ ] NO EMOJIS in body
- [ ] ALL CAPS H2 titles
- [ ] 500-800 words total
- [ ] All links work
- [ ] Aligns with OpenEd beliefs

**Archive:**
```bash
cp [working-folder]/Newsletter_FINAL.md daily-newsletter-workflow/examples/[YYYY-MM-DD]-newsletter.md
```

## Reference Files

**Core frameworks:**
- [OpenEd Identity Framework](../../Frameworks/Basic Context/OpenEd Identity Framework.md) - Beliefs and audience
- [Subject Line Guide](../../Frameworks/Newsletter/Subject Line Guide.md) - Formulas and strategies
- [Pirate Wires Style](../../Frameworks/Style/Pirate Wires Imitation Style Guide.md) - Voice examples
- [OpenEd Writing Guide](../../Frameworks/Style/OpenEd Newsletter Style Guide The Art of Impactful Writing.md) - Sticky sentences
- [Opening Letter Examples](references/Opening_Letter_Examples.md) - Examples of tone and structure

**Related skills:**
- `weekly-newsletter-workflow` - Friday digest
- `social-content-creation` - Social repurposing

## File Naming

Working folder: `Content/OpenEd Daily/[YYYY-MM-DD] - [Theme]/`

Files:
- `Source_Material.md`
- `Checkpoint_1_Angles.md`
- `Newsletter_DRAFT.md`
- `Newsletter_FINAL.md` (only after approval)

## Critical Reminders

❌ NO EMOJIS in body
❌ Don't skip Checkpoint 1
❌ Opening must not spoil segments (tease, don't summarize)
❌ Thought and Trend must be orthogonal
✅ 500-800 words total
✅ ALL CAPS H2 titles
✅ Link early and often
