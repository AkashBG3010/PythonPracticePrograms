def squareRoot(number):  # Function to return the square root
    c = number  # Variables
    count = 0
    l = 0.00001        # (epsilon = 1e-15 ) Constant Tolerance level

    while 1:  # Newtons method
        root = 0.5 * (c + (number / c))  # Calculate more closed x
        count += 1

        if abs(root - c) < l:  # Validating for closeness
            break
        c = root
    return round(root)  # returning root as output


number = int(input("Enter the square root number: \n"))  # Reading User input
if number > 0:  # validating input
    print("The root is: ")
    print(squareRoot(number))  # Function calling
else:
    print("Invalid Input!")  # Error message


print("------End of program------")
