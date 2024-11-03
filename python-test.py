import json

# Зчитування файлу spaces.json
with open('spaces.json', 'r') as file:
    data = json.load(file)

# Виведення всіх ID об'єктів "lists"
for folder in data['folders']:
    for lst in folder['lists']:
        print(lst['id'])

# Виведення space.name і space.id для lists, ім'я яких починається на "test"
for folder in data['folders']:
    for lst in folder['lists']:
        if lst['name'].startswith('test'):
            print(lst['space']['name'])
            print(lst['space']['id'])
