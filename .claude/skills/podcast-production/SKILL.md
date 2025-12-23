---
name: podcast-production
description: Complete workflow for producing podcast episodes from raw transcript to publishable YouTube and social media assets. Four-checkpoint system for strategic decision-making plus final polished assets.
---

# Podcast Production Skill

## Overview

Transform a raw podcast transcript into polished, multi-platform content assets through four strategic checkpoints. Each checkpoint delivers decision-ready analysis in a markdown file for your feedback before proceeding. You'll provide feedback directly in the checkpoint documents, then we'll iterate before moving to the next phase. Final outputs include publication-ready YouTube strategy and a narrative-driven blog post.

**Workflow Structure:**
- Start with `[Guest]_Source_Material.md` (raw transcript + notes)
- Create `Checkpoint_1_Comprehensive_Analysis.md` (your feedback here)
- Create `Checkpoint_2_Cold_Opens_and_Clips.md` (your feedback here)
- Create `Checkpoint_3_YouTube_Strategy.md` (your feedback here)
- Create `Checkpoint_4_Polished_Transcript_and_Blog.md` (final deliverable)

## When to Use This Skill

- You have a raw podcast transcript and need to identify the strongest marketing angle
- You want to create a cold open that hooks listeners immediately
- You need YouTube titles and thumbnail strategies
- You're creating social clips from podcast material
- You want to create SEO-optimized blog content from the episode
- You want all assets aligned with OpenEd brand identity

---

## Session Startup

At the start of each podcast production session, sync the content database:

```bash
cd "Content/Misc. Utilities/seomachine" && python3 -c "
from dotenv import load_dotenv
load_dotenv('data_sources/config/.env')
from data_sources.modules.webflow import sync_content_database
sync_content_database()
"
```

This pulls latest content from Webflow to `Content/Master Content Database/` for internal linking and context.

---

## THE FOUR CHECKPOINTS

### Checkpoint 1: Comprehensive Analysis (90-120 min)

**Goal**: Understand the episode and identify the strongest themes for marketing.

**Your deliverable**: `Checkpoint_1_Comprehensive_Analysis.md`

**What it contains**:
- 5 Big Ideas (potential marketing angles)
- The TED Talk Version (core insight)
- AI Summary Beats (key narrative moments)
- Chapter Outline (timestamped)
- Surprising Points (contradictions with common belief)
- Quote Bank (organized verbatim quotes)
- Social Clip Highlights (5-6 potential clips)

**User decision point**: Which Big Idea is strongest?

**Reference**: See `references/checkpoint-1-example.md` for detailed example

---

### Checkpoint 2: Cold Opens & Clips (120-150 min)

**Prerequisites**: Checkpoint 1 complete + Big Idea selected

**Goal**: Create one approved cold open script and identify 3 approved social clips with on-screen hooks.

**Your deliverable**: `Checkpoint_2_Cold_Opens_and_Clips.md`

**What it contains**:
- One selected cold open script (22-35 seconds, verbatim clips arranged for narrative momentum)
- On-screen text hooks (2-4 words each for social media captions)
- 3 approved social clips (1:00-1:30 each, full verbatim transcripts)
- Each clip includes: duration, on-screen hook, full transcript, platform recommendations, use case
- Design specifications (font, placement, timing)

**Output format**:
- Cold open: Simple clip sequence with speaker labels and timestamps
- Clips: Verbatim, with complementary on-screen hooks (not redundant)
- Hooks: 2-4 words maximum for mobile readability
- All clips ready to copy/paste directly into production

**Skills used**:
- **video-caption-creation**: For on-screen text hooks and short-form video captions (generates 3-5 hook options per clip)
- **cold-open-creator**: For cold open methodology (optional reference)

**User decision point**: Approve cold open and social clips for Checkpoint 3

**Reference**: See `references/checkpoint-2-example.md` for detailed example

---

### Checkpoint 3: YouTube Strategy (90-120 min)

**Prerequisites**: Checkpoint 2 complete + Cold open selected

**Goal**: Define YouTube title, thumbnail, description, and chapter timestamps.

**Your deliverable**: `Checkpoint_3_YouTube_Strategy.md`

