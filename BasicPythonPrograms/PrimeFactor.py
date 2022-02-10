num = int(input("Enter a Number: \n"))      # Reading User Input
if num < 0:
    print("Please enter a positive integer")       # Checking for non-negative Input

elif num == 1:
    print("1 is not a prime number, So it do not have any prime factors")        # Checking if number is 1

else:
    print("Prime Factors of ", num, "are: ")
    for i in range(2, num + 1):     # Iterating till the user input
        if num % i == 0:    # Checking if number is divisible and remainder is 0
            count = 1
            for j in range(2, (i // 2 + 1)):    # Iterating till the condition holds good
                if (i % j == 0):        # Checking if number is divisible
                    count = 0
                    break
            if (count == 1):        # Checking the condition
                print(i)        # printing the values

print("----End of Program-----")
