---
name: opened-weekly-newsletter-writer
description: Creates Friday OpenEd Weekly digest newsletters consolidating the week's content. This skill should be used when creating the weekly newsletter, Friday digest, or compiling weekly content. Not for daily newsletters.
---

# OpenEd Weekly Newsletter Writer

Creates Friday digest newsletters synthesizing the week's content into eight distinct sections: Opening Letter, Deep Dive, Podcast Corner, Listen for the Listeners, What's Moving, Tools We're Bookmarking, Reddit Corner, and Parting Thought.

**Not for:** Monday-Thursday daily newsletters (use `opened-daily-newsletter-writer`).

**Requirements:** Flexible length (typically 1,500-2,500 words) • NO EMOJIS in body • Pirate Wires-influenced voice • All external links include source attribution in parentheses

## Workflow

### Phase 1: Gather & Organize Source Material

Collect from the week:
- Opening letter context (timely announcements, promotions, deadlines)
- Wednesday Deep Dive article with full text and author info
- Thursday Podcast episode transcript or description
- Additional curated links, tools, Reddit discussions, and other resources

Create `Source_Material.md` with:
- All URLs, descriptions, and key quotes
- Author names and titles
- Statistics and data points
- Engagement context (why this content matters)

### Phase 2: Create Deep Dive Options (Approval Gate)

Create `Deep_Dive_Options.md` with 2-3 different teaser versions for the Deep Dive section.

**Deep Dive Format (3-4 paragraphs, third-person):**
- Written in third person (use author's name, not first person)
- 3-4 paragraphs maximum (shorter teaser, not full article)
- Hook with personal/story element
- Include key data point (bolded)
- Closing insight that hints at larger topic without revealing all
- Byline: "*By [Author], [Title] at OpenEd | Read in browser*"
- Purpose: Tease, don't tell. Make readers want to click.

Get approval on which Deep Dive version to use before proceeding.

### Phase 3: Draft All Remaining Sections

Create `Weekly_Newsletter_Draft.md` with all eight sections:

**Opening Letter (1-2 paragraphs):**
- Light, inclusive tone (e.g., Halloween reference that includes everyone)
- Feature timely announcements (sales, deadlines, giveaways)
- Numbered list for clear CTAs (e.g., How to enter giveaway)
- Integrate key messaging about educational philosophy
- Sign off: "– Charlie (the OpenEd newsletter guy)"

**Deep Dive (approved version from Phase 2):**
- Use approved teaser version
- Include byline and "Read in browser" link

**Podcast Corner (2-3 paragraphs):**
- Brief setup (who, what, why)
- Direct quotes from transcript
- Links to watch/listen/explore resources
- Optional: Add "Also worth listening to:" subsection with related OpenEd podcasts

**Listen for the Listeners (5+ podcast recommendations):**
- Curated audio/video content (NOT the main podcast)
- Each with: Title + description that earns the click + source attribution
- Pirate Wires style: Tease the value without explaining everything
- Format: `**[Title](URL)** — [Intriguing description]. ([Source])`

**What's Moving (5-6 data-driven trends):**
- Each with compelling headline and 1-2 sentence description
- Include relevant data/stats that support the trend
- Source attribution in parentheses: `(Source: [Name])`
- Hyperlink titles to URLs
- Focus on what makes each trend noteworthy, not just what happened

**Tools We're Bookmarking (10-15 tools):**
- NO category grouping (list sequentially)
- Each with: Tool name (hyperlinked) + benefit-first description (1-2 sentences) + source attribution
- Format: `**[Tool Name](URL)** — [Benefit description]. ([Source])`
- Include price when relevant
- Write to earn the click: hint at value without explaining everything
- Use Pirate Wires tone: observational, slightly irreverent

**Reddit Corner (4-5 discussions):**
- Links to Reddit r/homeschool discussions
- Each with: Title + teaser description + source attribution
- Format: `**[Title](URL)** — [Intriguing summary]. (Reddit r/homeschool)`
- Focus on human elements, real parent experiences, practical advice

**Parting Thought (2-3 paragraphs):**
- Open with a question or quote that ties the newsletter together
- Include brief story or reflection
- Close with action invitation or insight
- Typically relates to Ken Danford's message or another major theme from the week

**Closing:**
```
---

That's all for this week!

– Charlie (the OpenEd newsletter guy)

P.S. [Link to manage email preferences]
```

### Phase 4: Integrate Source Attributions (No Separate URL Mapping)

As sections are drafted, embed source attributions directly in the newsletter text. No separate `URL_Mappings.md` file needed.

**Attribution Style:**
- Always include source in parentheses after each link
- Format: `(Source: [Publication/Person Name])` or `([Platform] [Username/Handle])`
- Examples: `(AEI)`, `(Austin Scholar)`, `(The 74 Million)`, `(Reddit r/homeschool)`, `(OpenEd YouTube)`

### Phase 5: QA & Finalization

**Quality Checklist:**
- [ ] NO EMOJIS in body text
- [ ] All external links include source attribution
- [ ] Deep Dive is teaser format (not summary)
- [ ] What's Moving items are data-driven with sources
- [ ] Tools section leads with benefit, not features
- [ ] Reddit Corner items are human/story-focused
- [ ] Podcast descriptions entice clicks
- [ ] Listen for the Listeners section is included (separate from main Podcast Corner)
- [ ] All links are verified and working
- [ ] No duplicate content between sections
- [ ] Pirate Wires tone consistent throughout
- [ ] Opening letter includes all key announcements

**Archive:**
```bash
cp [working-folder]/Weekly_Newsletter_Draft.md [archive-folder]/[YYYY-MM-DD]-newsletter-final.md
```

## Reference Files

Each section of the newsletter has an example reference file with the actual format, real examples from a published newsletter, and specific instructions for writing that section:

- [Opening Letter Example](references/example-opening-letter.md) - How to write warm, inclusive openings with clear CTAs
- [Deep Dive Example](references/example-deep-dive.md) - Third-person teaser format that makes readers curious
- [Podcast Corner Example](references/example-podcast-corner.md) - How to feature the main episode with compelling hooks
- [What's Moving Example](references/example-whats-moving.md) - Data-driven trends with source attribution
- [Tools We're Bookmarking Example](references/example-tools.md) - Benefit-first descriptions with sequential ordering
- [Audio Corner Example](references/example-audio-corner.md) - Curated podcast/video recommendations that earn clicks
- [Reddit Corner Example](references/example-reddit-corner.md) - Human-focused community conversations
- [Parting Thought Example](references/example-parting-thought.md) - Closing reflection that ties the week together

## Key Distinctions

**Weekly vs Daily:**
- Daily: 500-800 words, 1 each Thought/Trend/Tool
- Weekly: 1,500-2,000 words, NO "Thoughts" section (only Parting Thought), 4-6 Trends, 8-12+ Tools

**Trends vs Thoughts:**
- Trends: Data-driven (research, enrollment, policy)
- Thoughts: Philosophy, quotes, stories → Use in Parting Thought only

**Deep Dive vs Podcast:**
- Deep Dive: Wed article, 400-600 words, teaser format
- Podcast: Thu episode, 150-250 words, one moment

## Critical Reminders

❌ NO EMOJIS in body
❌ Don't skip Checkpoint 1
❌ Deep Dive = Wed article only
❌ Trends must have data
❌ No duplicate content
✅ 1,500-2,000 words
✅ Humanize stats
✅ Hustle-style tools (benefit, no hype)

**User feedback notation:**
- `***` = preferred choice
- `<>` = extrapolate contextually
- `{question}` = answer directly
- `~~text~~` = delete