**What it contains**:
- Final YouTube title (with guest name for authority)
- Thumbnail specification (2-4 words max, minimal design)
- YouTube description (opening hook sentence + full description + resources + chapters)
- Cold open script (verbatim clips)
- All 3 approved social clips with on-screen hooks
- Chapter breakdown (5-10 words per chapter title, keyword-rich)

**Skills used**:
- **youtube-title-creator**: For YouTube title strategy
- **opened-identity**: For brand alignment verification

**Output format**:
- Clean, streamlined specifications (no technical jargon)
- Chapter titles follow "My First Million" style (compelling, descriptive)
- Format: `(MM:SS) - Descriptive Chapter Title` (5-10 words max)
- Description: Opening hook + full description + resources + chapters
- Thumbnail: Simple visual + minimal text (2-4 words only)
- All clips ready to copy/paste

**User decision point**: Approve final specifications and move to Checkpoint 4

**Reference**: See `references/checkpoint-3-example.md` for detailed example

---

### Checkpoint 4: Polished Transcript & Blog Post (120-180 min)

**Prerequisites**: Checkpoint 3 complete + All selections locked

**Goal**: Create publication-ready transcript and SEO-optimized blog post.

**Your deliverables**:
- `[Guest]_YouTube_and_Show_Notes.md` (refined from Checkpoint 3)
- `[Guest]_Polished_Transcript.md` (new, contains transcript + blog)

**What it contains**:
- Full polished transcript (cleaned for readability)
- Embedded blog post (~1,000 words) focused on core insight
- Guest bio and resource links
- SEO headers and structure

**Skills used**:
- **transcript-polisher**: For transcript cleanup and formatting
- **podcast-blog-post-creator**: For narrative-driven blog post creation in Ela's voice

**Output structure**:
1. `[Guest]_YouTube_and_Show_Notes.md` — Handoff file for video production (title, thumbnail, cold open, show notes, timestamps)
2. `[Guest]_Polished_Transcript.md` — Publication-ready transcript with embedded blog post

**Reference**: See `references/checkpoint-4-example.md` for detailed example

---

## WORKFLOW TIMELINE & FILE STRUCTURE

| Phase | Duration | Input | Output File | Your Action |
|-------|----------|-------|------|---|
| **Setup** | 10 min | Raw materials | `[Guest]_Source_Material.md` | Provide feedback on context/notes |
| **Checkpoint 1** | 90-120 min | Source material | `Checkpoint_1_Comprehensive_Analysis.md` | Select Big Idea to pursue |
| **Checkpoint 2** | 120-150 min | Checkpoint 1 approved | `Checkpoint_2_Cold_Opens_and_Clips.md` | Approve cold open & clips |
| **Checkpoint 3** | 90-120 min | Checkpoint 2 approved | `Checkpoint_3_YouTube_Strategy.md` | Approve title/thumbnail/chapters |
| **Checkpoint 4** | 120-180 min | Checkpoint 3 approved | `Checkpoint_4_Polished_Transcript_and_Blog.md` | Review & publish |
| **TOTAL** | **6-8 hours** | Raw transcript | All publication-ready assets | 5 decision points |

---

## KEY PRINCIPLES

### Verbatim Only
All quoted transcript must be exactly as spoken. You can cut/rearrange, never paraphrase.

### Mine the Entire Transcript
Don't limit analysis to one section. The strongest angle might be anywhere.

### Bold Over Safe
Surprising, contrarian moments beat safe, obvious observations.

### Story Over Summary
Create narrative momentum. Clips should have complete arcs, not just be "good quotes."

### Simple Over Complex
- Thumbnails: 3 elements max
- Titles: One clear idea
- Clips: Clear beginning, middle, end

### Brand Aligned
All outputs reflect OpenEd visual and tonal guidelines. Homeschool parents should see themselves.

---

## SKILL DEPENDENCIES & WHERE TO USE THEM

### Checkpoint 1 Dependencies
- **No specific skills required** — This is pure analysis work

### Checkpoint 2 Dependencies
**Cold Open Creation**:
- Use: [cold-open-creator SKILL](../cold-open-creator/SKILL.md)
- Why: Methodology for identifying scenes, arranging clips, testing against quality gates

