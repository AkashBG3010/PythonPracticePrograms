import json  # importing the json library
from grocery_main import grocery_string  # importing grocery string


class main:

    def json_operation(self):
        print("The type of json file is: ", type(self))  # Data type of grocery_string

        # Serialize
        data = json.loads(self)  # To convert Json to python string
        print("The type of file after conversion to python is: ", type(data))  # Data type of data

        # print(data)     # printing the data on console

        for resource in data['resources']:
            del resource['type']  # Deleting the type key

            # Deserialize
        with open('grocery_main.json', 'w') as file:
            new_data = json.dumps(data, indent=2)  # To convert python object to json object

            print("The contents in the inventory: ")
            print(new_data)
            print("Again, the type of json file is: ", type(self))


if __name__ == '__main__':

    main.json_operation(grocery_string)


print("------End of program------")
