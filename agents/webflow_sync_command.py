#!/usr/bin/env python3
"""
Webflow Sync Slash Command Handler
Usage: /sync-webflow [options]
"""

import sys
import argparse
from pathlib import Path

# Add agents directory to path
agents_dir = Path(__file__).parent
sys.path.insert(0, str(agents_dir))

from webflow_mcp_sync import main as run_test_sync
from webflow_sync_agent import sync_new_webflow_posts, get_existing_posts, show_existing_stats

def handle_sync_command(args=None):
    """Handle the /sync-webflow slash command."""
    parser = argparse.ArgumentParser(
        description='Sync new posts from Webflow to Master Content Database',
        prog='/sync-webflow'
    )
    parser.add_argument(
        '--test', 
        action='store_true',
        help='Run with sample test data'
    )
    parser.add_argument(
        '--stats', 
        action='store_true',
        help='Show current content database stats'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true', 
        help='Show what would be synced without making changes'
    )
    
    parsed_args = parser.parse_args(args)
    
    print("🔄 Webflow Content Sync")
    print("=" * 30)
    
    if parsed_args.stats:
        show_existing_stats()
        return
        
    if parsed_args.test:
        print("Running test sync with sample data...")
        run_test_sync()
        return
    
    if parsed_args.dry_run:
        print("DRY RUN: Would fetch latest posts from Webflow and show what's new")
        print("Note: Real implementation would use Rube MCP integration")
        show_existing_stats()
        return
    
    # Default: Run actual sync (when Rube MCP is integrated)
    print("Note: Full sync requires Rube MCP integration")
    print("Use --test to run with sample data")
    print("Use --stats to see current content stats")

def main():
    """Entry point for direct execution."""
    handle_sync_command()

if __name__ == "__main__":
    main()