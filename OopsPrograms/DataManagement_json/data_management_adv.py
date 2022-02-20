import json

class main():

    def json_operation(filename = 'grocery_main.json'):
        with open(filename, 'r+') as file:
            data = json.load(file)

            data["resource1"][0]["total_price"] = "1750"
            data["resource2"][0]["total_price"] = "725"
            data["resource3"][0]["total_price"] = "250"

            file.seek(0)

            json.dump(data, file, indent = 4)

class subClass(main):
    if __name__ == '__main__':

        main.json_operation()

    print("Successfully added total price for each grocery")

print("\n")
print("------End of program------")
