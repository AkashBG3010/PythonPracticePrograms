def primeRange(lowerLimit, upperLimit):     # function to check prime of range
    for i in range(lowerLimit, upperLimit + 1):     # Traverse each number in the interval

        if i == 1:      # Skip 1 as 1 is neither prime nor composite
            continue
        flag = 1        # flag variable to tell if i is prime or not

        for j in range(2, i // 2 + 1):      # Traverse each number in the interval
            if i % j == 0:
                flag = 0
                break

        if flag == 1:       # flag = 1 means i is prime and flag = 0 means i is not prime
            palindrome(i)


def palindrome(number):     # Function to check palindrome
    reverse = 0     # Variables
    temp = number

    while number > 0:       # Traverse each number in the interval
        remainder = number % 10
        reverse = (reverse * 10) + remainder
        number = number // 10

    if temp == reverse:     # if condition meets, then prints number
        print(temp)


lowerLimit = int(input("Enter the lower limit: \n"))        # Ask user to enter lower value of interval
upperLimit = int(input("Enter the upper limit: \n"))        # Ask user to enter upper value of interval

if lowerLimit & upperLimit > 0:     # Validating user Input
    primeRange(lowerLimit, upperLimit)      # Function calling
    print("Prime numbers which are Anagram and Palindrome between the given range are: ")
else:
    print("Please enter a valid input!")


print("----End of Program-----")
