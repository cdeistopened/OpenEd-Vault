#!/usr/bin/env python3
"""
Webflow Content Sync Agent - Uses Rube MCP Integration
Fetches new posts from Webflow and syncs them to Master Content Database
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
from html import unescape

# Post type ID to name mapping (from existing webflow.py)
POST_TYPE_MAP = {
    '6812753c2611e43906dc13d6': 'Announcements',
    '6805d5076ff8c966566279a4': 'Daily Newsletters', 
    '6805d44048df4bd97a0754ed': 'Blog Posts',
    '6805d42ba524fabb70579f4e': 'Podcasts'
}

def html_to_markdown(html_content):
    """Convert HTML content to markdown."""
    if not html_content:
        return ''

    text = html_content

    # Remove style and script tags
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove embedded HTML documents 
    text = re.sub(r'<div data-rt-embed-type=[\'"]true[\'"]>.*?</div>\s*(?=<[^d]|$)', '', text, flags=re.DOTALL)

    # Convert headers
    text = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n# \1\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n## \1\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n### \1\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<h4[^>]*>(.*?)</h4>', r'\n#### \1\n', text, flags=re.DOTALL | re.IGNORECASE)

    # Convert links, bold, italic
    text = re.sub(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<(strong|b)[^>]*>(.*?)</\1>', r'**\2**', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<(em|i)[^>]*>(.*?)</\1>', r'*\2*', text, flags=re.DOTALL | re.IGNORECASE)

    # Convert lists
    text = re.sub(r'<ul[^>]*>(.*?)</ul>', lambda m: '\n' + re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', m.group(1), flags=re.DOTALL | re.IGNORECASE) + '\n', text, flags=re.DOTALL | re.IGNORECASE)

    def convert_ol(match):
        items = re.findall(r'<li[^>]*>(.*?)</li>', match.group(1), flags=re.DOTALL | re.IGNORECASE)
        return '\n' + '\n'.join(f'{i+1}. {item.strip()}' for i, item in enumerate(items)) + '\n'
    text = re.sub(r'<ol[^>]*>(.*?)</ol>', convert_ol, text, flags=re.DOTALL | re.IGNORECASE)

    # Convert paragraphs and line breaks
    text = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)

    # Convert blockquotes
    text = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', lambda m: '\n> ' + m.group(1).strip().replace('\n', '\n> ') + '\n', text, flags=re.DOTALL | re.IGNORECASE)

    # Remove remaining HTML tags and decode entities
    text = re.sub(r'<[^>]+>', '', text)
    text = unescape(text)

    # Clean up whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = '\n'.join(line.strip() for line in text.split('\n'))

    return text.strip()

def resolve_post_type(post_type_ids):
    """Convert post-type reference IDs to folder name."""
    if not post_type_ids:
        return 'Other'
    # Take the first type if multiple
    type_id = post_type_ids[0] if isinstance(post_type_ids, list) else post_type_ids
    return POST_TYPE_MAP.get(type_id, 'Other')

def get_existing_posts():
    """Get list of existing posts from Master Content Database."""
    vault_root = Path(__file__).parent.parent
    content_db = vault_root / "Content" / "Master Content Database"
    
    existing_posts = set()
    
    # Check all content folders
    for folder in content_db.iterdir():
        if folder.is_dir():
            for file in folder.glob("*.md"):
                # Extract webflow_id from frontmatter if it exists
                content = file.read_text(encoding='utf-8')
                if 'webflow_id:' in content:
                    match = re.search(r'webflow_id:\s*(\w+)', content)
                    if match:
                        existing_posts.add(match.group(1))
                        
                # Also track by filename for duplicate prevention
                existing_posts.add(file.stem)
    
    return existing_posts

def create_markdown_file(post, content_db_path):
    """Create markdown file for a new post."""
    field_data = post.get('fieldData', {})
    
    # Extract fields
    title = field_data.get('name', 'Untitled')
    slug = field_data.get('slug', '')
    post_type_ids = field_data.get('post-type', [])
    post_type = resolve_post_type(post_type_ids)
    meta_description = field_data.get('meta-description', '')
    summary = field_data.get('summary', '')
    published_date = field_data.get('published-date', '') or field_data.get('published-on', '')
    html_content = field_data.get('content', '')
    webflow_id = post.get('id', '')

    # Parse date
    if published_date:
        try:
            dt = datetime.fromisoformat(published_date.replace('Z', '+00:00'))
            date_str = dt.strftime('%Y-%m-%d')
        except:
            date_str = published_date[:10] if len(published_date) >= 10 else ''
    else:
        date_str = ''

    # Build URL based on type
    if 'Podcast' in post_type:
        url = f"https://opened.co/podcast/{slug}"
    elif 'Daily' in post_type:
        url = f"https://opened.co/newsletter/{slug}"
    elif 'Announcement' in post_type:
        url = f"https://opened.co/blog/{slug}"
    else:
        url = f"https://opened.co/blog/{slug}"

    # Escape quotes for YAML
    escaped_title = title.replace('"', "'")
    escaped_meta = meta_description.replace('"', "'")
    escaped_summary = summary.replace('"', "'")
    sync_time = datetime.now().strftime('%Y-%m-%d %H:%M')

    # Convert HTML content to markdown
    markdown_content = html_to_markdown(html_content) if html_content else ''

    # Create frontmatter and content
    file_content = f"""---
