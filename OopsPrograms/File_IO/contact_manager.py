def operations_file():

    with open('contact.txt', 'r') as file:      # To read the file. Here no need to close
        print("All the contents in the file: ")
        print("------------------------------------------------------------")
        for line in file:       # Efficient method to read
            print(line, end='')        # printing the contents of the file
    print("\n")
    print("------------------------------------------------------------")

    with open('text.txt', 'w') as new_file:
        new_file.write("Hello there!")


class main:
    operations_file()

# file_contents = file.read(100)     # to read first 100(size to read) characters of the file
# print(file.tell())        # to check the current position
# file_contents = file.read()     # to read all contents of the file
# file_contents = file.readline() # to read first line of the file
# file_contents = file.readlines() # to read contents of a file as list
# file = open('contact.txt', 'r')     # To read the file
# print(file.mode)        # to check the mode of opening file
# print(file.name)        # to check the name of the file
# file.close()        # closing the open file at the end explicitly

print("------End of program------")

