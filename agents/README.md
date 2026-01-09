# OpenEd Vault Agents

Automation agents for content management and workflow optimization.

## 📁 Structure

```
agents/
├── webflow_sync_agent.py      # Core Webflow sync logic
├── webflow_mcp_sync.py        # Test runner with sample data
├── run_webflow_sync.py        # Rube MCP integration template
├── webflow_sync_command.py    # Slash command handler
├── schedule_webflow_sync.py   # Scheduling setup utility
└── README.md                  # This file
```

## 🔄 Webflow Content Sync Agent

Automatically syncs new posts from Webflow CMS to the Master Content Database.

### Features
- Fetches new posts via Rube MCP integration
- Converts HTML content to markdown
- Organizes by type (Blog Posts, Daily Newsletters, Podcasts, Announcements)  
- Prevents duplicates using webflow_id tracking
- Updates Master_Content_Index.md automatically
- Preserves existing content structure

### Usage

**Slash Command:**
```bash
/sync-webflow           # Show usage info
/sync-webflow --test    # Run with sample data
/sync-webflow --stats   # Show content database stats
/sync-webflow --dry-run # Preview what would be synced
```

**Direct Execution:**
```bash
cd agents/
python3 webflow_mcp_sync.py    # Test with sample data
python3 webflow_sync_command.py --stats  # Show current stats
```

**Scheduling:**
```bash
python3 schedule_webflow_sync.py  # Set up weekly automation
```

### Integration with Rube MCP

The agent is designed to work with Rube MCP's Webflow integration:

1. **Fetch posts** via `WEBFLOW_LIST_COLLECTION_ITEMS`
2. **Filter for new content** using existing post tracking
3. **Process and convert** HTML to markdown with proper frontmatter
4. **Organize into folders** by content type
5. **Update index** with new content stats

### Content Database Structure

Posts are organized into:
- `Blog Posts/` - Articles and long-form content
- `Daily Newsletters/` - Daily newsletter content  
- `Podcasts/` - Podcast episodes and transcripts
- `Announcements/` - Important updates and announcements
- `Other/` - Miscellaneous content

### Output Format

Each post becomes a markdown file with:
- YAML frontmatter (title, URL, type, date, summary, webflow_id)
- Clean markdown content converted from HTML
- Proper linking and formatting
- Metadata for tracking and organization

### Scheduling Options

**Cron (Linux/macOS):**
```bash
# Weekly on Sunday at 6 AM
0 6 * * 0 cd '/path/to/agents' && python3 webflow_mcp_sync.py
```

**macOS LaunchAgent:**
Use `schedule_webflow_sync.py` to create a proper LaunchAgent plist.

**Manual:**
Run as needed during content review sessions.

## 🔧 Configuration

The sync agent uses:
- Webflow collection ID: `6805bf729a7b33423cc8a08c` (main posts)
- Post type mappings from existing seomachine config
- Master Content Database path resolution
- Duplicate prevention via webflow_id tracking

## 📊 Monitoring

- Check `/tmp/webflow_sync.log` for scheduled run output
- Use `--stats` flag to see current content counts  
- Master_Content_Index.md shows last sync time and totals

## 🚀 Future Enhancements

- Real-time Rube MCP integration (currently uses test data)
- Incremental sync based on lastUpdated timestamps
- Content validation and quality checks
- Automated tagging and categorization
- Slack/email notifications for new content
- Integration with other CMSs beyond Webflow

---

*Part of the OpenEd Vault automation ecosystem*