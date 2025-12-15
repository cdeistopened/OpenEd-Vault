# SEO Content Writer

Write SEO-optimized hub pages and blog content for OpenEd (homeschool education company) using data-driven keyword analysis, proprietary sources, and strategic internal linking.

## When to Use This Skill

Use this skill when creating:
- Hub pages (e.g., "What is Montessori Education?", "Classical Homeschooling Guide")
- Deep-dive articles (2000-3000+ words)
- SEO-focused blog posts targeting specific keywords

DO NOT use for:
- OpenEd Daily/Weekly newsletters (use newsletter skills instead)
- Social media content (use social-content-creation skill)
- Podcast production assets (use podcast-production skill)

## Pre-Writing Checklist

Before writing, gather:

1. **Primary Keyword & Intent**
   - What exact phrase are you targeting? (e.g., "homeschool art curriculum")
   - What is the search intent? (informational, navigational, transactional)
   - What's the competition level? (determines target word count)

2. **Proprietary Sources**
   - Podcast transcripts from `/Content/Open Ed Podcasts/`
   - Slack #recommendations quotes (check Notion or source files)
   - Existing OpenEd Daily content that covers the topic
   - Community stories and real parent experiences

3. **Internal Link Opportunities**
   - Check `seomachine/context/blog-index.csv` for related articles
   - Use grep to find relevant URLs: `grep -i "keyword" seomachine/context/blog-index.csv`
   - Target 3-5+ internal links minimum

4. **OpenEd Features to Highlight**
   - Review `seomachine/context/features.md` for relevant features
   - Identify where to naturally mention OpenEd offerings
   - Plan CTA placement (typically at end, sometimes mid-article for long content)

5. **Target Word Count**
   - Hub pages targeting competitive keywords: 2500-3500+ words
   - Deep dives on niche topics: 2000-2500 words
   - Standard blog posts: 1500-2000 words

## Article Structure Template

### H1: Primary Keyword Title
- Include exact primary keyword
- Keep under 60 characters for SEO
- Make it compelling, not just keyword-stuffed
- Examples:
  - "Homeschool Art Curriculum: A Complete Guide for Creative Learning"
  - "What Is Charlotte Mason Education? Philosophy, Methods & Resources"

### Hook/Introduction (150-200 words)
- Include primary keyword in first 100 words
- Start with a relatable scenario, surprising fact, or common pain point
- Preview what the article will cover
- Establish credibility (OpenEd community, expert interviews, etc.)

### Body: 4-7 H2 Sections
Structure sections using keyword variations and semantic keywords:

**H2 Ideas:**
- "What Is [Topic]?" - foundational definition section
- "How [Topic] Works" - process/implementation section
- "[Topic] vs. [Alternative]" - comparison section
- "Benefits of [Topic]" - value proposition section
- "How to Get Started with [Topic]" - action-oriented section
- "Common Challenges with [Topic]" - problem-solving section
- "Resources for [Topic]" - tools/materials section

**Within Each Section:**
- Use H3 subheadings to break up long sections
- Include 1-2 internal links where relevant
- Weave in proprietary insights (podcast quotes, community stories)
- Aim for 300-500 words per major section

### FAQ Section (For Featured Snippets)
- Include 3-5 commonly asked questions
- Use H3 for each question
- Answer in 40-60 words (optimal for featured snippet)
- Target question-based keywords (e.g., "How do I start homeschool art curriculum?")

### Call-to-Action
- Link to OpenEd info session or relevant feature
- Keep it natural, not salesy
- Example: "Want to explore more homeschool approaches like this? Join our community at OpenEd to connect with experienced homeschool families and discover what works for your children."

### Meta Elements (Add at End of Document)
```
---
META TITLE: [50-60 chars with primary keyword]
META DESCRIPTION: [150-160 chars with primary keyword and value prop]
PRIMARY KEYWORD: [exact phrase]
SECONDARY KEYWORDS: [3-5 related phrases]
INTERNAL LINKS: [list of URLs from blog-index.csv]
EXTERNAL LINKS: [2-3 authority sources]
---
```

## SEO Requirements Checklist

### Keyword Optimization
- [ ] Primary keyword in H1
- [ ] Primary keyword in first 100 words
- [ ] Primary keyword in 2-3 H2 headings (use variations)
- [ ] Primary keyword in meta title
- [ ] Primary keyword in meta description
- [ ] Keyword density: 1-2% (natural placement, not stuffed)
- [ ] Secondary keywords dispersed throughout

