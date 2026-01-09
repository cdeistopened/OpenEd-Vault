#!/usr/bin/env python3
"""
Webflow Sync Controller - Uses Rube MCP to fetch and sync new posts
Run this script to check for new Webflow content and sync to Master Content Database
"""

import json
import subprocess
import tempfile
from pathlib import Path
from datetime import datetime

def run_rube_mcp_fetch():
    """Use Rube MCP to fetch recent Webflow posts."""
    print("Fetching posts from Webflow via Rube MCP...")
    
    # Create a temporary Python script to run the Rube MCP commands
    temp_script = f'''
import json
import sys
sys.path.append("/Users/charliedeist/.claude/mcp")

# Import MCP tools (this is pseudocode - adjust based on actual MCP setup)
try:
    from mcp_rube import RUBE_MULTI_EXECUTE_TOOL
    
    # Fetch recent posts from Webflow
    tools = [{{
        "tool_slug": "WEBFLOW_LIST_COLLECTION_ITEMS",
        "arguments": {{
            "collection_id": "6805bf729a7b33423cc8a08c",
            "limit": 100,
            "sort_by": "lastUpdated", 
            "sort_order": "desc"
        }}
    }}]
    
    result = RUBE_MULTI_EXECUTE_TOOL(
        session_id="webflow_sync",
        tools=tools,
        thought="Fetching recent Webflow posts for content sync",
        current_step="FETCHING_POSTS",
        current_step_metric="1/1 fetch",
        sync_response_to_workbench=False,
        memory={{"webflow": ["Syncing posts to Master Content Database"]}}
    )
    
    # Output the result as JSON
    print(json.dumps(result, indent=2))
    
except Exception as e:
    print(f"Error: {{e}}")
    sys.exit(1)
'''

    # For now, let's create a simplified version that shows the structure
    # In practice, you'd integrate this with the actual Rube MCP Python SDK
    
    print("NOTE: This is a template - you'll need to integrate with actual Rube MCP SDK")
    print("For now, let's test with sample data...")
    
    # Return sample structure for testing
    sample_result = {
        "successful": True,
        "data": {
            "results": [{
                "response": {
                    "data": {
                        "items": [
                            {
                                "id": "sample_post_1",
                                "fieldData": {
                                    "name": "Sample New Blog Post",
                                    "slug": "sample-new-blog-post", 
                                    "post-type": ["6805d44048df4bd97a0754ed"],
                                    "summary": "This is a sample post for testing the sync",
                                    "content": "<p>Sample content here</p>",
                                    "published-date": "2026-01-03T00:00:00.000Z"
                                },
                                "createdOn": "2026-01-03T00:00:00.000Z",
                                "lastUpdated": "2026-01-03T00:00:00.000Z"
                            }
                        ]
                    }
                }
            }]
        }
    }
    
    return sample_result

def extract_webflow_data(rube_result):
    """Extract Webflow posts from Rube MCP response."""
    try:
        if not rube_result.get("successful"):
            print("Rube MCP request was not successful")
            return []
            
        # Navigate the Rube response structure
        results = rube_result.get("data", {}).get("results", [])
        if not results:
            print("No results found in Rube response")
            return []
            
        # Get the first result (our WEBFLOW_LIST_COLLECTION_ITEMS call)
        first_result = results[0]
        response_data = first_result.get("response", {}).get("data", {})
        items = response_data.get("items", [])
        
        print(f"Extracted {len(items)} posts from Rube response")
        return items
        
    except Exception as e:
        print(f"Error extracting Webflow data: {e}")
        return []

def main():
    """Main function to run the sync process."""
    print("Webflow Content Sync Started")
    print("=" * 40)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Step 1: Fetch data from Webflow via Rube MCP
    try:
        rube_result = run_rube_mcp_fetch()
        webflow_posts = extract_webflow_data(rube_result)
        
        if not webflow_posts:
            print("No posts retrieved from Webflow. Exiting.")
            return
            
    except Exception as e:
        print(f"Error fetching from Webflow: {e}")
        return
    
    # Step 2: Import and run the sync agent
    try:
        # Import the sync function from our agent
        import sys
        agent_path = Path(__file__).parent / "webflow_sync_agent.py"
        
        # Add the directory to Python path
        sys.path.insert(0, str(agent_path.parent))
        
        # Import the sync function
        from webflow_sync_agent import sync_new_webflow_posts
        
        # Run the sync
        synced_posts = sync_new_webflow_posts(webflow_posts)
        
        if synced_posts:
            print(f"\\n✅ Successfully synced {len(synced_posts)} new posts!")
        else:
            print("\\n✅ Sync completed - no new posts to add.")
            
    except Exception as e:
        print(f"Error running sync agent: {e}")
        return
    
    print("\\nWebflow sync completed!")

if __name__ == "__main__":
    main()