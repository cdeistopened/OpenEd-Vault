#!/usr/bin/env python3
"""
Content Multiplication Agent for OpenEd Vault
Takes hub content and creates platform-specific social posts
"""

import os
import json
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@dataclass
class HubContent:
    """Source content for multiplication"""
    title: str
    content_type: str  # newsletter, podcast, article
    summary: str
    key_points: List[str]
    stats: List[str]
    stories: List[str]
    url: str
    controversial_take: Optional[str] = None
    transformation_example: Optional[str] = None


class ContentMultiplier:
    """Multiply hub content across social platforms"""
    
    def __init__(self):
        self.platforms = ['linkedin', 'facebook', 'twitter', 'instagram', 'reddit', 'tiktok', 'pinterest']
        self.generated_posts = {}
        
    def extract_value(self, content: str) -> HubContent:
        """Extract key value from hub content"""
        # In production, this would use AI to analyze content
        # For demo, we'll use the 2012 newsletter example
        return HubContent(
            title="What happened in 2012?",
            content_type="newsletter",
            summary="Explores how 2012 marked a shift when smartphones became ubiquitous, leading to 50%+ increases in youth depression and anxiety.",
            key_points=[
                "Depression and anxiety rose by over 50% among young people after 2012",
                "Academic achievement reversed decades of steady gains",
                "Even having a phone nearby creates a cognitive tax"
            ],
            stats=[
                "Depression increased by 50%+ after 2012",
                "First generation with perpetual digital connection",
                "Academic gains reversed after decades"
            ],
            stories=[
                "The 'Great Rewiring' of childhood happened in 2012",
                "Smartphones went from luxury to necessity"
            ],
            url="https://opened.com/newsletter/108-what-happened-2012",
            controversial_take="2012 killed childhood as we know it",
            transformation_example="Phone-free homework zones improved focus dramatically"
        )
    
    def generate_linkedin_post(self, hub: HubContent) -> Dict:
        """Generate LinkedIn comment-to-get post"""
        
        # Select hook based on content type
        hooks = [
            f"Depression and anxiety in kids rose by 50% after 2012.",
            f"{hub.controversial_take}",
            f"Every parent should know {hub.title.lower()}",
            f"We analyzed 13 years of youth data. {hub.stats[0]}",
            f"If your kid struggles with focus, this started in 2012."
        ]
        
        # Build post
        post = {
            'platform': 'linkedin',
            'hook': hooks[0],  # In production, test multiple
            'content': f"""{hooks[0]}

Here's what changed - and what we can do about it.

{hub.summary}

The results?
• {hub.key_points[0]}
• {hub.key_points[1]}
• Social connections plummeted
• Dating and real-world interactions nearly disappeared

But here's what most parents don't know: {hub.key_points[2]}

I've compiled the research into a comprehensive guide that includes:
• The timeline of how the "Great Rewiring" unfolded
• Why traditional classrooms make it worse
• Strategic alternatives that actually work
• {hub.transformation_example}

Give this post a like and comment "RESEARCH" and I'll DM you the full analysis (must be connected).

#Education #Parenting #AlternativeEducation #DigitalWellbeing #HomeschoolLife""",
            'cta_keyword': 'RESEARCH',
            'resource_link': hub.url
        }
        
        return post
    
    def generate_facebook_post(self, hub: HubContent) -> Dict:
        """Generate Facebook visual controversy post"""
        
        # Text-on-background one-liner
        one_liners = [
            "Your kid's anxiety isn't their fault. It started in 2012.",
            "Normalize understanding what happened to kids in 2012",
            "Traditional school + smartphones = anxiety epidemic",
            f"{hub.controversial_take}",
            "Stop blaming parents. Start understanding 2012."
        ]
        
        return {
            'platform': 'facebook',
            'format': 'text-on-background',
            'text': one_liners[0],
            'caption': f"""{hub.summary}

What changed:
{chr(10).join(['→ ' + point for point in hub.key_points[:3]])}

We've been studying this shift for years. The data is shocking but the solutions are surprisingly simple.

What's been your family's experience with technology and learning?

Read the full analysis: {hub.url}""",
            'background_color': '#ffeda0'  # OpenEd yellow
        }
    
    def generate_twitter_thread(self, hub: HubContent) -> Dict:
        """Generate Twitter/X thread"""
        
        tweets = [
            f"{hub.controversial_take}\n\nA thread on what happened - and how to fix it: 🧵",
            f"In 2012, something fundamental shifted.\n\n{hub.stats[0]}",
            f"{hub.stories[0]}\n\nFor the first time in history, an entire generation grew up with constant digital connection.",
            f"The results were immediate and devastating:\n\n{chr(10).join(['• ' + point for point in hub.key_points[:3]])}",
            f"But here's what most don't know:\n\n{hub.key_points[2]}",
            f"{hub.transformation_example}\n\nSmall changes, huge impact.",
            f"We analyzed the data and created a guide for parents.\n\nFull research + action steps: {hub.url}"
        ]
        
        return {
            'platform': 'twitter',
            'format': 'thread',
            'tweets': tweets
        }
    
    def generate_reddit_responses(self, hub: HubContent) -> List[Dict]:
        """Generate organic Reddit responses"""
        
        responses = []
        
        # Response for anxiety thread
        responses.append({
            'platform': 'reddit',
            'subreddit': 'r/Parenting',
            'trigger_keywords': ['anxiety', 'focus', 'screen time', 'struggling'],
            'response': f"""You're not alone in this - there's actually a bigger pattern that most parents don't know about.

{hub.stats[0]} It wasn't gradual - it was a sudden shift that coincided with {hub.stories[1]}.

What helped us was understanding that {hub.key_points[2]}. We made some simple changes ({hub.transformation_example}) and saw huge improvements.

The research on this is fascinating and honestly changed how we approach screen time entirely. Happy to share more about what we learned if you're interested. The main thing is: this isn't your fault, and there are concrete things that help."""
        })
        
        # Response for homeschool thread
        responses.append({
            'platform': 'reddit',
            'subreddit': 'r/homeschool',
            'trigger_keywords': ['technology', 'screens', 'distraction', 'focus'],
            'response': f"""This is exactly why we chose alternative education for our kids.

{hub.summary}

One thing that really opened our eyes: {hub.key_points[2]}. Once we understood this, we completely restructured our learning environment.

If you're curious about the research behind this, I actually put together a comprehensive guide on what happened and what we can do about it. The solutions are more straightforward than you might think!"""
        })
        
        return responses
    
    def generate_instagram_reel(self, hub: HubContent) -> Dict:
        """Generate Instagram Reel concept"""
        
        return {
            'platform': 'instagram',
            'format': 'reel',
            'hook': "POV: You just learned your kid's anxiety started in 2012",
            'text_reveals': [
                "Depression up 50%",
                "Academic gains reversed",
                "Social connections plummeted", 
                "The year smartphones took over",
                "But there's hope..."
            ],
            'caption': f"""{hub.title}

{hub.summary}

{chr(10).join([point for point in hub.key_points[:2]])}

But here's the good news - understanding the problem is the first step to solving it.

Comment "GUIDE" and I'll send you our research + action plan 📱➡️📚

#AlternativeEducation #ParentingTips #DigitalWellbeing #HomeschoolLife #EducationMatters #2012Shift #AnxietySupport #KidsAndTech""",
            'audio': 'trending-audio-emotional'
        }
    
    def generate_tiktok_video(self, hub: HubContent) -> Dict:
        """Generate TikTok video concept"""
        
        return {
            'platform': 'tiktok',
            'format': 'text-over-video',
            'hook': "The education system doesn't want you to know what happened in 2012",
            'script': [
                "You know how kids today seem more anxious than ever?",
                "It's not your imagination",
                f"{hub.stats[0]}",
                "It all started in 2012", 
                f"{hub.stories[1]}",
                "The first generation to grow up like this is struggling",
                "But families who know this secret are thriving",
                f"{hub.transformation_example}",
                "Follow for more education truth bombs"
            ],
            'hashtags': ['#2012Truth', '#EducationSecrets', '#ParentingHacks', '#AlternativeEducation', '#KidsAndTech']
        }
    
    def generate_pinterest_pin(self, hub: HubContent) -> Dict:
        """Generate Pinterest pin"""
        
        return {
            'platform': 'pinterest',
            'title': f"The 2012 Shift: {hub.title}",
            'description': f"""{hub.summary}

Key findings:
{chr(10).join(['• ' + point for point in hub.key_points])}

{hub.transformation_example}

Click through for the full research report and action guide for parents navigating education in the digital age.

Keywords: alternative education, homeschool resources, digital wellness, parenting tips, education research, screen time solutions, anxiety in kids, focus strategies, 2012 shift""",
            'pin_text_overlay': "What Happened in 2012?\n50% Rise in Youth Anxiety\nThe Research Every Parent Needs",
            'board': 'Education Research & Resources'
        }
    
    def multiply_content(self, hub_content: str) -> Dict:
        """Main method to multiply content across platforms"""
        
        # Extract value from hub content
        hub = self.extract_value(hub_content)
        
        # Generate platform-specific posts
        self.generated_posts = {
            'source': {
                'title': hub.title,
                'type': hub.content_type,
                'url': hub.url
            },
            'posts': {
                'linkedin': self.generate_linkedin_post(hub),
                'facebook': self.generate_facebook_post(hub),
                'twitter': self.generate_twitter_thread(hub),
                'reddit': self.generate_reddit_responses(hub),
                'instagram': self.generate_instagram_reel(hub),
                'tiktok': self.generate_tiktok_video(hub),
                'pinterest': self.generate_pinterest_pin(hub)
            },
            'generated_at': datetime.now().isoformat()
        }
        
        return self.generated_posts
    
    def save_posts(self, filename: str = None):
        """Save generated posts to file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"multiplied_content_{timestamp}.json"
        
        output_dir = "Studio/Social Media Tests/generated"
        os.makedirs(output_dir, exist_ok=True)
        
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w') as f:
            json.dump(self.generated_posts, f, indent=2)
        
        logger.info(f"Saved generated posts to {filepath}")
        return filepath
    
    def schedule_posts(self, posts: Dict, start_time: datetime = None):
        """Create posting schedule for all platforms"""
        if not start_time:
            start_time = datetime.now() + timedelta(hours=1)
        
        schedule = []
        
        # Platform-specific best times (ET)
        best_times = {
            'linkedin': 8,  # 8am
            'facebook': 13,  # 1pm  
            'twitter': 9,   # 9am
            'instagram': 18, # 6pm
            'tiktok': 19,   # 7pm
            'pinterest': 20, # 8pm
            'reddit': 10    # 10am
        }
        
        for platform, hour in best_times.items():
            if platform in posts['posts']:
                post_time = start_time.replace(hour=hour, minute=0, second=0)
                schedule.append({
                    'platform': platform,
                    'scheduled_for': post_time.isoformat(),
                    'content': posts['posts'][platform]
                })
        
        return sorted(schedule, key=lambda x: x['scheduled_for'])


# Example usage
if __name__ == "__main__":
    # Initialize multiplier
    multiplier = ContentMultiplier()
    
    # Example hub content (would normally load from file)
    hub_content = """
    Newsletter #108: What happened in 2012?
    
    The year 2012 marked a dramatic shift in childhood development...
    [Full newsletter content would go here]
    """
    
    # Generate all social posts
    logger.info("Multiplying content across platforms...")
    posts = multiplier.multiply_content(hub_content)
    
    # Save generated posts
    filepath = multiplier.save_posts()
    
    # Create posting schedule
    schedule = multiplier.schedule_posts(posts)
    
    # Display results
    logger.info(f"\nGenerated {len(posts['posts'])} platform variations:")
    for platform in posts['posts']:
        logger.info(f"  ✓ {platform}")
    
    logger.info(f"\nPosting schedule created:")
    for item in schedule:
        logger.info(f"  {item['platform']}: {item['scheduled_for']}")
    
    logger.info(f"\nNext steps:")
    logger.info(f"1. Review generated posts in {filepath}")
    logger.info(f"2. Edit for voice and platform fit")
    logger.info(f"3. Use social_media_agent.py to schedule via Get Late API")