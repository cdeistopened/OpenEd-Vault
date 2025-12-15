import pynliner

def create_hubspot_template():
    """Reads the HTML and CSS files, inlines the CSS, and saves the result to a new file."""
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()

        with open('styles.css', 'r', encoding='utf-8') as f:
            css_content = f.read()

        # Remove all <link> tags to prevent pynliner from making any network requests
        html_cleaned = html_content.replace('<link rel="stylesheet" href="styles.css">', '')
        html_cleaned = html_cleaned.replace('<link rel="preconnect" href="https://fonts.googleapis.com">', '')
        html_cleaned = html_cleaned.replace('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>', '')
        html_cleaned = html_cleaned.replace('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Merriweather:wght@400;700&display=swap" rel="stylesheet">', '')

        # Create a Pynliner object and set the content
        p = pynliner.Pynliner()
        inlined_html = p.from_string(html_cleaned).with_cssString(css_content).run()

        # Write the inlined HTML to a new file
        with open('hubspot_template.html', 'w', encoding='utf-8') as f:
            f.write(inlined_html)

        print("Successfully created hubspot_template.html with inlined CSS.")

    except FileNotFoundError as e:
        print(f"Error: {e}. Make sure index.html and styles.css are in the same directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    create_hubspot_template()
