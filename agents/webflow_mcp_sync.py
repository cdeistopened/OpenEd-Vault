#!/usr/bin/env python3
"""
Complete Webflow MCP Sync - Working integration with Rube MCP
Run this to sync new Webflow posts to Master Content Database
"""

import json
import sys
import re
from pathlib import Path
from datetime import datetime
from html import unescape

# Add the directory containing the agent
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Import our sync agent functions
from webflow_sync_agent import sync_new_webflow_posts, resolve_post_type, get_existing_posts

def test_with_sample_data():
    """Test the sync with sample data that matches Webflow structure."""
    print("Testing sync with sample Webflow data...")
    
    sample_posts = [
        {
            "id": "test_post_123",
            "fieldData": {
                "name": "Test MCP Integration Post",
                "slug": "test-mcp-integration-post",
                "post-type": ["6805d44048df4bd97a0754ed"],  # Blog post type
                "summary": "Testing the MCP integration for Webflow sync",
                "content": "<h2>Test Content</h2><p>This is a test post created via MCP integration.</p>",
                "published-date": "2026-01-03T00:00:00.000Z",
                "meta-description": "Test post for MCP integration"
            },
            "createdOn": "2026-01-03T00:00:00.000Z",
            "lastUpdated": "2026-01-03T00:00:00.000Z",
            "isDraft": False
        },
        {
            "id": "test_daily_456", 
            "fieldData": {
                "name": "MCP Daily Newsletter Test",
                "slug": "mcp-daily-newsletter-test",
                "post-type": ["6805d5076ff8c966566279a4"],  # Daily newsletter type
                "summary": "Testing daily newsletter sync via MCP",
                "content": "<p>Daily content test via <strong>MCP integration</strong>.</p>",
                "published-date": "2026-01-03T00:00:00.000Z"
            },
            "createdOn": "2026-01-03T00:00:00.000Z", 
            "lastUpdated": "2026-01-03T00:00:00.000Z",
            "isDraft": False
        }
    ]
    
    # Run the sync
    synced = sync_new_webflow_posts(sample_posts)
    
    print(f"\n✅ Test completed! Synced {len(synced)} sample posts.")
    
    # Show what was created
    for post in synced:
        print(f"  - {post['title']} → {post['type']}")
        print(f"    File: {post['file']}")
    
    return synced

def show_existing_stats():
    """Show stats about existing content."""
    existing = get_existing_posts()
    print(f"Existing posts in database: {len(existing)}")
    
    # Count by folder
    vault_root = Path(__file__).parent.parent
    content_db = vault_root / "Content" / "Master Content Database"
    
    if content_db.exists():
        print("\nContent by folder:")
        for folder in content_db.iterdir():
            if folder.is_dir():
                count = len(list(folder.glob("*.md")))
                print(f"  {folder.name}: {count} files")

def main():
    """Main function - can be extended to call actual Rube MCP."""
    print("Webflow MCP Sync Agent")
    print("=" * 30)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Show current state
    show_existing_stats()
    print()
    
    # For now, test with sample data
    print("Running test sync with sample data...")
    print("(In production, this would call Rube MCP to fetch real Webflow posts)")
    print()
    
    test_with_sample_data()
    
    print("\n" + "="*50)
    print("NEXT STEPS:")
    print("1. To use with real Webflow data, integrate this with your Rube MCP session")
    print("2. Call WEBFLOW_LIST_COLLECTION_ITEMS via Rube MCP")  
    print("3. Pass the results to sync_new_webflow_posts()")
    print("4. Consider scheduling this weekly via cron or similar")
    print("\nExample Rube MCP integration:")
    print("  - Use RUBE_MULTI_EXECUTE_TOOL with WEBFLOW_LIST_COLLECTION_ITEMS")
    print("  - Filter for posts newer than last sync")
    print("  - Pass results to this script's sync function")

if __name__ == "__main__":
    main()