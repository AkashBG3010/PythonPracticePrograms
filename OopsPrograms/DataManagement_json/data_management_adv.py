import json

with open('grocery_main.json') as file:
    data = json.load(file)

for resource in data['resources']:
    data["total_cost"] = "1000"

with open('new_grocery_main.json', 'w') as file:
    json.dump(data, file, indent=2)

# print(new_data)