### Internal Linking
- [ ] 3-5+ internal links to related OpenEd content
- [ ] Used `blog-index.csv` to find relevant URLs
- [ ] Anchor text includes keywords naturally
- [ ] Links placed contextually, not in a "related posts" dump

### External Linking
- [ ] 2-3+ links to authoritative sources
- [ ] Links support claims and add credibility
- [ ] Prefer .edu, .gov, established publications

### Meta Elements
- [ ] Meta title: 50-60 characters
- [ ] Meta description: 150-160 characters
- [ ] Meta title includes primary keyword
- [ ] Meta description includes primary keyword + compelling hook

### Content Quality
- [ ] No AI-isms (see CLAUDE.md for forbidden phrases)
- [ ] Uses regular hyphens for breaks - like this - not em dashes
- [ ] Includes proprietary insights (not generic web content)
- [ ] Natural, conversational tone (OpenEd voice)
- [ ] Readability: 8th-10th grade level target

## Finding Internal Links

To discover relevant internal link opportunities:

**Method 1: Grep the Blog Index**
```bash
grep -i "montessori" /Users/charliedeist/Library/Mobile\ Documents/com~apple~CloudDocs/Root\ Docs/OpenEd\ Vault/seomachine/context/blog-index.csv
```

**Method 2: Read the Blog Index**
```bash
# Use Read tool to view blog-index.csv
# Search for related topics manually
```

**Method 3: Use Glob to Find Related Content**
```bash
# Find podcast transcripts on topic
# Find existing Daily/Weekly newsletters
# Find other hub pages
```

**Internal Link Best Practices:**
- Use descriptive anchor text (not "click here")
- Link early in the article when contextually relevant
- Prioritize hub pages and cornerstone content
- Link to related pedagogical approaches (e.g., Montessori article links to Classical, Unschooling)

## Post-Writing Analysis Tools

After drafting the article, run these Python analysis tools to verify SEO quality:

### 1. Keyword Density Check
```python
python3 -c "
from seomachine.data_sources.modules.keyword_analyzer import analyze_keywords
with open('path/to/article.md', 'r') as f:
    content = f.read()
result = analyze_keywords(content, 'primary keyword', ['secondary', 'keyword', 'list'])
print(f'Primary Keyword Density: {result[\"primary_keyword\"][\"density\"]}%')
print(f'Primary Keyword Count: {result[\"primary_keyword\"][\"count\"]}')
for kw, data in result['secondary_keywords'].items():
    print(f'{kw}: {data[\"density\"]}% ({data[\"count\"]} occurrences)')
"
```

**Targets:**
- Primary keyword: 1-2% density
- Secondary keywords: 0.5-1% each
- Total keyword mentions should feel natural, not repetitive

### 2. Readability Analysis
```python
python3 -c "
from seomachine.data_sources.modules.readability_scorer import analyze_readability
with open('path/to/article.md', 'r') as f:
    content = f.read()
result = analyze_readability(content)
print(f'Flesch-Kincaid Grade Level: {result[\"flesch_kincaid_grade\"]}')
print(f'Flesch Reading Ease: {result[\"flesch_reading_ease\"]}')
print(f'Average Sentence Length: {result[\"avg_sentence_length\"]} words')
print(f'Average Word Length: {result[\"avg_word_length\"]} characters')
"
```

**Targets:**
- Grade level: 8-10 (accessible but not dumbed down)
- Reading ease: 60-70 (standard readability)
- Sentence length: 15-20 words average
- Avoid overly complex sentences (flag anything >30 words)

### 3. Content Scrubbing (AI Watermark Removal)
```python
python3 -c "
from seomachine.data_sources.modules.content_scrubber import scrub_file
scrub_file('path/to/article.md', verbose=True)
"
```

**This tool automatically:**
- Removes em dashes (—) and replaces with hyphen + spaces
- Flags AI-isms from CLAUDE.md forbidden list
- Removes excessive formatting
- Cleans up spacing inconsistencies

### 4. Manual Review After Tools
After running automated checks:
- Read the article aloud - does it sound natural?
- Check that keywords appear in context, not shoehorned
- Verify internal links open correctly and are relevant
- Confirm meta title/description are compelling, not just keyword stuffed

## Quality Checklist (Pre-Publish)

