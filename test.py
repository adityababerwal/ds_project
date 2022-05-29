import json

with open('stations.json') as f:
    data = json.load(f)

with open('new_stations.json', 'w') as f:
    json.dump(data, f, indent=3)
