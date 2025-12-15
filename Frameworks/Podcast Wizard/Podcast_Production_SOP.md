# OpenEd Podcast Production SOP

Complete workflow for transforming raw podcast recordings into polished YouTube episodes, blog posts, and social media assets.

---

## Overview

This SOP covers the end-to-end podcast production process:

1. **Phase 1: Riverside & Descript Setup** - Download, import, transcribe
2. **Phase 2: Preliminary AI Analysis** - Editing notes and mic drop moments
3. **Phase 3: Claude Code Workflow** - 4-checkpoint content creation system
4. **Phase 4: Descript Editing** - Intro/outro, multi-cam, polish
5. **Phase 5: Show Notes & Assets** - Clips, thumbnails, titles
6. **Phase 6: Export & Publish** - Final delivery

---

## Phase 1: Riverside & Descript Setup

### 1.1 Download from Riverside

1. Log into Riverside.fm
2. Navigate to the recording session
3. Download: **High-quality aligned video tracks**
4. Download the transcript file

### 1.2 Create Descript Project

1. Open Descript
2. Navigate to the Open Ed podcast folder
3. Create a new **video project**
4. Name format: `00X - [Guest Name]` (e.g., "005 - Andrea Fife")
5. Go to Project and drag audio/video files into the project

### 1.3 Create Sequence and Transcribe

1. Highlight both tracks
2. Click **Create Sequence**
3. Drag the sequence into the script area for transcription
4. Name speakers when prompted:
   - Host: "Ela" (or host name)
   - Guest: "[First] [Last Name]" (use full name for guests)
5. Wait for transcription to complete

### 1.4 Apply Studio Sound

1. Select the entire sequence
2. Go to **Underlord > Studio Sound**
3. Set intensity to **80%**
4. Apply to whole sequence

### 1.5 Apply Multi-Cam

1. Go to **Underlord > Automatic multi-cam**
2. Select "Show active speaker only"
3. Submit

---

## Phase 2: Preliminary AI Analysis

### 2.1 Export Transcript

1. In Descript: **Publish > Export transcript > Copy to clipboard**
2. Save a copy in Notion under "Rough Transcript" header

### 2.2 Set Up Notion Entry

Create a new Notion page for the episode with these sections:

```
# [Guest Name] - Episode [Number]

## Transcript
### Rough Transcript
[Paste exported transcript here]

### Polished Transcript
[Will be filled later from Checkpoint 4]

## Chapters
[Will be filled from Descript/Claude]

## Mic Drop Moments
[AI-identified standout quotes]

## Assets
- Clips
- Thumbnails
- Show notes
```

### 2.3 Run Editing Analysis

Paste transcript into Claude and run the editing prompt:

```
Do the first podcast editing role looking for things to cut out or edit
```

This identifies:
- Sections to cut (timestamps provided)
- Technical issues
- Off-topic tangents
- False starts

Review the timestamps and apply cuts in Descript.

### 2.4 Identify Mic Drop Moments

In the same Claude session:

```
Identify 5 cold open ideas
```

Copy the mic drop moments to Notion. Highlight your top pick for the cold open.

---

## Phase 3: Claude Code Workflow

### 3.1 Prepare Source Material

1. Create folder: `/Content/Open Ed Podcasts/[Guest Name]/`
2. Create `[Guest]_Source_Material.md` containing:
   - Full transcript (copy from Descript)
   - Guest background/credentials
   - Episode context and recording notes
   - Links or resources mentioned
   - Notes on standout moments

### 3.2 Run the Podcast Production Skill

Open Claude Code and invoke the skill:

```
/skill podcast-production
```

**[INSERT SKILL: podcast-production]**

---

### 3.3 Checkpoint 1: Comprehensive Analysis

**Output**: `Checkpoint_1_Comprehensive_Analysis.md`

**What Claude Produces**:
- 5 Big Ideas (potential marketing angles)
- The TED Talk Version (core insight)
- Chapter Outline with timestamps
- Quote Bank organized by theme
- Surprising Points
- Social Clip Highlights (5-6 potential clips)

**Your Action**: Review and select the strongest Big Idea for marketing.

---

