#!/usr/bin/env python3
"""
Quick test script for Get Late API connection
Run this first to verify your setup
"""

import os
import sys
from pathlib import Path

# Add parent directory to path
parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))

# Load environment variables
from dotenv import load_dotenv
load_dotenv(parent_dir / '.env')

from agents.social_media_agent import OpenEdSocialMediaAgent, ContentSource
import logging

# Simple logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


def main():
    # Check for API key
    api_key = os.getenv('GETLATE_API_KEY')
    if not api_key:
        logger.error("❌ GETLATE_API_KEY not found in .env file")
        return
    
    logger.info("🚀 Testing Get Late API Integration\n")
    logger.info("=" * 50)
    
    # Initialize agent
    agent = OpenEdSocialMediaAgent(api_key)
    
    # Test basic connection
    logger.info("\n1️⃣  Testing API Connection...")
    if not agent.test_connection():
        logger.error("Failed to connect to API")
        return
    
    # Get OAuth URLs if needed
    logger.info("\n2️⃣  Checking for missing social accounts...")
    oauth_urls = agent.get_oauth_urls()
    
    if oauth_urls:
        logger.info("\n⚠️  You need to connect these accounts:")
        logger.info("Click each link below to authorize Get Late:\n")
        
        for platform, url in oauth_urls.items():
            logger.info(f"  {platform.upper()}:")
            logger.info(f"  {url}\n")
        
        logger.info("After connecting accounts, run this script again!")
    else:
        logger.info("✅ All platforms connected!")
        
        # Show example content
        logger.info("\n3️⃣  Example Content Generation")
        logger.info("=" * 50)
        
        # Create sample content
        sample = ContentSource(
            title="5 Myths About Alternative Education Debunked",
            summary="Think alternative education means less structure? Think again. We're breaking down the biggest misconceptions about personalized learning.",
            key_points=[
                "Myth 1: No real curriculum → Truth: Tailored to each student",
                "Myth 2: Kids fall behind → Truth: Many excel beyond grade level",
                "Myth 3: No social skills → Truth: Strong community connections"
            ],
            url="https://opened.com/blog/5-myths-alternative-education",
            content_type="blog",
            tags=["education myths", "homeschool", "OpenEd"]
        )
        
        # Generate platform content
        posts = agent.create_platform_posts(sample)
        
        logger.info("\nGenerated content for your platforms:\n")
        for platform, content in posts.items():
            logger.info(f"📱 {platform.upper()}")
            logger.info("-" * 30)
            logger.info(content)
            logger.info(f"\nLength: {len(content)} characters")
            logger.info("=" * 50 + "\n")
        
        logger.info("\n✅ Everything looks good!")
        logger.info("\nNext steps:")
        logger.info("1. Review the generated content above")
        logger.info("2. Run 'python agents/schedule_content.py' to schedule posts")
        logger.info("3. Check your Get Late dashboard at https://getlate.dev")


if __name__ == "__main__":
    main()