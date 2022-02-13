
def countCurrency(amount):      # Function to count notes and print the same
    notes = [2000, 500, 200, 100, 50, 20, 10, 5, 1]  # total list of currency notes
    note_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0]       # number of notes
    print("Currency notes list are: ")

    for i, j in zip(notes, note_counter):  # Greedy approach method
        if amount >= i:             # Zip function to compare total list of currency notes and number of notes
            j = amount // i
            amount = amount - j * i
            print(i, " : ", j)


amount = int(input("Enter the Amount to be withdrawn: \n"))     # Reads User input

if amount > 0:     # Validating if the entered is non-negative input
    countCurrency(amount)     # Function calling
else:
    print("Invalid Input!")     # Error message


print("------End of program------")
