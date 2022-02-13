def calculatePayment(principal, rate, years):      # Function to calculation
    p = principal       # Variables
    r = rate / (12 * 100)
    n = years * 12

    numerator = p * r        # Calculations using the formula
    dinominator = 1 - (1 + r) ** (-n)
    payment = numerator / dinominator

    print("The Monthly payment is: ", round(payment))        # Printing result


principal = int(input("Enter the principal amount: \n"))       # Reading User input
if 0 < principal:       # validating for principle
    years = int(input("Enter the number of years: \n"))       # Reading User input
else:
    print("Invalid Input! Please try again")        # Error message

if 0 < years:       # validating for years
    rate = int(input("Enter the rate of interest in percentage : \n"))     # Reading User input
else:
    print("Invalid Input! Please try again")        # Error message

if 0 < rate < 100:       # validating for rate of interest
    print("Calculating the mortgage amount for: ")
    print("Total Principal amount : ", principal)        # Printing the entered details
    print("Total number of years : ", years)
    print("Rate of Interest per month : ", rate)

    calculatePayment(principal, rate, years)     # Function calling
else:
    print("Invalid Input! Please try again")        # Error message


print("------End of program------")