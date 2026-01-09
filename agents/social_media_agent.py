#!/usr/bin/env python3
"""
Social Media Automation Agent for OpenEd Vault
Uses Get Late API to schedule and publish derivative content across all platforms
"""

import os
import requests
import json
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timezone
import logging
from dataclasses import dataclass
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Platform(Enum):
    """Supported social media platforms"""
    TWITTER = "twitter"
    LINKEDIN = "linkedin"
    FACEBOOK = "facebook"
    INSTAGRAM = "instagram"
    TIKTOK = "tiktok"
    YOUTUBE = "youtube"
    PINTEREST = "pinterest"
    REDDIT = "reddit"
    BLUESKY = "bluesky"
    THREADS = "threads"
    GOOGLE_BUSINESS = "google-business"
    TELEGRAM = "telegram"


@dataclass
class ContentSource:
    """Source content for derivative posts"""
    title: str
    summary: str
    key_points: List[str]
    url: str
    content_type: str  # newsletter, podcast, blog
    tags: List[str] = None
    media_urls: List[str] = None


class GetLateAPI:
    """Client for interacting with Get Late API"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://getlate.dev/api/v1"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def _request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """Make API request with error handling"""
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            if hasattr(e.response, 'text'):
                logger.error(f"Response: {e.response.text}")
            raise
    
    def create_profile(self, name: str, description: str = "") -> Dict:
        """Create a new profile"""
        return self._request("POST", "/profiles", {
            "name": name,
            "description": description
        })
    
    def get_profiles(self) -> List[Dict]:
        """Get all profiles"""
        response = self._request("GET", "/profiles")
        # Handle different response formats
        if isinstance(response, dict) and 'profiles' in response:
            return response['profiles']
        elif isinstance(response, list):
            return response
        else:
            return []
    
    def get_connect_url(self, platform: Platform, profile_id: str) -> str:
        """Get OAuth URL to connect a social account"""
        endpoint = f"/connect/{platform.value}"
        params = {"profileId": profile_id}
        # Make request with params
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            # OAuth URL can be in different fields
            return data.get('url') or data.get('authUrl') or data.get('redirectUrl') or ""
        except Exception as e:
            logger.error(f"Failed to get OAuth URL for {platform.value}: {e}")
            return ""
    
    def get_accounts(self, profile_id: Optional[str] = None) -> List[Dict]:
        """Get accounts, optionally filtered by profile"""
        endpoint = "/accounts"
        if profile_id:
            endpoint += f"?profileId={profile_id}"
        response = self._request("GET", endpoint)
        # Handle different response formats
        if isinstance(response, dict) and 'accounts' in response:
            return response['accounts']
        elif isinstance(response, list):
            return response
        else:
            return []
    
    def create_post(self, post_data: Dict) -> Dict:
        """Create a new post"""
        return self._request("POST", "/posts", post_data)
    
    def schedule_post(self, 
                     content: str,
                     platforms: List[Dict],
                     scheduled_for: Optional[datetime] = None,
                     timezone: str = "America/New_York") -> Dict:
        """Schedule a post to multiple platforms"""
        
        post_data = {
            "content": content,
            "platforms": platforms,
            "timezone": timezone
        }
        
        if scheduled_for:
            # Convert to ISO format
            post_data["scheduledFor"] = scheduled_for.strftime("%Y-%m-%dT%H:%M:%S")
        
        return self.create_post(post_data)
    
    def get_queue_slots(self, profile_id: str) -> List[Dict]:
        """Get available queue slots for a profile"""
        return self._request("GET", f"/profiles/{profile_id}/queue")


class ContentFormatter:
    """Platform-specific content formatting"""
    
    @staticmethod
    def twitter(source: ContentSource) -> str:
        """Format for Twitter/X (280 chars)"""
        # Create punchy, engaging content
        if source.content_type == "newsletter":
            template = "📧 {title}\n\n{key_point}\n\n{url}"
        elif source.content_type == "podcast":
            template = "🎙️ New episode: {title}\n\n{key_point}\n\n🎧 Listen: {url}"
        else:  # blog
            template = "{title}\n\n{key_point}\n\n{url}"
        
        key_point = source.key_points[0] if source.key_points else source.summary[:100]
        content = template.format(
            title=source.title,
            key_point=key_point,
            url=source.url
        )
        
        # Ensure under 280 chars
        if len(content) > 280:
            available = 280 - len(source.url) - 10  # Buffer for formatting
            title_short = source.title[:available]
            content = f"{title_short}...\n\n{source.url}"
        
        return content
    
    @staticmethod
    def linkedin(source: ContentSource) -> str:
        """Format for LinkedIn (professional, detailed)"""
        content_parts = [source.title, "", source.summary, ""]
        
        if source.key_points:
            content_parts.append("Key insights:")
            for point in source.key_points[:3]:
                content_parts.append(f"▪️ {point}")
            content_parts.append("")
        
        if source.tags:
            hashtags = " ".join([f"#{tag.replace(' ', '')}" for tag in source.tags[:5]])
            content_parts.append(hashtags)
            content_parts.append("")
        
        content_parts.append(f"Read more: {source.url}")
        
        return "\n".join(content_parts)
    
    @staticmethod
    def facebook(source: ContentSource) -> str:
        """Format for Facebook (conversational, engaging)"""
        if source.content_type == "newsletter":
            intro = "📬 Fresh from our newsletter:"
        elif source.content_type == "podcast":
            intro = "🎧 Just dropped a new episode!"
        else:
            intro = "New on the blog:"
        
        content = f"{intro} {source.title}\n\n{source.summary}\n\n"
        
        # Add engagement question
        if "parent" in source.title.lower() or "family" in source.title.lower():
            content += "What's been your experience? Share below! 👇\n\n"
        else:
            content += "Thoughts? We'd love to hear from you! 💭\n\n"
        
        content += source.url
        
        return content
    
    @staticmethod
    def instagram(source: ContentSource) -> str:
        """Format for Instagram (visual, hashtag-heavy)"""
        # Instagram needs visual content - text is for caption
        content_parts = [source.title, "", source.summary[:200], ""]
        
        if source.key_points and len(source.key_points) > 0:
            content_parts.append("✨ " + source.key_points[0])
            content_parts.append("")
        
        # More hashtags for Instagram
        hashtags = ["#OpenEd", "#AlternativeEducation", "#HomeschoolLife", 
                   "#PersonalizedLearning", "#EducationMatters"]
        
        if source.tags:
            for tag in source.tags[:3]:
                hashtags.append(f"#{tag.replace(' ', '')}")
        
        content_parts.append(" ".join(hashtags))
        content_parts.append("")
        content_parts.append(f"🔗 Link in bio for full article")
        
        return "\n".join(content_parts)
    
    @staticmethod
    def tiktok(source: ContentSource) -> str:
        """Format for TikTok (trendy, hook-focused)"""
        # TikTok needs strong hooks
        if source.content_type == "podcast":
            hook = "POV: You just discovered the education podcast that changes everything"
        elif "parent" in source.title.lower():
            hook = "Parents, this one's for you 👇"
        else:
            hook = "The education system doesn't want you to know this..."
        
        content = f"{hook}\n\n{source.title}\n\n"
        
        # Quick bullet points
        if source.key_points:
            for point in source.key_points[:2]:
                content += f"💡 {point}\n"
        
        content += "\n#OpenEd #Education #AlternativeSchool #LearnDifferent"
        
        return content
    
    @staticmethod
    def youtube(source: ContentSource) -> str:
        """Format for YouTube (detailed description)"""
        if source.content_type == "podcast":
            content = f"🎙️ {source.title}\n\n"
        else:
            content = f"📚 {source.title}\n\n"
        
        content += f"{source.summary}\n\n"
        
        if source.key_points:
            content += "In this video/episode:\n"
            for i, point in enumerate(source.key_points, 1):
                content += f"{i}. {point}\n"
            content += "\n"
        
        content += "RESOURCES:\n"
        content += f"📖 Full article: {source.url}\n"
        content += "🌐 Website: https://opened.com\n"
        content += "📧 Newsletter: https://opened.com/newsletter\n\n"
        
        content += "CONNECT:\n"
        content += "Twitter: @OpenEdOfficial\n"
        content += "LinkedIn: /company/opened\n"
        content += "Facebook: /OpenEdCommunity\n\n"
        
        content += "#OpenEd #AlternativeEducation #Homeschool"
        
        return content
    
    @staticmethod
    def pinterest(source: ContentSource) -> str:
        """Format for Pinterest (SEO-focused)"""
        # Pinterest is very SEO-driven
        content = f"{source.title} | OpenEd\n\n"
        content += f"{source.summary}\n\n"
        
        # Add keywords
        keywords = ["alternative education", "homeschool ideas", "personalized learning",
                   "education tips", "parenting advice", "student success"]
        
        if source.tags:
            keywords.extend(source.tags[:3])
        
        content += " • ".join(keywords) + "\n\n"
        content += f"Read more ➡️ {source.url}"
        
        return content


class OpenEdSocialMediaAgent:
    """Agent for automating OpenEd Vault social media posts"""
    
    def __init__(self, api_key: str):
        self.api = GetLateAPI(api_key)
        self.profile_id = None
        self.accounts = {}
        self.formatter = ContentFormatter()
        
    def setup(self) -> bool:
        """Set up profiles and accounts"""
        try:
            # Get existing profiles
            profiles = self.api.get_profiles()
            
            # Debug: log profiles structure
            logger.debug(f"Profiles response: {profiles}")
            
            # Look for OpenEd Vault profile
            opened_profile = None
            if isinstance(profiles, list):
                opened_profile = next(
                    (p for p in profiles if isinstance(p, dict) and p.get('name') == 'OpenEd Vault'),
                    None
                )
            elif isinstance(profiles, dict) and 'data' in profiles:
                # Handle wrapped response
                profiles_list = profiles.get('data', [])
                opened_profile = next(
                    (p for p in profiles_list if isinstance(p, dict) and p.get('name') == 'OpenEd Vault'),
                    None
                )
            
            if not opened_profile:
                # Create new profile
                logger.info("Creating OpenEd Vault profile...")
                opened_profile = self.api.create_profile(
                    name="OpenEd Vault",
                    description="Alternative education content hub - newsletters, podcasts, and resources"
                )
                logger.info(f"Created profile: {opened_profile['id']}")
            
            # Handle different ID field names
            self.profile_id = opened_profile.get('id') or opened_profile.get('_id')
            
            # Get connected accounts
            accounts = self.api.get_accounts(self.profile_id)
            for account in accounts:
                platform = account.get('platform', '').lower()
                self.accounts[platform] = account
                logger.info(f"Found {platform} account: {account.get('name')}")
            
            # Report missing accounts
            desired_platforms = [Platform.TWITTER, Platform.LINKEDIN, Platform.FACEBOOK,
                               Platform.INSTAGRAM, Platform.TIKTOK, Platform.YOUTUBE,
                               Platform.PINTEREST]
            
            missing = []
            for platform in desired_platforms:
                if platform.value not in self.accounts:
                    missing.append(platform)
            
            if missing:
                logger.info("\nMissing platform connections:")
                for platform in missing:
                    logger.info(f"  - {platform.value}")
                logger.info("\nUse get_oauth_urls() to get connection links")
            
            return True
            
        except Exception as e:
            logger.error(f"Setup failed: {e}")
            return False
    
    def get_oauth_urls(self) -> Dict[str, str]:
        """Get OAuth URLs for connecting social accounts"""
        if not self.profile_id:
            raise Exception("Run setup() first")
        
        urls = {}
        platforms = [Platform.TWITTER, Platform.LINKEDIN, Platform.FACEBOOK,
                    Platform.INSTAGRAM, Platform.TIKTOK, Platform.YOUTUBE,
                    Platform.PINTEREST]
        
        for platform in platforms:
            if platform.value not in self.accounts:
                try:
                    url = self.api.get_connect_url(platform, self.profile_id)
                    urls[platform.value] = url
                except Exception as e:
                    logger.error(f"Failed to get {platform.value} OAuth URL: {e}")
        
        return urls
    
    def create_platform_posts(self, source: ContentSource) -> Dict[str, str]:
        """Create platform-specific content from source"""
        posts = {}
        
        # Generate content for each connected platform
        formatters = {
            Platform.TWITTER.value: self.formatter.twitter,
            Platform.LINKEDIN.value: self.formatter.linkedin,
            Platform.FACEBOOK.value: self.formatter.facebook,
            Platform.INSTAGRAM.value: self.formatter.instagram,
            Platform.TIKTOK.value: self.formatter.tiktok,
            Platform.YOUTUBE.value: self.formatter.youtube,
            Platform.PINTEREST.value: self.formatter.pinterest,
        }
        
        for platform, formatter_func in formatters.items():
            if platform in self.accounts:
                posts[platform] = formatter_func(source)
        
        return posts
    
    def schedule_content(self, source: ContentSource, 
                        scheduled_for: Optional[datetime] = None) -> List[Dict]:
        """Schedule content across all connected platforms"""
        if not self.profile_id:
            if not self.setup():
                raise Exception("Failed to set up social media accounts")
        
        # Create platform-specific content
        platform_posts = self.create_platform_posts(source)
        
        # Prepare platforms data for API
        platforms_data = []
        for platform, content in platform_posts.items():
            platforms_data.append({
                "platform": platform,
                "accountId": self.accounts[platform]["id"],
                "content": content
            })
        
        if not platforms_data:
            logger.warning("No connected platforms to post to")
            return []
        
        # Schedule the post
        try:
            result = self.api.schedule_post(
                content=source.title,  # This is used as the "main" content
                platforms=platforms_data,
                scheduled_for=scheduled_for
            )
            
            logger.info(f"Successfully scheduled post: {result.get('id')}")
            return [result]
            
        except Exception as e:
            logger.error(f"Failed to schedule posts: {e}")
            raise
    
    def test_connection(self) -> bool:
        """Test API connection and show account status"""
        try:
            profiles = self.api.get_profiles()
            logger.info(f"✅ API connection successful")
            logger.info(f"Found {len(profiles)} profiles")
            
            if self.setup():
                logger.info(f"\nProfile: OpenEd Vault")
                logger.info(f"Connected accounts: {len(self.accounts)}")
                for platform, account in self.accounts.items():
                    logger.info(f"  - {platform}: {account.get('name', 'Unknown')}")
                
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"❌ API connection failed: {e}")
            return False


# Test script
if __name__ == "__main__":
    # Load API key from environment
    api_key = os.getenv('GETLATE_API_KEY')
    if not api_key:
        logger.error("GETLATE_API_KEY not found in environment")
        exit(1)
    
    # Initialize agent
    agent = OpenEdSocialMediaAgent(api_key)
    
    # Test connection
    logger.info("Testing Get Late API connection...")
    if agent.test_connection():
        logger.info("\n✅ Connection successful!")
        
        # Get OAuth URLs for missing accounts
        oauth_urls = agent.get_oauth_urls()
        if oauth_urls:
            logger.info("\n🔗 Connect your social accounts:")
            for platform, url in oauth_urls.items():
                logger.info(f"{platform}: {url}")
        
        # Example content
        logger.info("\n📝 Example content formatting:")
        sample = ContentSource(
            title="Why Alternative Education is the Future",
            summary="Discover how personalized learning paths are revolutionizing education for thousands of students across 9 states.",
            key_points=[
                "Students learn at their own pace with individualized curricula",
                "Real-world projects connect learning to practical life skills", 
                "Parent involvement strengthens educational outcomes"
            ],
            url="https://opened.com/blog/alternative-education-future",
            content_type="blog",
            tags=["education", "homeschool", "personalized learning"]
        )
        
        posts = agent.create_platform_posts(sample)
        for platform, content in posts.items():
            logger.info(f"\n--- {platform.upper()} ---")
            logger.info(content)
            logger.info(f"Length: {len(content)} chars")
    else:
        logger.error("\n❌ Connection test failed")