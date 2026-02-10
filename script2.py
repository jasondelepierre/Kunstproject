import json
import re

with open("drawing.json", "r") as f:
data = json.load(f)

tekst = json.dumps(data)

match = re.search(r"(\\d+) x (\\d+)", tekst)
if match:
print("Afmetingen gevonden:", match.group())
else:
print("Geen afmetingen gevonden")