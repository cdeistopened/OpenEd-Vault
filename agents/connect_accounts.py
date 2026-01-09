#!/usr/bin/env python3
"""
Connect Social Media Accounts to Get Late
Interactive script to guide through OAuth connections
"""

import os
import sys
import time
import webbrowser
from pathlib import Path
from dotenv import load_dotenv

# Add parent directory to path
parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))
load_dotenv(parent_dir / '.env')

from agents.social_media_agent import OpenEdSocialMediaAgent
import logging

# Simple logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

# Platform emojis and descriptions
PLATFORM_INFO = {
    'twitter': {'emoji': '🐦', 'name': 'Twitter/X', 'desc': 'Share quick updates and engage'},
    'linkedin': {'emoji': '💼', 'name': 'LinkedIn', 'desc': 'Professional network posts'},
    'facebook': {'emoji': '👥', 'name': 'Facebook', 'desc': 'Community engagement'},
    'instagram': {'emoji': '📸', 'name': 'Instagram', 'desc': 'Visual storytelling'},
    'tiktok': {'emoji': '🎵', 'name': 'TikTok', 'desc': 'Short-form video content'},
    'youtube': {'emoji': '📹', 'name': 'YouTube', 'desc': 'Video content and Shorts'},
    'pinterest': {'emoji': '📌', 'name': 'Pinterest', 'desc': 'Visual discovery platform'}
}


def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')


def display_header():
    """Display app header"""
    print("=" * 60)
    print("🚀 Get Late Social Media Connection Setup")
    print("=" * 60)
    print()


def main():
    # Check for API key
    api_key = os.getenv('GETLATE_API_KEY')
    if not api_key:
        logger.error("❌ GETLATE_API_KEY not found in .env file")
        return
    
    # Initialize agent
    agent = OpenEdSocialMediaAgent(api_key)
    
    # Setup and check current status
    if not agent.setup():
        logger.error("Failed to initialize Get Late agent")
        return
    
    clear_screen()
    display_header()
    
    # Check connected accounts
    connected = []
    not_connected = []
    
    for platform in PLATFORM_INFO.keys():
        if platform in agent.accounts:
            connected.append(platform)
        else:
            not_connected.append(platform)
    
    # Display current status
    print("📊 Current Connection Status:\n")
    
    if connected:
        print("✅ Connected Accounts:")
        for platform in connected:
            info = PLATFORM_INFO[platform]
            account = agent.accounts[platform]
            print(f"   {info['emoji']} {info['name']} - @{account.get('name', 'Unknown')}")
        print()
    
    if not_connected:
        print("❌ Not Connected:")
        for platform in not_connected:
            info = PLATFORM_INFO[platform]
            print(f"   {info['emoji']} {info['name']} - {info['desc']}")
        print()
    
    if not not_connected:
        print("🎉 All platforms are connected! You're ready to start posting.")
        return
    
    # Get OAuth URLs
    print("🔗 Getting connection links...\n")
    oauth_urls = agent.get_oauth_urls()
    
    # Interactive connection process
    print("=" * 60)
    print("📋 Connection Instructions:")
    print("=" * 60)
    print("1. Click each link below (or copy/paste into browser)")
    print("2. Authorize Get Late to access your account")
    print("3. You'll be redirected back to Get Late")
    print("4. Repeat for each platform you want to connect")
    print("5. Run this script again to verify connections")
    print("=" * 60)
    print()
    
    # Display OAuth URLs with option to open
    for i, platform in enumerate(not_connected, 1):
        info = PLATFORM_INFO[platform]
        url = oauth_urls.get(platform, '')
        
        print(f"{i}. {info['emoji']} {info['name']}")
        print(f"   {'-' * 55}")
        
        if url:
            print(f"   {url}")
            print()
            
            # Ask if user wants to open in browser
            if i == 1:  # Only ask for the first one
                try:
                    response = input("   Open this link in your browser? (y/n): ").lower()
                    if response == 'y':
                        webbrowser.open(url)
                        print("   ✅ Opened in browser!")
                except:
                    pass
        else:
            print(f"   ❌ Failed to get OAuth URL")
        
        print()
    
    print("=" * 60)
    print("💡 Tips:")
    print("- Make sure you're logged into each platform first")
    print("- For Instagram/Facebook, you need a business account")
    print("- YouTube requires a channel to post videos")
    print("- Some platforms may ask for additional permissions")
    print()
    print("After connecting, run 'python agents/connect_accounts.py' again")
    print("to verify your connections and see the next steps!")
    print("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Connection setup cancelled")
    except Exception as e:
        logger.error(f"\n❌ Error: {e}")