### Content
- [ ] Article delivers on the promise in the H1/intro
- [ ] Includes proprietary OpenEd insights (not generic advice)
- [ ] No AI-isms or forbidden phrases (see CLAUDE.md)
- [ ] Uses regular hyphens for parenthetical breaks - like this
- [ ] Natural, conversational OpenEd voice throughout
- [ ] Real examples from community, podcasts, or parent stories

### SEO Technical
- [ ] Primary keyword density 1-2%
- [ ] Keyword in H1, first 100 words, 2-3 H2s, meta elements
- [ ] 3-5+ internal links from blog-index.csv
- [ ] 2-3+ external authority links
- [ ] Meta title 50-60 chars
- [ ] Meta description 150-160 chars
- [ ] FAQ section for featured snippet opportunity

### Structure
- [ ] Clear H1, H2, H3 hierarchy
- [ ] Sections are 300-500 words each (not too long)
- [ ] Article flows logically from intro to conclusion
- [ ] CTA placed naturally at end (and mid-article for long content)

### Readability
- [ ] Flesch-Kincaid grade level: 8-10
- [ ] Average sentence length: 15-20 words
- [ ] No paragraphs longer than 4-5 sentences
- [ ] Scanned for complex jargon (define or simplify)

### Final Polish
- [ ] Ran content_scrubber.py to remove AI watermarks
- [ ] Proofread for typos and grammar
- [ ] Checked links are functional
- [ ] Verified OpenEd features mentioned are accurate (check features.md)

## Example Workflow

Here's how to use this skill step-by-step:

**Step 1: Gather Requirements**
```
Target keyword: "homeschool art curriculum"
Search intent: Informational (parents researching options)
Competition: Medium (aim for 2500 words)
```

**Step 2: Find Internal Links**
```bash
grep -i "art\|curriculum\|homeschool" seomachine/context/blog-index.csv
```

**Step 3: Gather Sources**
- Read podcast transcripts on creativity, arts education
- Check Slack #recommendations for art curriculum suggestions
- Review existing Daily newsletters on creative learning

**Step 4: Draft Article**
- Use structure template above
- Weave in proprietary insights from sources
- Include 3-5 internal links naturally
- Add 2-3 external links to art education authorities

**Step 5: Run Analysis Tools**
```bash
# Keyword density
python3 -c "..." # (use script above)

# Readability
python3 -c "..." # (use script above)

# Scrub content
python3 -c "..." # (use script above)
```

**Step 6: Revise Based on Data**
- If keyword density >2%, remove some instances
- If grade level >10, simplify complex sentences
- If scrubber flags AI-isms, rewrite those sections

**Step 7: Final Quality Check**
- Run through Quality Checklist
- Read aloud for flow
- Verify all links work
- Check meta elements are filled in

**Step 8: Publish**
- Add meta title/description to CMS
- Upload article
- Monitor rankings and traffic

## Common Pitfalls to Avoid

1. **Keyword Stuffing**: Don't force the keyword into every paragraph. Use variations and synonyms.

2. **Generic Content**: Every OpenEd article should include proprietary insights. If it reads like a generic web article, dig deeper into podcast transcripts and community stories.

3. **Weak Internal Linking**: Don't just link to the homepage or info session. Link to related hub pages, blog posts, and resources.

4. **Boring Meta Descriptions**: The meta description is your search result sales pitch. Make it compelling, not just "Learn about [keyword]."

5. **Ignoring Search Intent**: If the keyword is "best homeschool art curriculum," users want recommendations, not a philosophical essay on art education.

6. **Forgetting the CTA**: Every article should guide readers toward OpenEd - info session, community, or relevant feature.

7. **AI Voice Leakage**: Run the scrubber and manually check for forbidden phrases. AI-isms kill credibility.

## Reference Files

- **Blog Index**: `seomachine/context/blog-index.csv` - all published OpenEd articles for internal linking
- **OpenEd Features**: `seomachine/context/features.md` - feature descriptions for CTAs
- **SEO Checklist**: `.claude/skills/seo-content-writer/references/seo-checklist.md` - condensed optimization checklist
- **Writing Rules**: `CLAUDE.md` - forbidden AI-isms and style guidelines

## Tool Locations

Python analysis modules are in `seomachine/data_sources/modules/`:
- `keyword_analyzer.py` - keyword density and distribution
- `readability_scorer.py` - Flesch-Kincaid scoring
- `content_scrubber.py` - AI watermark removal

Run these after drafting to validate SEO quality before publishing.