### 3.4 Checkpoint 2: Cold Opens and Clips

**Output**: `Checkpoint_2_Cold_Opens_and_Clips.md`

**Skill Dependencies**:

**[INSERT SKILL: cold-open-creator]**

**[INSERT SKILL: video-caption-creation]**

**What Claude Produces**:
- Cold open script (22-35 seconds, verbatim clips)
- On-screen text hooks (2-4 words each)
- 3-5 social clips with full transcripts
- Timestamps for finding clips in Descript
- Platform recommendations

**Your Action**: Approve cold open and clips, or request revisions.

---

### 3.5 Checkpoint 3: YouTube Strategy

**Output**: `Checkpoint_3_YouTube_Strategy.md`

**Skill Dependencies**:

**[INSERT SKILL: youtube-title-creator]**

**[INSERT SKILL: opened-identity]**

**What Claude Produces**:
- YouTube title (with guest name)
- Thumbnail specification (2-4 words)
- YouTube description (hook + full description + resources)
- Chapter breakdown (5-10 words per chapter)
- Final cold open script
- All social clips with hooks

**Your Action**: Approve title/thumbnail/chapters.

---

### 3.6 Checkpoint 4: Final Content

**Output**: `Checkpoint_4_Final_Content.md`

**Skill Dependencies**:

**[INSERT SKILL: transcript-polisher]**

**[INSERT SKILL: podcast-blog-post-creator 2]**

**[INSERT SKILL: day-in-the-life]** (when applicable)

**[INSERT SKILL: verified-review]** (when applicable)

**[INSERT SKILL: ghostwriter]**

