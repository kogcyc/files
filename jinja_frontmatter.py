
import frontmatter
from jinja2 import Environment, BaseLoader

page ="""
---
title: Hello, world!
---
The is the conent of the character.
"""

template_string = """
<h2>Frontmatter Metadata:</h2>
<ul>
{% for key, value in metadata.items() %}
  <li><strong>{{ key }}:</strong> {{ value }}</li>
{% endfor %}
</ul>

{{ content }}

"""

template = Environment(loader=BaseLoader).from_string(template_string)

fm = frontmatter.loads(page)

rendered = template.render(metadata=fm.metadata,content=fm.content)

print(f"\n\n\n{rendered}\n\n\n")

