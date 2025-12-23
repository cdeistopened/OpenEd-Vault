"""
Webflow CMS Integration for OpenEd Content Database
Pulls blog posts, podcasts, and newsletters from Webflow CMS API
and syncs them to local Obsidian-style markdown files with frontmatter.
"""

import os
import re
import requests
from datetime import datetime
from pathlib import Path
from html import unescape


def html_to_markdown(html_content):
    """
    Convert HTML content to markdown.
    Handles common Webflow rich text patterns.
    """
    if not html_content:
        return ''

    text = html_content

    # Remove style tags and their content
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)

    # Remove script tags and their content
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)

    # Remove embedded HTML documents (transcript widgets, etc.)
    text = re.sub(r'<div data-rt-embed-type=[\'"]true[\'"]>.*?</div>\s*(?=<[^d]|$)', '', text, flags=re.DOTALL)

    # Convert headers
    text = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n# \1\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n## \1\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n### \1\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<h4[^>]*>(.*?)</h4>', r'\n#### \1\n', text, flags=re.DOTALL | re.IGNORECASE)

    # Convert links
    text = re.sub(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', text, flags=re.DOTALL | re.IGNORECASE)

    # Convert bold/strong
    text = re.sub(r'<(strong|b)[^>]*>(.*?)</\1>', r'**\2**', text, flags=re.DOTALL | re.IGNORECASE)

    # Convert italic/em
    text = re.sub(r'<(em|i)[^>]*>(.*?)</\1>', r'*\2*', text, flags=re.DOTALL | re.IGNORECASE)

    # Convert unordered lists
    text = re.sub(r'<ul[^>]*>(.*?)</ul>', lambda m: '\n' + re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', m.group(1), flags=re.DOTALL | re.IGNORECASE) + '\n', text, flags=re.DOTALL | re.IGNORECASE)

    # Convert ordered lists
    def convert_ol(match):
        items = re.findall(r'<li[^>]*>(.*?)</li>', match.group(1), flags=re.DOTALL | re.IGNORECASE)
        return '\n' + '\n'.join(f'{i+1}. {item.strip()}' for i, item in enumerate(items)) + '\n'
    text = re.sub(r'<ol[^>]*>(.*?)</ol>', convert_ol, text, flags=re.DOTALL | re.IGNORECASE)

    # Convert paragraphs
    text = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', text, flags=re.DOTALL | re.IGNORECASE)

    # Convert line breaks
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)

    # Convert blockquotes
    text = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', lambda m: '\n> ' + m.group(1).strip().replace('\n', '\n> ') + '\n', text, flags=re.DOTALL | re.IGNORECASE)

    # Remove remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Decode HTML entities
    text = unescape(text)

    # Clean up whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = '\n'.join(line.strip() for line in text.split('\n'))

    return text.strip()


class WebflowCMS:
    """Interface with Webflow CMS API to sync content."""

    # Post type ID to name mapping from Webflow collection '6805d40bc0f4e1ed13b3b797'
    POST_TYPE_MAP = {
        '6812753c2611e43906dc13d6': 'announcements',
        '6805d5076ff8c966566279a4': 'daily',
        '6805d44048df4bd97a0754ed': 'blog',
        '6805d42ba524fabb70579f4e': 'podcast'
    }

    def __init__(self):
        self.api_key = os.getenv('WEBFLOW_API_KEY')
        self.site_name = os.getenv('WEBFLOW_SITE_NAME', 'open-ed')
        self.posts_collection_id = os.getenv('WEBFLOW_POSTS_COLLECTION_ID')
        self.base_url = 'https://api.webflow.com/v2'

        if not self.api_key:
            raise ValueError("WEBFLOW_API_KEY not found in environment variables")

        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'accept': 'application/json'
        }

    def resolve_post_type(self, post_type_ids):
        """Convert post-type reference IDs to actual type name."""
        if not post_type_ids:
            return 'unknown'
        # Take the first type if multiple
        type_id = post_type_ids[0] if isinstance(post_type_ids, list) else post_type_ids
        return self.POST_TYPE_MAP.get(type_id, 'unknown')

    def get_all_posts(self):
        """Fetch all posts from Webflow CMS with pagination."""
        all_items = []
        offset = 0
        limit = 100  # Max per request

        while True:
            url = f"{self.base_url}/collections/{self.posts_collection_id}/items"
            params = {'limit': limit, 'offset': offset}

            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()

            data = response.json()
            items = data.get('items', [])
            all_items.extend(items)

            # Check if we got all items
            pagination = data.get('pagination', {})
            total = pagination.get('total', 0)

            if len(all_items) >= total or len(items) < limit:
                break

            offset += limit

        return all_items

    def get_post_by_slug(self, slug):
        """Fetch a specific post by its slug."""
        posts = self.get_all_posts()
        for post in posts:
            if post.get('fieldData', {}).get('slug') == slug:
                return post
        return None

    def sync_to_obsidian(self, output_dir=None, include_content=True, organize_by_type=True):
        """
        Sync all Webflow content to Obsidian-style markdown files.
        Creates one markdown file per post with YAML frontmatter.

        Args:
            output_dir: Directory to save markdown files.
                       Defaults to Content/Master Content Database/
            include_content: Whether to include the full article content (default True)
            organize_by_type: Whether to organize files into subfolders by type (default True)
        """
        if output_dir is None:
            # Default to the vault's content database
            # Path: seomachine/data_sources/modules/webflow.py -> OpenEd Vault/Content/Master Content Database
            vault_root = Path(__file__).parent.parent.parent.parent.parent.parent
            output_dir = vault_root / "Content" / "Master Content Database"

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        posts = self.get_all_posts()
        synced = []

        for post in posts:
            field_data = post.get('fieldData', {})

            # Extract fields
            title = field_data.get('name', 'Untitled')
            slug = field_data.get('slug', '')
            post_type_ids = field_data.get('post-type', [])
            post_type = self.resolve_post_type(post_type_ids)
            meta_description = field_data.get('meta-description', '')
            summary = field_data.get('summary', '')
            published_date = field_data.get('published-date', '') or field_data.get('published-on', '')
            html_content = field_data.get('content', '')

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
            if post_type == 'podcast':
                url = f"https://opened.co/podcast/{slug}"
            elif post_type == 'daily':
                url = f"https://opened.co/newsletter/{slug}"
            elif post_type == 'announcements':
                url = f"https://opened.co/blog/{slug}"  # Announcements go to blog
            else:
                url = f"https://opened.co/blog/{slug}"

            # Escape quotes for YAML
            escaped_title = title.replace('"', "'")
            escaped_meta = meta_description.replace('"', "'")
            escaped_summary = summary.replace('"', "'")
            webflow_id = post.get('id', '')
            sync_time = datetime.now().strftime('%Y-%m-%d %H:%M')

            # Convert HTML content to markdown
            markdown_content = html_to_markdown(html_content) if include_content and html_content else ''

            # Create frontmatter and content
            file_content = f"""---
title: "{escaped_title}"
url: {url}
slug: {slug}
type: {post_type}
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

            # Organize into subfolders by type
            if organize_by_type:
                # Map types to folder names
                type_folders = {
                    'daily': 'Daily Newsletters',
                    'blog': 'Blog Posts',
                    'podcast': 'Podcasts',
                    'announcements': 'Announcements',
                    'unknown': 'Other'
                }
                subfolder = type_folders.get(post_type, 'Other')
                type_dir = output_dir / subfolder
                type_dir.mkdir(parents=True, exist_ok=True)
                filepath = type_dir / filename
            else:
                filepath = output_dir / filename

            filepath.write_text(file_content, encoding='utf-8')

            synced.append({
                'title': title,
                'url': url,
                'type': post_type,
                'file': str(filepath),
                'has_content': bool(markdown_content)
            })

        return synced

    def get_content_summary(self):
        """Get a summary of all content in Webflow CMS."""
        posts = self.get_all_posts()

        summary = {
            'total': len(posts),
            'by_type': {},
            'recent': []
        }

        for post in posts:
            field_data = post.get('fieldData', {})
            post_type_ids = field_data.get('post-type', [])
            post_type = self.resolve_post_type(post_type_ids)

            if post_type not in summary['by_type']:
                summary['by_type'][post_type] = 0
            summary['by_type'][post_type] += 1

        # Get 5 most recent
        sorted_posts = sorted(
            posts,
            key=lambda x: x.get('fieldData', {}).get('published-on', ''),
            reverse=True
        )[:5]

        for post in sorted_posts:
            field_data = post.get('fieldData', {})
            post_type_ids = field_data.get('post-type', [])
            summary['recent'].append({
                'title': field_data.get('name', 'Untitled'),
                'type': self.resolve_post_type(post_type_ids),
                'date': field_data.get('published-on', '')[:10] if field_data.get('published-on') else ''
            })

        return summary


def sync_content_database(verbose=True, include_content=True):
    """
    Main function to sync Webflow content to local Obsidian database.
    Call this at the start of podcast/daily/weekly sessions.
    Also generates content-index.csv for quick reference.

    Args:
        verbose: Print progress messages
        include_content: Include full article content (default True)
    """
    import csv
    from dotenv import load_dotenv

    # Load env from seomachine config
    env_path = Path(__file__).parent.parent / "config" / ".env"
    load_dotenv(env_path)

    webflow = WebflowCMS()

    if verbose:
        print("Syncing Webflow CMS to local content database...")
        print("=" * 50)

    synced = webflow.sync_to_obsidian(include_content=include_content)

    # Also generate CSV index for quick reference
    csv_path = Path(__file__).parent.parent / "config" / ".." / "context" / "content-index.csv"
    csv_path = csv_path.resolve()
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['title', 'url', 'type', 'date', 'summary'])
        for item in synced:
            # Get summary from the synced data - need to re-fetch since we don't store it
            pass

    # Re-fetch posts for CSV (synced doesn't include summary)
    posts = webflow.get_all_posts()
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['title', 'url', 'type', 'date', 'summary'])
        for post in posts:
            field_data = post.get('fieldData', {})
            title = field_data.get('name', '')
            slug = field_data.get('slug', '')
            post_type_ids = field_data.get('post-type', [])
            post_type = webflow.resolve_post_type(post_type_ids)
            summary = field_data.get('summary', '')
            published_date = field_data.get('published-date', '') or field_data.get('published-on', '')
            date_str = published_date[:10] if published_date and len(published_date) >= 10 else ''

            if post_type == 'podcast':
                url = f'https://opened.co/podcast/{slug}'
            elif post_type == 'daily':
                url = f'https://opened.co/newsletter/{slug}'
            else:
                url = f'https://opened.co/blog/{slug}'

            writer.writerow([title, url, post_type, date_str, summary])

    if verbose:
        print(f"Updated content-index.csv")

    if verbose:
        print(f"Synced {len(synced)} items:")
        types = {}
        with_content = 0
        for item in synced:
            t = item['type']
            types[t] = types.get(t, 0) + 1
            if item.get('has_content'):
                with_content += 1
        for t, count in types.items():
            print(f"  - {t}: {count}")
        print(f"  - With content: {with_content}/{len(synced)}")
        print(f"\nFiles saved to: Content/Master Content Database/")

    return synced


if __name__ == "__main__":
    sync_content_database()