**Caption Suggestions**:
- Use: [video-caption-creation SKILL](../video-caption-creation/SKILL.md)
- Why: Guidelines for on-screen text, platform-specific captions, engagement tactics

### Checkpoint 3 Dependencies
**YouTube Titles & Thumbnails**:
- Use: [youtube-title-creator SKILL](../youtube-title-creator/SKILL.md)
- Why: Title + thumbnail synergy, search optimization, design strategy

**Brand Alignment**:
- Use: [opened-identity SKILL](../opened-identity/SKILL.md)
- Why: Verify messaging aligns with OpenEd mission, values, and audience understanding

### Checkpoint 4 Dependencies
**Transcript Polish**:
- Use: [transcript-polisher SKILL](../transcript-polisher/SKILL.md)
- Why: Clean, readable transcript formatting for blog post integration

**Blog Post Creation**:
- Use: [podcast-blog-post-creator SKILL](../podcast-blog-post-creator/SKILL.md)
- Why: Narrative-driven blog post in Ela's voice; SEO optimization; guest representation

**Day-in-the-Life Post** (Optional):
- Use: [day-in-the-life SKILL](../day-in-the-life/SKILL.md)
- Why: When guest describes their daily/weekly homeschool structure in detail
- Creates: Personal narrative (~800-1,200 words) + tool inventory for practical takeaways

**Verified Reviews** (Optional):
- Use: [verified-review SKILL](../verified-review/SKILL.md)
- Why: When guest mentions specific curricula, tools, or products they use
- Creates: Structured reviews (300-500 words each) with real parent attribution

---

## QUALITY GATES (At Each Decision Point)

### Before Checkpoint 1 → Checkpoint 2:
**Is the analysis complete?**
- ✅ All 5 Big Ideas clearly differentiate from each other?
- ✅ One Big Idea is "the obvious choice" for marketing?
- ✅ Have you mined the entire transcript (not just first/last sections)?
- ✅ Quote bank is organized by theme?
- ✅ Chapter outline matches actual content?