title: "{escaped_title}"
url: {url}
slug: {slug}
type: {post_type.lower().replace(' ', '_')}
date: {date_str}
meta_description: "{escaped_meta}"
summary: "{escaped_summary}"
webflow_id: {webflow_id}
last_synced: {sync_time}
---

# {title}

**URL:** [{url}]({url})
**Type:** {post_type}
**Published:** {date_str}

"""

    if summary:
        file_content += f"## Summary\n{summary}\n\n"

    if markdown_content:
        file_content += f"## Content\n\n{markdown_content}\n"
    else:
        file_content += "_No content available_\n"

    # Create safe filename
    safe_title = "".join(c for c in title if c.isalnum() or c in ' -_').strip()
    safe_title = safe_title[:60]  # Limit length
    filename = f"{safe_title}.md"

    # Create subfolder and file path
    type_dir = content_db_path / post_type
    type_dir.mkdir(parents=True, exist_ok=True)
    filepath = type_dir / filename

    # Write file
    filepath.write_text(file_content, encoding='utf-8')
    
    return {
        'title': title,
        'url': url,
        'type': post_type,
        'file': str(filepath),
        'webflow_id': webflow_id,
        'has_content': bool(markdown_content)
    }

def update_master_index(synced_posts):
    """Update the Master_Content_Index.md file."""
    vault_root = Path(__file__).parent.parent
    index_file = vault_root / "Master_Content_Index.md"
    
    if not index_file.exists():
        print(f"Master index not found at {index_file}")
        return
    
    # Read current index
    content = index_file.read_text(encoding='utf-8')
    
    # Update the generated timestamp
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    content = re.sub(r'Generated: [^\n]+', f'Generated: {now}', content)
    
    # Update total files count (rough estimation - could be more precise)
    current_total_match = re.search(r'Total Files: (\d+)', content)
    if current_total_match:
        current_total = int(current_total_match.group(1))
        new_total = current_total + len(synced_posts)
        content = re.sub(r'Total Files: \d+', f'Total Files: {new_total}', content)
    
    # Write updated index
    index_file.write_text(content, encoding='utf-8')
    print(f"Updated Master Content Index with {len(synced_posts)} new posts")

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
    """Main sync function - to be called by Rube MCP integration."""
    print("Starting Webflow content sync using Rube MCP...")
    print("=" * 50)
    
    # Set up paths
    vault_root = Path(__file__).parent.parent
    content_db = vault_root / "Content" / "Master Content Database"
    content_db.mkdir(parents=True, exist_ok=True)
    
    # Get existing posts to avoid duplicates
    existing_posts = get_existing_posts()
    print(f"Found {len(existing_posts)} existing posts")
    
    # Note: This script is designed to be called with Webflow data
    # The actual Rube MCP calls should be made from the calling script
    print("\nNOTE: This script processes Webflow data provided by Rube MCP.")
    print("Call this with: sync_new_webflow_posts(webflow_posts_data)")
    
def sync_new_webflow_posts(webflow_posts_data):
    """Process Webflow posts data from Rube MCP and sync new posts."""
    vault_root = Path(__file__).parent.parent  
    content_db = vault_root / "Content" / "Master Content Database"
    content_db.mkdir(parents=True, exist_ok=True)
    
    # Get existing posts
    existing_posts = get_existing_posts()
    
    new_posts = []
    synced = []
    
    # Process each post from Webflow
    for post in webflow_posts_data:
        webflow_id = post.get('id', '')
        title = post.get('fieldData', {}).get('name', 'Untitled')
        
        # Skip if we already have this post
        if webflow_id in existing_posts:
            continue
            
        # Skip if title already exists (backup check)
        safe_title = "".join(c for c in title if c.isalnum() or c in ' -_').strip()[:60]
        if safe_title in existing_posts:
            continue
            
        new_posts.append(post)
    
    if not new_posts:
        print("No new posts found to sync.")
        return []
    
    print(f"Found {len(new_posts)} new posts to sync...")
    
    # Create markdown files for new posts
    for post in new_posts:
        try:
            result = create_markdown_file(post, content_db)
            synced.append(result)
            print(f"✓ Synced: {result['title']} ({result['type']})")
        except Exception as e:
            print(f"✗ Error syncing post {post.get('fieldData', {}).get('name', 'Unknown')}: {e}")
    
    # Update master index
    if synced:
        update_master_index(synced)
        
        # Print summary
        print(f"\n{'='*50}")
        print(f"Sync completed! Added {len(synced)} new posts:")
        
        types = {}
        for item in synced:
            t = item['type']
            types[t] = types.get(t, 0) + 1
            
        for t, count in types.items():
            print(f"  - {t}: {count}")
            
        print(f"\nFiles saved to: {content_db}")
    
    return synced

if __name__ == "__main__":
    main()