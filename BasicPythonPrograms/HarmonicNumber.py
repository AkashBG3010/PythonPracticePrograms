num = int(input("Enter the number: \n"))  # Read User Input
harmonic = 1  # Variable

if num < 0:  # Checking for conditions
    print("Please enter a positive Integer")        # Error statement
elif num == 1:
    print("Harmonic value of ", num, "is: ", harmonic)
else:
    for value in range(2, num+1):  # Iterating for number of times
        harmonic = harmonic + (1 / value)  # Calculating value of harmonic

print("Harmonic value of ", num, "is: ", harmonic)  # Printing result

print("------End of program------")