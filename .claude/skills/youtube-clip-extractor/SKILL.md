---
name: youtube-clip-extractor
description: Download YouTube videos, identify compelling clips from transcripts, cut clips with ffmpeg, and generate platform-optimized on-screen text and captions. Complete workflow from URL to publishable clips.
---

# YouTube Clip Extractor

## Overview

This skill downloads YouTube videos, analyzes transcripts for compelling clip moments, extracts clips using ffmpeg, and generates platform-ready on-screen text and captions. It integrates with the existing caption and social content skills to deliver complete, publishable assets.

## When to Use This Skill

- You have a YouTube URL and want to extract the best clips
- You want automated clip identification based on hook/coda criteria
- You need clips cut and ready for Descript or other editors
- You want on-screen text hooks and platform-specific captions for each clip

**Do NOT use for:**
- Full podcast production workflow (use `podcast-production` skill instead)
- Text-only social posts (use `social-content-creation` skill)
- Already-downloaded videos (skip to Phase 2)

---

## Prerequisites

### Required Tools (install via Homebrew)

```bash
brew install yt-dlp ffmpeg
```

### File Location

All downloads go to: `Content/YouTube Transcripts/`

Structure:
```
Content/YouTube Transcripts/
├── {video_id}.mp4              # Full video (H.264 encoded)
├── {video_id}.en.vtt           # Timestamped subtitles
└── clips/
    └── {video_id}/
        ├── clip_01_{name}.mp4  # Individual clips
        ├── clip_02_{name}.mp4
        └── {video_id}_Clip_Assets.md  # Captions & hooks
```

---

## The 4-Phase Workflow

### Phase 1: Download Video & Transcript

**Goal:** Get video and subtitles from YouTube URL

#### Step 1: Download with H.264 Encoding

Use H.264 format for Descript compatibility (NOT AV1):

```bash
# Download video in H.264 format (Descript-compatible)
yt-dlp -f "bestvideo[vcodec^=avc]+bestaudio[ext=m4a]/best[vcodec^=avc]" \
  --merge-output-format mp4 \
  -o "Content/YouTube Transcripts/{video_id}.mp4" \
  "YOUTUBE_URL"

# If H.264 unavailable, download best quality then re-encode:
yt-dlp -f "bestvideo+bestaudio" --merge-output-format mp4 \
  -o "Content/YouTube Transcripts/{video_id}_temp.mp4" \
  "YOUTUBE_URL"

# Re-encode to H.264 for Descript compatibility
ffmpeg -i "{video_id}_temp.mp4" -c:v libx264 -preset fast -crf 22 \
  -c:a aac -b:a 128k "{video_id}.mp4"
```

#### Step 2: Download Subtitles

```bash
yt-dlp --write-auto-sub --sub-lang en --skip-download \
  -o "Content/YouTube Transcripts/{video_id}.%(ext)s" \
  "YOUTUBE_URL"
```

#### Phase 1 Output:
- `{video_id}.mp4` — Full video (H.264)
- `{video_id}.en.vtt` — Timestamped subtitles

---

### Phase 2: Analyze Transcript for Clips

**Goal:** Identify 5-8 compelling clip moments with strong hooks and codas

#### Clip Selection Criteria

**A good clip has:**

1. **Strong Hook (First 3 Seconds)**
   - Polarizing statement ("Your kid's addiction is actually genius")
   - Counter-intuitive reveal ("My son's first job sucked. Perfect.")
   - Direct challenge ("Never give up on the weird kid")
   - Curiosity gap ("Then everything changed...")

2. **Complete Arc (30-90 seconds)**
   - Clear beginning, middle, end
   - Not just a "good quote" — a complete thought
   - Setup → Tension → Resolution OR Setup → Tension → Cliffhanger

3. **Stakes**
   - Why does this matter?
   - Who cares?
   - What's at risk?

4. **Strong Coda/Ending**
   - Insight or surprising conclusion
   - Cuts right before the answer (cliffhanger)
   - Quotable final line

#### Scan Transcript For:

**Inflection Points:**
- "Then everything changed..."
- "I realized..."
- "That's when I knew..."
- "The moment I..."

