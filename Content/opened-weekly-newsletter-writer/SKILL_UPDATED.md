---
name: opened-weekly-newsletter-writer
description: Creates Friday OpenEd Weekly digest newsletters consolidating the week's content. This skill should be used when creating the weekly newsletter, Friday digest, or compiling weekly content. Not for daily newsletters.
---

# OpenEd Weekly Newsletter Writer

Creates Friday digest newsletters synthesizing the week's content into six distinct newsletter sections, plus a bonus Phase 4 for creating Ed's Roundup Twitter thread strategy.

**Not for:** Monday-Thursday daily newsletters (use `opened-daily-newsletter-writer`).

**Requirements:** Flexible length (typically 1,500-2,500 words) • NO EMOJIS in body • Pirate Wires-influenced voice • All external links include source attribution in parentheses

## Workflow

### Phase 1: Gather & Organize Source Material

Collect from the week:
- Opening letter context (timely announcements, promotions, deadlines)
- Deep Dive article with full text and author info
- Deep Dive Podcast episode transcript or description
- Additional curated links, tools, and other resources

Create `Source_Material.md` with:
- All URLs, descriptions, and key quotes
- Author names and titles
- Statistics and data points
- Engagement context (why this content matters)
- Names and Twitter handles of people/organizations mentioned (for Phase 4 Twitter thread)

### Phase 2: Draft Opening Letter

Create opening section that:
- Opens with greeting ("Greetings Eddies!" or similar)
- Features the main giveaway/announcement winner/deadline
- Includes light humor (corny joke, relatable observation)
- States what's NOT you (if applicable - "you didn't win")
- Explains the fairness/transparency (e.g., Python script selection)
- Mentions consolation prizes/alternatives
- Ends with clear CTA and links
- Signs off: "– Charlie (the OpenEd newsletter guy)"

**Opening Letter Example Structure:**
1. Greeting + Main announcement
2. Light humor about the "you didn't win" situation
3. Context/transparency about selection process
4. Consolation prizes or alternatives
5. Clear deadline + CTA link
6. Charlie signature

### Phase 3: Draft All Remaining Newsletter Sections

Create `Weekly_Newsletter_Draft.md` with six sections:

**DEEP DIVE: [Article Title]**
- Feature the week's main article/guide
- 3-4 paragraphs, third-person or narrative style
- Hook with compelling angle (can reference notable figures like Adam Savage)
- Include key data point(s)
- End with link to full article: `[Read the full guide on OpenEd](URL)`

**[PODCAST TITLE]: [Episode Title]**
- Brief setup (guest, host, topic)
- One compelling moment or key insight
- 2-3 direct quotes from transcript
- Practical takeaway or hook
- Link to listen: `[Listen to the full episode](URL)`

**Trends We're Following**
- 4-6 data-driven trends/stories from the week
- Each with compelling headline and 1-2 sentence description
- Include relevant data/stats that support the trend
- Source attribution in parentheses: `([Source Name](URL))`
- Focus on what makes each trend noteworthy, not just what happened

**Tools We're Bookmarking**
- 10-15 resources, tools, curricula, or recommendations
- NO category grouping (list sequentially)
- Each with: Tool name (hyperlinked) + benefit-first description (1-2 sentences) + source attribution
- Format: `**[Tool Name](URL)** — [Benefit description]. ([Source])`
- Write to earn the click: hint at value without explaining everything
- Use Pirate Wires tone: observational, slightly irreverent

**Ed's Stable**
- Social media highlights from the week
- Reference recent Instagram/social posts from OpenEd
- Include quirky brand moments (horse mask, chalkboard, etc.)
- 2-3 specific post examples with themes
- Close with reflection that ties newsletter theme to community/brand energy

**Closing:**
```
---

That's all for this week!

– Charlie (the OpenEd newsletter guy)

P.S. [Link to manage email preferences](#)
```

### Phase 4: Create Ed's Roundup Twitter Thread Strategy

**NEW PHASE:** Create `Twitter_Thread_Roundup.md` (or `Twitter_Thread_Roundup_V2.md` if iterating)

