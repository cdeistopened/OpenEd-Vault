#!/usr/bin/env python3
"""
Webflow Sync Scheduler - Sets up weekly sync automation
Creates cron job and provides scheduling options
"""

import os
import sys
from pathlib import Path
from datetime import datetime

def create_cron_job():
    """Create a cron job to run weekly sync."""
    agents_dir = Path(__file__).parent
    sync_script = agents_dir / "webflow_mcp_sync.py"
    
    # Cron command to run every Sunday at 6 AM
    cron_command = f"0 6 * * 0 cd '{agents_dir}' && python3 '{sync_script}' >> /tmp/webflow_sync.log 2>&1"
    
    print("📅 Webflow Sync Scheduler")
    print("=" * 30)
    print()
    print("To set up weekly Webflow sync, add this cron job:")
    print()
    print("1. Open terminal and run: crontab -e")
    print("2. Add this line:")
    print()
    print(f"   {cron_command}")
    print()
    print("3. Save and exit")
    print()
    print("Schedule Details:")
    print("- Runs every Sunday at 6:00 AM")
    print("- Logs output to /tmp/webflow_sync.log")
    print("- Uses your current Python environment")
    print()
    print("Alternative scheduling options:")
    print("- Daily at 8 AM:    0 8 * * *")
    print("- Twice weekly:     0 6 * * 1,4  (Monday & Thursday)")
    print("- Monthly:          0 6 1 * *     (1st of each month)")

def show_current_cron():
    """Show existing cron jobs."""
    print("\nCurrent cron jobs:")
    print("-" * 20)
    os.system("crontab -l")

def create_launchd_plist():
    """Create macOS LaunchAgent plist for scheduling (alternative to cron)."""
    agents_dir = Path(__file__).parent
    sync_script = agents_dir / "webflow_mcp_sync.py"
    
    plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.opened.webflow.sync</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>{sync_script}</string>
    </array>
    <key>WorkingDirectory</key>
    <string>{agents_dir}</string>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Weekday</key>
        <integer>0</integer>
        <key>Hour</key>
        <integer>6</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/tmp/webflow_sync.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/webflow_sync.log</string>
</dict>
</plist>"""
    
    plist_path = Path.home() / "Library/LaunchAgents/com.opened.webflow.sync.plist"
    
    print(f"\n🍎 macOS LaunchAgent Option")
    print("=" * 30)
    print()
    print("Alternative to cron: macOS LaunchAgent")
    print("More reliable on macOS, survives reboots")
    print()
    print("To install:")
    print(f"1. Create file: {plist_path}")
    print("2. Load with: launchctl load ~/Library/LaunchAgents/com.opened.webflow.sync.plist")
    print("3. Start with: launchctl start com.opened.webflow.sync")
    print()
    
    if input("Create LaunchAgent plist? (y/N): ").lower().startswith('y'):
        plist_path.parent.mkdir(exist_ok=True)
        plist_path.write_text(plist_content)
        print(f"✅ Created: {plist_path}")
        print("\nNext steps:")
        print("launchctl load ~/Library/LaunchAgents/com.opened.webflow.sync.plist")

def main():
    """Main scheduler setup."""
    print("Choose scheduling method:")
    print("1. Cron job (traditional Unix scheduling)")
    print("2. macOS LaunchAgent (recommended for macOS)")
    print("3. Show current scheduled jobs")
    print("4. Manual setup instructions")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == "1":
        create_cron_job()
    elif choice == "2":
        create_launchd_plist()
    elif choice == "3":
        show_current_cron()
    elif choice == "4":
        print("\n📋 Manual Setup Options")
        print("=" * 25)
        print("1. Run manually: python3 webflow_mcp_sync.py")
        print("2. Add to your weekly routine")
        print("3. Create Alfred/Shortcut workflow")
        print("4. Integrate with your existing automation")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()