**Vulnerability Moments:**
- Personal stakes, failures, struggles
- "I was terrified..."
- "I almost gave up..."
- "Nobody believed..."

**Contradiction Moments:**
- "We thought X but actually..."
- "Everyone says... but the truth is..."
- "The opposite happened..."

**Surprising Insights:**
- Research, data, unexpected findings
- Counter-intuitive conclusions
- "What we found was..."

**Character in Action:**
- Showing, not telling
- Doing, not describing
- Specific moments, not abstractions

#### Quality Tests (Pass 4/5):

- [ ] **Stranger Test:** Would someone with zero context care?
- [ ] **Itch Test:** Creates need to know more?
- [ ] **Stakes Test:** Clear why it matters?
- [ ] **Tease Test:** Hints without giving away?
- [ ] **Emotion Test:** Feel something in first 5 seconds?

#### Phase 2 Output Format:

Create analysis document with clip recommendations:

```markdown
# {Video Title} - Clip Analysis

## Video Details
- **URL:** [YouTube URL]
- **Duration:** [Total length]
- **Speaker(s):** [Names]
- **Topic:** [Primary subject]

---

## Recommended Clips

### CLIP 1: "{Descriptive Name}"
**Timestamp:** `MM:SS - MM:SS` (XX seconds)
**Hook:** [First line or opening moment]
**Arc:** [Setup → Middle → Ending summary]
**Coda:** [How it ends / final line]

**Key Quotes:**
- "[Verbatim quote 1]"
- "[Verbatim quote 2]"
- "[Verbatim quote 3]"

**Quality Tests:** Stranger ✅ | Itch ✅ | Stakes ✅ | Tease ✅ | Emotion ✅
**Why It Works:** [1-2 sentence rationale]
**Priority:** HIGH / MEDIUM / LOW

---

### CLIP 2: "{Descriptive Name}"
[Repeat structure...]

---

## Summary Table

| # | Clip Name | Timestamp | Length | Hook | Coda | Priority |
|---|-----------|-----------|--------|------|------|----------|
| 1 | [Name] | MM:SS-MM:SS | XXs | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | HIGH |
| 2 | [Name] | MM:SS-MM:SS | XXs | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | HIGH |
| 3 | [Name] | MM:SS-MM:SS | XXs | ⭐⭐⭐ | ⭐⭐⭐⭐ | MEDIUM |
```

---

### Phase 3: Cut Clips with FFmpeg

**Goal:** Extract approved clips as separate video files

#### Cutting Commands

**Basic clip extraction (fast, uses keyframes):**
```bash
ffmpeg -i "{video_id}.mp4" -ss MM:SS -to MM:SS -c copy \
  "clips/{video_id}/clip_01_{name}.mp4"
```

**Precise cutting with re-encoding (slower but frame-accurate):**
```bash
ffmpeg -ss MM:SS -i "{video_id}.mp4" -t DURATION \
  -c:v libx264 -preset fast -crf 22 -c:a aac -b:a 128k \
  "clips/{video_id}/clip_01_{name}.mp4"
```

**Notes:**
- `-ss` before `-i` = faster seeking (recommended)
- `-c copy` = no re-encoding (fast but may have keyframe issues)
- `-c:v libx264` = re-encode to H.264 (slower but precise)
- Use H.264 output for Descript compatibility

#### Batch Cutting Example

```bash
# Create clips directory
mkdir -p "Content/YouTube Transcripts/clips/{video_id}"

# Cut each clip
ffmpeg -i "{video_id}.mp4" -ss 06:59 -to 08:10 -c copy "clips/{video_id}/clip_01_covid_revelation.mp4"
ffmpeg -i "{video_id}.mp4" -ss 20:50 -to 21:54 -c copy "clips/{video_id}/clip_02_whiteboard_teen.mp4"
ffmpeg -i "{video_id}.mp4" -ss 25:00 -to 26:10 -c copy "clips/{video_id}/clip_03_college_loans.mp4"
```

