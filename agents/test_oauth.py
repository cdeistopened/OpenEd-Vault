#!/usr/bin/env python3
"""Test OAuth connection flow"""

import os
import requests
import json
from dotenv import load_dotenv
from pathlib import Path

# Load environment
load_dotenv(Path(__file__).parent.parent / '.env')

api_key = os.getenv('GETLATE_API_KEY')
base_url = "https://getlate.dev/api/v1"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

print("Testing OAuth URLs for Get Late...")
print("=" * 50)

# Get existing profile
response = requests.get(f"{base_url}/profiles", headers=headers)
profiles_data = response.json()
profiles = profiles_data.get('profiles', [])

if not profiles:
    print("No profiles found!")
    exit(1)

# Use first profile (OpenEd Vault)
profile = profiles[0]
profile_id = profile.get('_id')
print(f"Using profile: {profile.get('name')} (ID: {profile_id})")

# Test each platform
platforms = ['twitter', 'linkedin', 'facebook', 'instagram', 'tiktok', 'youtube', 'pinterest']

print("\nTesting OAuth URLs:")
print("-" * 30)

for platform in platforms:
    print(f"\n{platform.upper()}:")
    try:
        # Try the connect endpoint
        url = f"{base_url}/connect/{platform}"
        params = {"profileId": profile_id}
        response = requests.get(url, headers=headers, params=params)
        
        print(f"  Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            oauth_url = data.get('url') or data.get('authUrl') or data.get('redirectUrl')
            if oauth_url:
                print(f"  OAuth URL: {oauth_url}")
            else:
                print(f"  Response: {json.dumps(data, indent=2)}")
        else:
            print(f"  Error: {response.text}")
            
    except Exception as e:
        print(f"  Exception: {e}")

# Also check accounts
print("\n\nChecking connected accounts:")
print("-" * 30)
response = requests.get(f"{base_url}/accounts", headers=headers, params={"profileId": profile_id})
print(f"Status: {response.status_code}")
if response.status_code == 200:
    accounts = response.json()
    print(f"Response: {json.dumps(accounts, indent=2)}")