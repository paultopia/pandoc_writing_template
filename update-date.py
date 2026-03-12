from datetime import datetime
import re

def today():
    now = str(datetime.now().strftime('"%B %-d, %Y"'))
    return "date: " + now + "\n"

with open("draft.md", encoding="utf-8") as draft:
    text = draft.read()

updated = re.sub(r'date:\s.*\n', today(), text, count=1)

with open("draft.md", 'w', encoding="utf-8") as draft:
    draft.write(updated)

