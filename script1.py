import json

with open("drawing.json", "r") as f:
data = json.load(f)

print("Tekening info geladen:")
print(data)