### Before Checkpoint 2 → Checkpoint 3:
**Does the cold open work?**
- ✅ Passes 4 out of 5 quality tests? (Stranger, Itch, Stakes, Tease, Emotion)
- ✅ Ends with unresolved cliffhanger (doesn't answer the question)?
- ✅ All clips are verbatim (no paraphrasing)?
- ✅ Duration is 22-35 seconds?
- ✅ Social clips have distinct angles (not all making same point)?
- ✅ On-screen hooks are 2-4 words max?

### Before Checkpoint 3 → Checkpoint 4:
**Is the strategy aligned?**
- ✅ YouTube title clearly communicates core finding?
- ✅ Title includes guest name for authority?
- ✅ Thumbnail is simple (2-4 words only)?
- ✅ Thumbnail visual is complementary (not redundant with title)?
- ✅ Description hook is compelling (1 sentence)?
- ✅ Chapter titles are 5-10 words (keyword-rich, compelling)?
- ✅ All resources/links are correct?
- ✅ Aligned with OpenEd brand?

### Before Checkpoint 4 → Publication:
**Are final assets publication-ready?**
- ✅ Transcript is clean and readable?
- ✅ Blog post is ~1,000 words with clear narrative arc?
- ✅ All quotes are verbatim with proper attribution?
- ✅ Guest bio includes credentials and links?
- ✅ SEO headers present and optimized?
- ✅ Tone is conversational (sounds like Ela, not formal)?
- ✅ Ready for blog publishing?
- ✅ Social clips ready to post with on-screen hooks?

---

## COMMON MISTAKES TO AVOID

- ❌ Using only one section of transcript (mine the entire episode)
- ❌ Paraphrasing quotes (all quotes must be verbatim)
- ❌ Creating complex thumbnails (keep to 3 elements max)
- ❌ Choosing the "safe" angle instead of the surprising one
- ❌ Making cold open too long (25-35 seconds max)
- ❌ Resolving the cliffhanger (always cut before the answer)
- ❌ Skipping quality gates (get approval before each phase)
- ❌ Making blog post too long or too short (target ~1,000 words)
- ❌ Burying guest credentials (introduce early and naturally)
- ❌ Writing blog post in formal tone (write like Ela is talking to you)

---

## FILE STRUCTURE & DELIVERABLES

### Source Material Phase
**`[Guest]_Source_Material.md`**
- Raw transcript (rough or cleaned)
- Guest background/context
- Episode links and resources
- Notes on tone, highlights, structure

### Checkpoint 1 Output
**`Checkpoint_1_Comprehensive_Analysis.md`**
- 5 Big Ideas (potential marketing angles)
- TED Talk Version (core insight)
- Chapter outline with timestamps
- Quote bank (organized by theme)
- Surprising points
- Social clip highlights
📌 **You provide feedback**: Which Big Idea is strongest?

### Checkpoint 2 Output
**`Checkpoint_2_Cold_Opens_and_Clips.md`**
- One approved cold open script (22-35 seconds)
- On-screen text hooks (2-4 words each)
- 3 approved social clips (1:00-1:30 each)
- Design specifications
- Platform recommendations
📌 **You provide feedback**: Approve cold open and clips, suggest on-screen hook edits

### Checkpoint 3 Output
**`Checkpoint_3_YouTube_Strategy.md`**
- YouTube title (with guest name)
- Thumbnail specification (visual + 2-4 words)
- YouTube description (hook + full description + resources)
- Chapter breakdown (5-10 words per chapter, keyword-rich)
- Cold open script (final)
- All 3 social clips (with final on-screen hooks)
📌 **You provide feedback**: Approve title/thumbnail/chapters

### Checkpoint 4 Output (Final Deliverables)
**`Checkpoint_4_Polished_Transcript_and_Blog.md`**
- Full polished transcript (cleaned for readability)
- ~1,000 word blog post (in Ela's voice)
- Guest bio with credentials and links
- SEO headers and structure
📌 **You provide feedback**: Review for publication

### Ready for Distribution
- YouTube: Upload video with Checkpoint 3 specs (title, thumbnail, description, chapters)
- Blog: Publish Checkpoint 4 content
- Social: Share Checkpoint 2 clips with on-screen hooks
- Newsletter: Promote with Checkpoint 4 blog excerpt

---

## REFERENCES

For detailed instructions and examples, see:
- `references/checkpoint-1-example.md` — Complete Checkpoint 1 example
- `references/checkpoint-2-example.md` — Complete Checkpoint 2 example
- `references/checkpoint-3-example.md` — Complete Checkpoint 3 example (YouTube specifications format)
- `references/checkpoint-4-example.md` — Complete Checkpoint 4 example (Polished transcript + blog post)

---

## RELATED SKILLS

- **[cold-open-creator](../cold-open-creator/SKILL.md)**: Scene selection, clip arrangement, quality testing
- **[video-caption-creation](../video-caption-creation/SKILL.md)**: Caption/overlay suggestions for clips
- **[youtube-title-creator](../youtube-title-creator/SKILL.md)**: YouTube title and thumbnail strategy
- **[podcast-blog-post-creator](../podcast-blog-post-creator/SKILL.md)**: SEO-optimized blog post in Ela's voice
- **[transcript-polisher](../transcript-polisher/SKILL.md)**: Polish raw transcript for readability
- **[opened-identity](../opened-identity/SKILL.md)**: Brand alignment verification
- **[day-in-the-life](../day-in-the-life/SKILL.md)**: Day-in-the-Life blog posts with tool inventory
- **[verified-review](../verified-review/SKILL.md)**: Structured product/curriculum reviews

---

## SUCCESS METRICS

**For YouTube Performance**:
- CTR: Title + thumbnail is compelling (>6% for ADHD/education content)
- Retention: Cold open hooks in first 5 seconds
- Conversion: Viewers finish episode

**For Blog Performance**:
- SEO: Post ranks for homeschooling-specific keywords
- Engagement: Readers make it to guest bio/links
- Sharing: Post is shareable (format, length, voice)

**For Social Performance**:
- Shareability: Clips standalone compelling
- Captions: Text makes sense without audio
- Platform fit: Clips work on target platforms

**For Overall Strategy**:
- Alignment: All assets reinforce same theme
- Brand consistency: Recognizable across formats
- Topic clarity: Viewers immediately understand episode topic
- Asset completeness: All deliverables ready for team handoff
