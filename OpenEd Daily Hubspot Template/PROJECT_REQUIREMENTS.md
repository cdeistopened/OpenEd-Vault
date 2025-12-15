# OpenEd Daily Newsletter Template - Project Requirements

## Project Overview
Create a HubSpot email template for the OpenEd Daily newsletter that is fully editable within HubSpot's email editor while maintaining consistent styling and cross-client compatibility.

## Design Specifications

### Color Scheme
- **Primary Orange**: #f24915 (Thought category, buttons)
- **Primary Blue**: #03a4ea (Trend category, links)
- **Dark Gray**: #333 (Tool category, text)
- **Light Gray**: #e0e0e0 (borders)
- **Background**: #fff (white)
- **Light Blue Background**: #f8fdff (quick bites container)

### Typography
- **Headers (H1)**: System font stack, 24px, centered, #333 color
  - Font stack: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`
- **Body Text**: Serif font stack, 16px, 1.6 line-height, #333 color
  - Font stack: `Georgia, "Times New Roman", Times, serif`
- **H2 Headers**: System font stack, 20px, #333 color

### Layout Structure
- **Max Width**: 600px
- **Container Padding**: 20px
- **Article Cards**: White background, 1px gray border, 5px border-radius, box-shadow
- **Responsive**: Mobile-optimized with media queries

## Image Assets (PNG Format)

All images are hosted on HubSpot CDN at: `https://45961901.fs1.hubspotusercontent-na1.net/hubfs/45961901/Daily%20Images/`

### Required Images:
1. **Logo**: `DAILY.png` (350px max-width)
2. **Thought Icon**: `Thought.png` (20x20px in 40px circle)
3. **Trend Icon**: `Trend.png` (20x20px in 40px circle)
4. **Tool Icon**: `Tool.png` (20x20px in 40px circle)
5. **Paper Airplane**: `paper%20airplane.png` (90x90px)

### Image Requirements:
- PNG format for email client compatibility
- Explicit width/height attributes
- Emoji fallbacks in alt attributes (💡, 📈, 🔧, ✈️)
- Table-based centering for Gmail compatibility
- `display: block; margin: 0 auto;` for alignment

## Template Structure & HubSpot Modules

### 1. Header Section
- **Logo**: Centered, responsive
- **Forward Link**: "Forwarded this email? Subscribe" with link to https://opened.co/resources