#### Phase 3 Output:
- Individual MP4 files for each clip
- All files in `clips/{video_id}/` directory
- H.264 encoded for Descript compatibility

---

### Phase 4: Generate On-Screen Text & Captions

**Goal:** Create platform-optimized hooks and captions for each clip

**This phase uses the `video-caption-creation` skill methodology.**

#### For Each Clip, Generate:

**1. On-Screen Text Hook (3-5 options)**

The text that appears in the first 3 seconds of the video. Must be:
- 2-4 words maximum (mobile readable)
- Stops the scroll
- Passes McDonald's Test (accessible language)
- Complements (not duplicates) audio

**Hook Categories:**
- **Polarizing:** "Your kid's [negative] is actually genius"
- **Counter-Intuitive:** "My son's first job sucked. Perfect."
- **Direct Challenge:** "Never give up on the weird kid"
- **Curiosity Gap:** "Then everything changed..."

**2. Platform-Specific Captions**

| Platform | On-Screen Text | Caption Style | Hashtags |
|----------|---------------|---------------|----------|
| Instagram | Same | Short, emoji OK, accessible | 5-10 |
| TikTok | Same | Short, emoji OK, accessible | 3-5 |
| YouTube Shorts | Same | Short, minimal emoji | 3-5 + #Shorts |
| Facebook | Same | Slightly longer, conversational, NO external links | 0-2 |

**Facebook Difference:** Caption can be longer and more conversational. NO hashtags or external links (kills reach).

**3. Algorithm Optimization**

Per the Triple Word Score system:
- **Audio:** Topic words spoken in first 10 seconds
- **On-Screen Text:** Reinforces (not competes with) audio
- **Caption:** Topic-relevant keywords in first sentence
- **Hashtags:** Broad → Mid → Specific → Niche (10-12 total)

#### Phase 4 Output Format:

Create file: `clips/{video_id}/{video_id}_Clip_Assets.md`

```markdown
# {Video Title} - Clip Assets

## CLIP 1: "{Descriptive Name}"

### Video Details
- **File:** `clip_01_{name}.mp4`
- **Duration:** XX seconds
- **Core Message:** [1 sentence]
- **Speaker:** [Name]

---

### On-Screen Text Options (Choose 1)

**Option 1:** Your kid's Minecraft addiction is genius
- **Category:** Polarizing Statement
- **Recommended for:** All platforms

**Option 2:** Schools got this wrong
- **Category:** Direct Challenge
- **Recommended for:** TikTok, Reels

**Option 3:** What COVID revealed about learning
- **Category:** Curiosity Gap
- **Recommended for:** YouTube Shorts

**RECOMMENDED:** Option 1 (strongest hook, broadest appeal)

---

### Platform Captions

#### Instagram / TikTok / YouTube Shorts
[Same caption for all three]

Your kid's Minecraft addiction might be smarter than school 🎮

The conveyor belt wasn't doing the heavy lifting. COVID proved it.

#Education #Homeschool #Parenting #AlternativeEducation #OpenEducation

---

#### Facebook
[Slightly different - longer, conversational, NO hashtags]

Your kid's Minecraft addiction might be smarter than school.

COVID forced families home—and something unexpected happened. Parents realized their kids weren't falling behind. They were thriving. The conveyor belt education system wasn't doing the heavy lifting after all.

What did you discover during COVID about how your kids actually learn?

---

### Algorithm Optimization

**Topic Keywords (spoken in first 10 seconds):**
education, school, learning, COVID, kids, homeschool

**Hashtag Set (10-12 total):**
- Broad: #Education #Parenting
- Mid: #Homeschool #AlternativeEducation #LearningDifferences
- Specific: #Homeschooling #Unschooling #OpenEducation
- Niche: #HomeschoolLife #HomeschoolMom
- Platform: #Shorts (YouTube only)

---

## CLIP 2: "{Descriptive Name}"
[Repeat structure...]
```

---

## Complete Workflow Example

