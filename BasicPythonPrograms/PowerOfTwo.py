num = int(input("Enter the power: "))  # Reading User Input
if num < 0:  # Checking for non-negative Input
    print("Please enter a positive integer")
elif num == 0:  # checking if power is 0
    print("2^0 = 1")
elif num <= 31:  # checking for givan condition
    for i in range(1, num+1):   # Iterating till the user input
        value = 2 ** i      # calculating power of two
        print("2^", i, "=", value)      # printing the output
else:
    print("Invalid input!")  # Error statement
print("----End of Program-----")