---
created: 2026-01-02
type: reference
tags:
  - social-media
  - api
  - automation
---

# GetLate.dev Setup Guide

## Overview
Late API: Unified social media scheduling across 12 platforms (Twitter, Instagram, TikTok, LinkedIn, Facebook, YouTube, etc.)

## Key Benefits
- **No OAuth complexity** - No need to set up individual developer apps  
- **Free tier available** - Can build/test without paid plan
- **White-label ready** - No Late branding visible to users
- **Unified API** - Single endpoint for all platforms

## Quick Setup

### 1. Get API Key
1. Sign up at https://getlate.dev
2. Grab your API key from dashboard

### 2. Create Profile
```bash
curl -X POST https://getlate.dev/api/v1/profiles \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "OpenEd Social", "description": "OpenEd social accounts"}'
```

### 3. Connect Social Accounts
```bash
curl "https://getlate.dev/api/v1/connect/twitter?profileId=PROFILE_ID" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### 4. Schedule Posts
```javascript
await fetch('https://getlate.dev/api/v1/posts', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    platforms: [{ platform: 'twitter', accountId: 'account-id' }],
    content: 'Post content here',
    scheduledFor: '2026-01-15T12:00:00Z'
  })
});
```

## Integration Ideas

- **Bookmark workflow** → Generate social posts → Schedule via Late
- **Newsletter content** → Social media teasers
- **Educational posts** → Multi-platform distribution

## Rate Limits
- **Free**: 60 requests/minute
- **Paid tiers**: Up to 1,200 requests/minute

---

*Docs: https://getlate.dev/docs*
*Routed from Life OS inbox 2026-01-03*
