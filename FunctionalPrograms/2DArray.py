def array(rows, columns):       # Function for array operation
    if (rows > 0) & (columns > 0):
        print("2D-Array of", rows, "X", columns, " is: ")
        arr = [[0] * columns] * rows
        arr[0][0] = 0  # method to add elements

        for row in arr:
            print(row)
    else:
        print("Invalid input! Please enter non negative input only")        # Error Statement


rows = int(input("Enter the number of rows: \n"))       # Reads input from user
columns = int(input("Enter the number of columns: \n"))     # Reads input from user

array(rows, columns)        # Function Calling for array operation

print("----End of Program-----")
