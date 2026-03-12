from datetime import datetime
import re

def today():
    now = str(datetime.now().strftime("%B %-d, %Y"))
    return "date: " + now + "\n"

with open("draft.md") as draft:
    text = draft.read()

updated = re.sub(r'date:\s.*\n', today(), text, count=1)

with open("draft.md", 'w') as draft:
    fm.write(updated)