**What Claude Produces**:
- Full polished transcript with section headers
- ~1,000 word blog post (in Ela's voice)
- Technical editing notes (cuts, glitches)
- Optional: Day-in-the-Life post
- Optional: Verified Reviews

**Your Action**: Review for publication. Note technical editing instructions.

---

## Phase 4: Descript Editing

### 4.1 Cut the Beginning

1. Ensure podcast starts with "Welcome back to the Open Ed Podcast"
2. Cut any pre-roll conversation or setup

### 4.2 Insert Intro Scene

1. Find the cold open clip (use timestamp or search keywords)
2. Insert a new scene at the beginning using "/" in the transcript
3. Paste the cold open clip into this new scene
4. Add a **gap clip** after the intro (about 7.5-10 seconds) using "/"
5. Go to **Scene > Layouts** and apply "Open Ed Instagram Reel" > "In this episode" template
6. Adjust timing so talking begins as music fades out
7. Ensure correct speaker shows in intro (adjust in Scene Layers if needed)

### 4.3 Insert Outro

1. Apply same process to outro
2. Add gap clip at the end
3. Extend for proper fade-out

### 4.4 Shorten Word Gaps

1. Go to **Underlord > Shorten word gaps**
2. Set to find gaps of **2 seconds or longer**
3. Review suggestions and decide what to keep/remove
4. Gaps of 1 second are generally fine to leave

### 4.5 Apply Technical Cuts

Using editing notes from Checkpoint 4:

1. Find flagged timestamps
2. Delete:
   - Pop-up notifications
   - Audio glitches
   - Long pauses
   - Technical tangents
3. Review cuts for smooth transitions

### 4.6 Add Chapters (Scene Dividers)

1. Go to **Underlord > Add chapters**
2. Copy timestamps to Notion
3. Or: Manually add scene dividers at chapter timestamps from Checkpoint 3
4. Name each scene with the chapter title
5. Scene dividers become YouTube chapters on export

### 4.7 Add Zoom Effects (Optional)

For emphasis on key moments:

1. Select clip section
2. Add zoom keyframe (110-120% zoom)
3. Duration: 2-5 seconds
4. Use sparingly: 3-5 zooms per 10 minutes max

### 4.8 Add Transitions

1. At cold open cuts: Add "whoosh" transition
2. Between sections: Subtle cross-dissolve (if needed)
3. Keep minimal

---

## Phase 5: Show Notes & Assets

### 5.1 Clip Creation

For each approved clip from Checkpoint 2:

1. Find timestamp in main composition
2. Select the clip range
3. Create new composition from selection
4. Edit/rearrange as needed
5. Generate caption (using Descript)
6. Apply social template:
   - Go to **Layouts**
   - Choose "Open Ed Instagram Reel" or appropriate template
   - Adjust for 9:16 vertical format
7. Add on-screen text hook (from Checkpoint 2):
   - 2-4 words max
   - Lower 1/3 of frame
   - Semi-transparent background
   - First 3-5 seconds, then fade

### 5.2 Create Notion Entry for Clip

1. Create new entry in Content Database
2. Put caption in title (if short)
3. Add Descript URL or exported file

### 5.3 Thumbnails & Title

1. Return to Claude with the transcript
2. Ask: "What questions does this podcast answer?"
3. Generate title ideas based on response
4. Generate thumbnail concepts based on title
5. Create thumbnails (2-4 words, simple design, 3 elements max)

### 5.4 Show Notes

1. Paste edited transcript into Claude
2. Ask to generate show notes based on title with teaser-chapters
3. Aim for 6-7 chapters for a 45-minute episode
4. Copy all assets to Notion card for the episode

---

## Phase 6: Export & Publish

### 6.1 Export Full Episode

1. Select full episode composition
2. Export settings:
   - Format: MP4 (H.264)
   - Resolution: 1080p minimum (4K if available)
   - Audio: AAC, 256kbps
3. Chapters export automatically from scene dividers

### 6.2 Export Social Clips

For each clip composition:

1. Export settings:
   - Format: MP4
   - Resolution: 1080x1920 (9:16 vertical)
   - Frame rate: 30fps
2. Name: `[Guest]_[Platform]_[ClipName].mp4`

### 6.3 YouTube Upload

- Video file
- Title from Checkpoint 3
- Description from Checkpoint 3 (with links)
- Thumbnail per Checkpoint 3 specs
- Chapters (verify from scene dividers)
- Tags, playlist, end screen, cards

### 6.4 Blog Post

- Format Checkpoint 4 blog post for CMS
- Include guest bio with links
- Add YouTube embed
- Set featured image
- Publish

### 6.5 Social Media

- Post clips across platforms (Instagram Reels, YouTube Shorts, TikTok, LinkedIn)
- Use on-screen hooks from Checkpoint 2
- Verify captions

### 6.6 Notion Update

- Mark episode as published
- Add YouTube link
- Add blog post link
- Archive all assets

---

## Troubleshooting

### Transcript Sync Issues

If Descript transcript drifts:
1. Find drift point
2. Split transcript
3. Manually realign
4. Or: Re-import fresh

### Audio Quality

If Studio Sound isn't enough:
1. Check source levels
2. Apply additional noise reduction
3. Consider re-recording intro/outro

### Claude Issues

If outputs don't match expectations:
1. Provide specific feedback in checkpoint file
2. Reference timestamps or quotes
3. Break complex requests into smaller asks

---

## File Structure Reference

### Per Episode

```
/Content/Open Ed Podcasts/[Guest Name]/
├── [Guest]_Source_Material.md
├── Checkpoint_1_Comprehensive_Analysis.md
├── Checkpoint_2_Cold_Opens_and_Clips.md
├── Checkpoint_3_YouTube_Strategy.md
└── Checkpoint_4_Final_Content.md
```

### Descript Project

```
[Guest Name] - OpenEd Podcast/
├── Main Timeline (full episode)
├── Cold Open (composition)
├── Clip 1 - [Hook]
├── Clip 2 - [Hook]
├── Clip 3 - [Hook]
└── [Additional clips]
```

### Skills Reference

| Checkpoint | Skills Used |
|------------|-------------|
| Checkpoint 1 | None (pure analysis) |
| Checkpoint 2 | cold-open-creator, video-caption-creation |
| Checkpoint 3 | youtube-title-creator, opened-identity |
| Checkpoint 4 | transcript-polisher, podcast-blog-post-creator, ghostwriter, day-in-the-life (optional), verified-review (optional) |

---

## Credentials

| Service | Login | Password |
|---------|-------|----------|
| Riverside.fm | market@mytechhigh.com | cup3AQU_edu-dxa6kgp |
