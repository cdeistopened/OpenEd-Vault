#!/usr/bin/env python3
"""Debug script to see raw API responses"""

import os
import requests
import json
from dotenv import load_dotenv
from pathlib import Path

# Load environment
load_dotenv(Path(__file__).parent.parent / '.env')

api_key = os.getenv('GETLATE_API_KEY')
if not api_key:
    print("No API key found")
    exit(1)

base_url = "https://getlate.dev/api/v1"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

print("Testing Get Late API...")
print("=" * 50)

# Test 1: Get profiles
print("\n1. GET /profiles")
try:
    response = requests.get(f"{base_url}/profiles", headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Error: {e}")

# Test 2: Create profile
print("\n2. POST /profiles")
try:
    data = {
        "name": "OpenEd Vault",
        "description": "Alternative education content hub"
    }
    response = requests.post(f"{base_url}/profiles", headers=headers, json=data)
    print(f"Status: {response.status_code}")
    result = response.json()
    print(f"Response: {json.dumps(result, indent=2)}")
    
    # Extract profile ID if created
    if response.status_code == 200 or response.status_code == 201:
        profile_id = result.get('id') or result.get('data', {}).get('id')
        print(f"\nProfile ID: {profile_id}")
        
        # Test 3: Get accounts
        if profile_id:
            print(f"\n3. GET /accounts?profileId={profile_id}")
            response = requests.get(f"{base_url}/accounts?profileId={profile_id}", headers=headers)
            print(f"Status: {response.status_code}")
            print(f"Response: {json.dumps(response.json(), indent=2)}")
            
            # Test OAuth URL
            print(f"\n4. GET /connect/twitter?profileId={profile_id}")
            response = requests.get(f"{base_url}/connect/twitter?profileId={profile_id}", headers=headers)
            print(f"Status: {response.status_code}")
            if response.status_code == 200:
                print(f"Response: {json.dumps(response.json(), indent=2)}")
            else:
                print(f"Response text: {response.text}")
            
except Exception as e:
    print(f"Error: {e}")
    if hasattr(e, 'response'):
        print(f"Response text: {e.response.text}")