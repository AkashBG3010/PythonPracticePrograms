def readFile():
    print("READING AND WRITING OF A FILE")
    print("------------------------------------------------------------")
    file = open(r"C:\Users\akash\PycharmProjects\DataStructuresPrograms\file_to_read.txt", "r")
    print("Reading a file and printing it---->")
    print(file.read())
    file.close()
    print("------------------------------------------------------------")

    print("Writing a file and printing it---->")
    file = open(r"C:\Users\akash\PycharmProjects\DataStructuresPrograms\file_to_read.txt", "w")
    file.write("1,2,3,4")
    file = open(r"C:\Users\akash\PycharmProjects\DataStructuresPrograms\file_to_read.txt", "r")
    print(file.read())
    file.close()
    print("------------------------------------------------------------")

    print("adding a element ""5"" to the file and printing it---->")
    file = open(r"C:\Users\akash\PycharmProjects\DataStructuresPrograms\file_to_read.txt", "a")
    file.write(",5")
    file = open(r"C:\Users\akash\PycharmProjects\DataStructuresPrograms\file_to_read.txt", "r")
    print(file.read())
    file.close()
    print("------------------------------------------------------------")


def searchInFile():
    file1 = open(r"C:\Users\akash\PycharmProjects\DataStructuresPrograms\file_to_search.txt", "r")
    print("Elements present in the file are: ")
    print(file1.read())
    print("------------------------------------------------------------")
    string = input("Enter something here to search in the file: ")

    if string in file1:
        print('String', string, 'is found in the file')
    else:
        print('String', string, 'is not found in the file')

    file1.close()

    print("------------------------------------------------------------")


if __name__ == '__main__':
    readFile()
    searchInFile()

    print("------End of program------")
