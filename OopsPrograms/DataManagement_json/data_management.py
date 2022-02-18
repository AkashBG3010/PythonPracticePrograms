import json     # importing the json library
from grocery_main import grocery_string  # importing grocery string


print("The type of json file is: ", type(grocery_string))        # Data type of grocery_string

# Sterilize
data = json.loads(grocery_string)       # To convert Json to python string
print("The type of file after conversion to python is: ", type(data))        # Data type of data
# print(data)     # printing the data on console

for resource in data['resources']:
    del resource['type']        # Deleting the type key

# Deserialize
with open('grocery_main.json', 'w') as file:
    new_data = json.dumps(data, file,  indent=2)       # To convert python object to json object

print("The contents in the inventory: ")
print(new_data)
print("Again, the type of json file is: ", type(grocery_string))


print("------End of program------")
