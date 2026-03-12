import json
from string import Template

with open('draft-template.md', 'r', encoding='utf-8') as draft:
	content = draft.read()

with open('names.json', 'r') as namesdata:
	names = json.load(namesdata)

tmpl = Template(content)
out = tmpl.substitute(names)

print(out)
