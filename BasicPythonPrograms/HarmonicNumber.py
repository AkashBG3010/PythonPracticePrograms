num = int(input("Enter the number: \n"))
harmonic = 1

if num < 0:
    print("Please enter a positive Integer")
elif num == 1:
    print("Harmonic value of ", num, "is: ", harmonic)
else:
    for value in range(2, num+1):
        harmonic = harmonic + (1 / value)

print("Harmonic value of ", num, "is: ", harmonic)

print("------End of program------")