### 2. Special Announcement (Optional)
- **Module**: `@hubspot/rich_text`
- **Label**: "Special Announcement"
- **Style**: Gray background (#f8f8f8), bordered container

### 3. Quick Bites Section
- **Title**: "3 QUICK BITES 🍎🍎🍎" (H2, system font)
- **Container**: Blue border (#03a4ea), light blue background
- **Three Modules**:
  - `{% module "thought_title" path="@hubspot/email_text", label="Thought Title" %}`
  - `{% module "trend_title" path="@hubspot/email_text", label="Trend Title" %}`
  - `{% module "tool_title" path="@hubspot/email_text", label="Tool Title" %}`
- **Category Labels**: Colored badges (THOUGHT=orange, TREND=blue, TOOL=gray)

### 4. Article Sections (3 Articles)
Each article requires:
- **Icon**: Centered above content using table-based layout
- **Single Module**: `@hubspot/rich_text` for combined title + content
- **Default Content**: H1 title + paragraph body
- **Styling**: Consistent fonts, colors, spacing

### 5. "You're All Caught Up" Section
- **Paper Airplane**: Clickable mailto link for forwarding
- **Title**: "You're all caught up!" (H2)
- **Description**: Encouragement text
- **Forward Button**: Blue button with mailto link

### 6. Footer
- **Unsubscribe Links**: `{{ unsubscribe_link }}` variable
- **Copyright**: `{{ year }} OpenEd`
- **Address**: Physical mailing address
- **Social Links**: Optional social media links

## Email Client Compatibility Requirements

### CSS Constraints
- **No Flexbox**: Use table-based layouts
- **No CSS Transforms**: Use table centering with `align="center"`
- **Inline Styles**: All styles must be inline for Gmail
- **Email-Safe Fonts**: System fonts only, no web fonts
- **!important Declarations**: Use for consistent styling

### HTML Requirements
- **Table-Based Centering**: For image alignment
- **Explicit Dimensions**: Width/height attributes on all images
- **Alt Text**: Meaningful alt text with emoji fallbacks
- **Responsive Meta**: Viewport meta tag for mobile

## HubSpot-Specific Requirements

### Module Configuration
- **Rich Text Modules**: Use `@hubspot/rich_text` for editable content
- **Email Text Modules**: Use `@hubspot/email_text` for simple text fields
- **Module Labels**: Clear, descriptive labels for editors
- **Default Content**: Meaningful placeholder content

### Template Variables
- **Unsubscribe**: `{{ unsubscribe_link }}`
- **Year**: `{{ year }}`
- **Standard Headers**: `{{ standard_header_includes }}`

### Editor Experience
- **Copy/Paste Support**: Maintain font styling when pasting
- **Markdown-Friendly**: H1 + paragraph structure for easy editing
- **Single Blocks**: Combined title + content modules for workflow efficiency

## CSS Implementation

### Font Enforcement
```css
/* Default styles for HubSpot rich text modules */
.hs-richtext p, 
.hs-richtext div,
.hs-richtext span {
    font-family: Georgia, "Times New Roman", Times, serif !important;
    font-size: 16px !important;
    line-height: 1.6 !important;
    color: #333 !important;
}

.hs-richtext h1,
h1 {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
    font-weight: 600 !important;
    font-size: 24px !important;
    text-align: center !important;
    color: #333 !important;
    margin-top: 10px !important;
    margin-bottom: 15px !important;
    line-height: 1.2 !important;
}

/* Ensure pasted content inherits these styles */
[contenteditable] p,
[contenteditable] div,
[contenteditable] span {
    font-family: Georgia, "Times New Roman", Times, serif !important;
    font-size: 16px !important;
    line-height: 1.6 !important;
    color: #333 !important;
}

[contenteditable] h1 {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
    font-weight: 600 !important;
    font-size: 24px !important;
    text-align: center !important;
    color: #333 !important;
    margin-top: 10px !important;
    margin-bottom: 15px !important;
    line-height: 1.2 !important;
}
```

### Responsive Design
```css
@media only screen and (max-width: 600px) {
    .container {
        width: 100% !important;
        padding: 10px !important;
    }
    .logo-container img {
        max-width: 250px !important;
        height: auto !important;
    }
    .article-card {
        width: 100% !important;
        box-sizing: border-box;
    }
    img {
        height: auto !important;
        max-width: 100% !important;
    }
}
```

## Image Centering Pattern (Gmail-Compatible)

```html
<!-- Use this pattern for all centered images -->
<table width="100%" cellpadding="0" cellspacing="0" border="0">
    <tr>
        <td align="center" style="text-align: center;">
            <div style="width: 40px; height: 40px; border-radius: 50%; display: inline-block; background-color: #f24915; text-align: center; line-height: 40px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);">
                <img src="[IMAGE_URL]" alt="[EMOJI_FALLBACK]" style="width: 20px; height: 20px; vertical-align: middle;" width="20" height="20"/>
            </div>
        </td>
    </tr>
</table>
```

## Testing Checklist

### Email Clients to Test
- [ ] Gmail (web + mobile)
- [ ] Outlook (desktop + web)
- [ ] Apple Mail (desktop + iOS)
- [ ] Android email apps
- [ ] Yahoo Mail
- [ ] Thunderbird

### Functionality Tests
- [ ] Images load correctly
- [ ] Images are centered
- [ ] Fonts render consistently
- [ ] Copy/paste maintains styling
- [ ] Unsubscribe links work
- [ ] Forward functionality works
- [ ] Responsive design works
- [ ] HubSpot modules are editable

## Known Issues & Solutions

### Issue: Images not loading in Gmail
**Solution**: Use PNG format hosted on reliable CDN, avoid SVG

### Issue: Images left-aligned in Gmail
**Solution**: Use table-based centering with `align="center"`

### Issue: Font changes when pasting
**Solution**: CSS with `!important` declarations and `[contenteditable]` selectors

### Issue: Flexbox/transforms stripped
**Solution**: Use table layouts and inline-block elements

## Success Criteria

1. **Visual Consistency**: Template looks identical across major email clients
2. **Image Reliability**: All images load consistently in Gmail and Outlook
3. **Font Persistence**: Fonts remain consistent when copying/pasting content
4. **Editor Usability**: HubSpot editors can easily update content without breaking layout
5. **Mobile Responsive**: Template adapts properly to mobile screens
6. **Accessibility**: Proper alt text and semantic HTML structure

## Next Steps

1. Create new HubSpot email template from scratch
2. Implement table-based layout structure
3. Add all required HubSpot modules with proper labels
4. Apply CSS with font enforcement rules
5. Test image loading and alignment
6. Verify copy/paste functionality
7. Test across all major email clients
8. Document any additional customizations needed

---

*This document captures all learnings from the original template development process and serves as a complete specification for recreating the OpenEd Daily newsletter template with optimal HubSpot and email client compatibility.*
