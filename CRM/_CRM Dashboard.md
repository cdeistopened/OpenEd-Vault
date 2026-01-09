---
type: crm-dashboard
updated: 2026-01-07 16:15
---

# CRM Dashboard

## Quick Stats
- **Total Contacts:** 382
- **Last Updated:** 2026-01-07 16:15

## Recent Contacts
```dataview
TABLE email, company, last_contact, total_exchanges
FROM "CRM/contacts"
WHERE type = "contact"
SORT last_contact DESC
LIMIT 25
```

## High Engagement (20+ exchanges)
```dataview
TABLE email, company, total_exchanges
FROM "CRM/contacts"
WHERE total_exchanges >= 20
SORT total_exchanges DESC
```

## Potential Contributors
```dataview
TABLE email, company, last_contact
FROM "CRM/contacts"
WHERE potential_contributor = true
SORT last_contact DESC
```

## By Company
```dataview
TABLE WITHOUT ID company as Company, length(rows) as Contacts
FROM "CRM/contacts"
WHERE company != ""
GROUP BY company
SORT length(rows) DESC
LIMIT 20
```

## Dormant (1+ year)
```dataview
TABLE email, last_contact, total_exchanges
FROM "CRM/contacts"
WHERE contains(tags, "dormant")
SORT total_exchanges DESC
LIMIT 25
```