This phase creates a multi-tweet thread that recaps the week's key stories and creators featured in the newsletter.

**Step 1: Identify All Twitter Handles**
- Create a comprehensive list of every person/organization mentioned in the newsletter
- Search Twitter/X for each to find active accounts and verify handles
- Prioritize people who are:
  - Featured guests (podcasters, experts)
  - Content creators referenced (Austin Scholar, Adam Savage, Henrik Wes, etc.)
  - Organizations mentioned (LearningRx, Simply Charlotte Mason, etc.)
- Format as: `@handle (Name/Organization) - [brief context]`

**Step 2: Research Active Accounts**
- For each identified person/org, verify:
  - Do they have a Twitter account?
  - Is it active (posted in last 30 days)?
  - Should they be tagged in the thread?
- Document in the Twitter thread file which handles are taggable

**Step 3: Draft Twitter Thread**

**Opening Tweet (Hook):**
- Opens with brand identity: "Ed's Roundup: The most clicked education links from this week"
- Or: "Here's what 10K+ readers of OpenEd Weekly are paying attention to"
- States number of creators: "13 creators. 1 thread."
- Includes emoji (horse/roundup theme): 🪶 or 🐴
- Clear call to action: "(thread)"

**Creator Tweets (One per major theme/person):**
- Feature person's name: @handle
- Their contribution/insight (1 sentence max)
- Direct quote if available
- Link to their content or OpenEd's content about them
- Use proven tweet structures: Direct Quote, Problem Recognition, Data Point, Contrarian Take, Observation Post

**Closing Tweets:**
- Wrap-up tweet with CTA to OpenEd Daily/Weekly
- Engagement tweet asking readers to reply with their favorite creators

**Format Examples:**

*Tweet with direct quote:*
```
"When we teach science as memorization, we're missing the point."

— @AdamSavage (MythBusters)

That quote started a conversation about why wonder matters more than worksheets.

Full deep dive: https://opened.co/blog/best-homeschool-science-curriculum
```

*Tweet with problem/insight:*
```
The reason your kid won't listen when you yell?

It's not defiance. It's neurology.

Dr. Amy Moore explains auditory exclusion: https://opened.co/blog/why-your-adhd-kid-wont-listen-its-not-what-you-think
```

*Tweet with data:*
```
1.5M students are now in microschools.

That's the same as Catholic schools.

Same enrollment. Different satisfaction rates.

@rebeleducator mapped it: [URL]
```

**Reference Guide:** See `references/eds-roundup-example.md` for complete real-world example from Nov 14, 2025 newsletter

### Phase 5: Integrate Source Attributions

As sections are drafted, embed source attributions directly in the newsletter text. No separate `URL_Mappings.md` file needed.

**Attribution Style:**
- Always include source in parentheses after each link
- Format: `(Source: [Publication/Person Name])` or `([Platform] [Username/Handle])`
- Examples: `(Newsweek)`, `(Austin Scholar)`, `(LearningRx)`, `(Simply Charlotte Mason)`, `(OpenEd YouTube)`

### Phase 6: QA & Finalization

**Quality Checklist:**
- [ ] NO EMOJIS in newsletter body text (OK in Twitter thread)
- [ ] All external links include source attribution
- [ ] Deep Dive article is compelling (not just a summary)
- [ ] Podcast highlight is one moment, not overview
- [ ] Trends section is data-driven with sources
- [ ] Tools section leads with benefit, not features
- [ ] Ed's Stable reflects actual brand moments
- [ ] All links are verified and working
- [ ] No duplicate content between sections
- [ ] Pirate Wires tone consistent throughout
- [ ] Opening letter includes all key announcements
- [ ] Twitter thread handles are verified and active

**Archive:**
```bash
cp [working-folder]/Weekly_Newsletter_Draft.md [archive-folder]/[YYYY-MM-DD]-newsletter-final.md
cp [working-folder]/Twitter_Thread_Roundup.md [archive-folder]/[YYYY-MM-DD]-twitter-roundup.md
```

