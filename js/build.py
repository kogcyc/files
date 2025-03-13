from jinja2 import Environment, FileSystemLoader
import markdown

# Set up the Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))  # Load templates from the current directory

# Load the template file
template = env.get_template('template.html')

# Define variables to pass into the template
content_md = """
# Hello, World!

This is a markdown block that will be converted to HTML.
"""

content_html = markdown.markdown(content_md)

# Corrected variable passing
data = ["title.html", "name.html", "items.html"]

# Render the template with properly formatted data
rendered_html = template.render(data=data, content_html=content_html)

# Save the output to an HTML file
with open("index.html", "w", encoding="utf-8") as f:
    f.write(rendered_html)

print("Template rendered successfully! Check index.html")