```bash
# PHASE 1: Download
yt-dlp -f "bestvideo[vcodec^=avc]+bestaudio" --merge-output-format mp4 \
  -o "Content/YouTube Transcripts/cvGtVmI4jTQ.mp4" \
  "https://www.youtube.com/watch?v=cvGtVmI4jTQ"

yt-dlp --write-auto-sub --sub-lang en --skip-download \
  -o "Content/YouTube Transcripts/cvGtVmI4jTQ.%(ext)s" \
  "https://www.youtube.com/watch?v=cvGtVmI4jTQ"

# PHASE 2: Analyze transcript (manual review)
# Read VTT file, identify clips using criteria above

# PHASE 3: Cut clips
mkdir -p "Content/YouTube Transcripts/clips/cvGtVmI4jTQ"
ffmpeg -i "cvGtVmI4jTQ.mp4" -ss 06:59 -to 08:10 \
  -c:v libx264 -preset fast -crf 22 -c:a aac \
  "clips/cvGtVmI4jTQ/clip_01_covid_revelation.mp4"

# PHASE 4: Generate assets (create markdown file with hooks/captions)
```

---

## Related Skills

This skill integrates with:

| Skill | When to Use | What It Provides |
|-------|-------------|------------------|
| **video-caption-creation** | Phase 4 | On-screen text hook categories, Triple Word Score system, platform caption guidelines |
| **hook-and-headline-writing** | Phase 4 | 15 hook formulas, 4 U's test, sticky sentence techniques |
| **social-content-creation** | After clips ready | Framework fitting for text posts about clips |
| **podcast-production** | Full episode workflow | Complete 4-checkpoint production system |

### Skill Cross-References

**From video-caption-creation:**
- Hook categories (Polarizing, Counter-Intuitive, Direct Challenge, Curiosity Gap)
- Triple Word Score system (Audio + On-Screen + Caption + Hashtags)
- Platform-specific hashtag counts
- McDonald's Test for accessibility

**From hook-and-headline-writing:**
- 15 headline formulas
- 4 U's test (Useful, Urgent, Unique, Ultra-specific)
- Sticky sentence techniques (alliteration, symmetry, contrast)
- 10 Commandments of engagement

**From social-content-creation:**
- Platform voice guidelines (LinkedIn vs Facebook vs Instagram)
- Framework fitting method
- SCAMPER proliferation for variations

---

## Common Mistakes to Avoid

### Download Issues
- ❌ Downloading AV1 codec (Descript can't import)
- ❌ Not re-encoding to H.264 when needed
- ❌ Forgetting to download subtitles

### Clip Selection Issues
- ❌ Choosing "good quotes" instead of complete arcs
- ❌ Clips too long (>90 seconds) or too short (<30 seconds)
- ❌ No clear hook in first 3 seconds
- ❌ Giving away the punchline in the hook

### Cutting Issues
- ❌ Cutting at non-keyframes (use re-encode for precision)
- ❌ Starting mid-sentence
- ❌ Ending before natural conclusion

### Caption Issues
- ❌ On-screen text too long (>4 words)
- ❌ Same caption for Facebook as other platforms
- ❌ External links in Facebook caption
- ❌ Hashtags in Facebook caption

---

## Quality Checklist

Before delivering clips:

**Video Files:**
- [ ] All clips are H.264 encoded
- [ ] Each clip is 30-90 seconds
- [ ] Audio and video are synced
- [ ] Clean start/end points (no mid-word cuts)

**Clip Selection:**
- [ ] Each clip passes 4/5 quality tests
- [ ] Strong hook in first 3 seconds
- [ ] Complete arc (not just a quote)
- [ ] Clear stakes (why it matters)

**Captions & Hooks:**
- [ ] 3-5 on-screen text options per clip
- [ ] On-screen text is 2-4 words max
- [ ] Platform-specific captions created
- [ ] Facebook caption is different (longer, no hashtags)
- [ ] Hashtag strategy spans broad to niche

---

## Version History

- **v1.0** (2025-12-02): Initial skill creation
  - 4-phase workflow: Download → Analyze → Cut → Caption
  - Integration with video-caption-creation skill
  - H.264 encoding for Descript compatibility
  - Platform-specific caption guidelines
  - Quality tests from podcast-production skill