## Reference Files

Each section of the newsletter has an example reference file with the actual format, real examples from a published newsletter, and specific instructions for writing that section:

- [Opening Letter Example](references/example-opening-letter.md) - How to write warm, inclusive openings with clear CTAs
- [Deep Dive Example](references/example-deep-dive.md) - Third-person teaser format that makes readers curious
- [Podcast Highlight Example](references/example-podcast-highlight.md) - One compelling moment with quotes
- [Trends We're Following Example](references/example-trends.md) - Data-driven stories with source attribution
- [Tools We're Bookmarking Example](references/example-tools.md) - Benefit-first descriptions with sequential ordering
- [Ed's Stable Example](references/example-eds-stable.md) - Social media highlights and brand moments
- [Ed's Roundup Twitter Thread Example](references/eds-roundup-example.md) - Complete Twitter thread with all creators tagged

## Key Distinctions

**Weekly vs Daily:**
- Daily: 500-800 words, 1 each Trend/Tool, shorter sections
- Weekly: 1,500-2,500 words, 4-6 Trends, 10-15 Tools, deeper analysis

**Newsletter Structure (Now Simplified):**
- Opening Letter
- Deep Dive Article (Wed article)
- Deep Dive Podcast Highlight (Thu episode - one moment)
- Trends We're Following (data-driven stories)
- Tools We're Bookmarking (resources, curricula, recommendations)
- Ed's Stable (brand moments, social highlights)
- BONUS Phase 4: Ed's Roundup Twitter Thread (recap with all creators tagged)

**What's Removed:**
- "Listen for the Listeners" (too redundant with Trends)
- "Reddit Corner" (content integrated into other sections as relevant)
- "Parting Thought" (function now served by Ed's Stable closing)

## Critical Reminders

❌ NO EMOJIS in newsletter body
❌ Don't skip Phase 1 (source material gathering)
❌ Deep Dive = Wed article ONLY (not podcast)
❌ Trends must have data
❌ No duplicate content between sections
❌ Twitter handles must be verified before tagging

✅ 1,500-2,500 words for newsletter
✅ Humanize stats with context
✅ Benefit-first approach for tools
✅ Create Twitter thread in Phase 4 (bonus amplification)
✅ Archive both newsletter AND Twitter thread

## Phase 4 Twitter Thread - Quick Reference

**Goal:** Convert newsletter into multi-tweet thread that:
1. Identifies all mentioned creators/organizations
2. Verifies their Twitter handles are active
3. Drafts 12-15 tweets featuring each
4. Uses proven tweet structures
5. Tags relevant people appropriately
6. Ends with clear CTA to OpenEd Daily/Weekly

**Expected Output:**
- 12-15 individual tweets
- Each featuring one creator/insight/data point
- Handles verified and active
- Links pointing to real content
- Ending with engagement CTA

**Success Metrics:**
- All mentioned creators identifiable
- Twitter handles verified (not guessed)
- Diverse tweet structures used
- Clear narrative flow across thread
- Specific CTAs (not generic)

---

## Related Skills

- `hook-and-headline-writing` - For generating newsletter subject lines
- `social-content-creation` - For repurposing newsletter sections into individual posts
- `video-caption-creation` - For creating captions for clips featured in newsletter

---

## Version History

- **v2.0** (2025-11-14): MAJOR UPDATE
  - Simplified from 8 sections to 6 newsletter sections
  - Headers updated: "Trends We're Following" (not "What's Moving")
  - Headers updated: "Ed's Stable" (not "Parting Thought")
  - Removed: "Listen for the Listeners" and "Reddit Corner" (redundant)
  - ADDED: Phase 4 Twitter Thread Strategy ("Ed's Roundup")
  - Added comprehensive Twitter handle verification process
  - Added tweet structure examples and reference guide

- **v1.0** (Previous): Original 8-section structure with separate Podcast Corner and Reddit Corner

---

*For detailed examples of the current structure, see the reference files folder and the Nov 14, 2025 newsletter implementation.*
