import json

# Read the contents of the JSON file
with open('bank_customer.json', 'r') as file:
    json_data = json.load(file)

data_list = list(json_data)

print(data_list)