import json
from string import Template
from datetime import datetime

with open('names.json', 'r') as namesdata:
	names = json.load(namesdata)

now = str(datetime.now().strftime('"%B %d, %Y"'))
names["date"] = now

with open('draft-template.md', 'r', encoding='utf-8') as draftdata:
	draft_tmpl = draftdata.read()

draft_template = Template(draft_tmpl)
draft_content = draft_template.substitute(names)

with open('quickbuild-template', 'r', encoding='utf-8') as quickbuilddata:
	quickbuild_tmpl = quickbuilddata.read()

quickbuild_template = Template(quickbuild_tmpl)
quickbuild_content = quickbuild_template.substitute(names)

with open('draft.md', 'w', encoding='utf-8') as draftout:
	draftout.write(draft_content)

with open('quickbuild', 'w', encoding='utf-8') as quickbuildout:
	quickbuildout.write(quickbuild_content)