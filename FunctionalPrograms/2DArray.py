import array as arr

rows = int(input("Enter the number of rows: \n"))
columns = int(input("Enter the number of columns: \n"))

if (rows > 0) & (columns > 0):
    print("2D-Array of", rows,"X",columns," is: ")
    arr = [[0] * columns] * rows
    arr[0][0] = 0  # method to add elements

    for row in arr:
        print(row)
else:
    print("Invalid input! Please enter non negative input only")

print("----End of Program-----")