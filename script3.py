import json

with open("artist.json", "r") as f:
data = json.load(f)

print("Kunstenaar info:")
print(data)