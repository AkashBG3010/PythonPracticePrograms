rows = int(input("Enter the number of rows: \n"))  # reading user input for number of rows
columns = int(input("Enter the number of columns: \n"))     # reading user input for number of columns

if (rows > 0) & (columns > 0):  # Checking for-non negative input
    print("2D-Array of", rows,"X",columns," is: ")  # printing the entered values
    arr = [[0] * columns] * rows    # Initiating an array with specified rows and columns
    arr[0][0] = 0  # method to add elements

    for row in arr:  # Iterating for each rows in the array
        print(row)      # printing each row of elements in the array
else:
    print("Invalid input! Please enter non negative input only")  # Error Statement

print("----End of Program-----")