def dayofweek(d, m, y):  # Function to calculation

    y0 = y - (14 - m) / 12  # Calculation using given formula
    x = y0 + y0 / 4 - y0 / 100 + y0 / 400
    m0 = m + 12 * ((14 - m) / 12) - 2
    d0 = (d + x + 31 * m0 / 12) % 7

    print("The day is: ", round(d0))  # Printing result


def isDayRange():   # Function to validate date input
    while True:
        try:
            day = int(input("Enter the day: \n"))
            if (day < 32) & (day > 0):
                return day
            else:
                print("Entered day is not valid! Try day range(1-31)")
                break
        except ValueError:
            print("Invalid input! Please try again..")
            continue

    return isDayRange()


def isMonthRange():     # Function to validate month input
    while True:
        try:
            month = int(input("Enter the month: \n"))
            if (month < 32) & (month > 0):
                return month
            else:
                print("Entered month is not valid! Try month range(1-12)")
                break
        except ValueError:
            print("Invalid input! Please try again..")
            continue

    return isMonthRange()


def isYearRange():      # Function to validate year input
    while True:
        try:
            year = int(input("Enter the year: \n"))
            if year > 0:
                return year
            else:
                print("Entered year is not valid! Try year range(>0)")
                break
        except ValueError:
            print("Invalid input! Please try again..")
            continue

    return isYearRange()


if __name__ == '__main__':      # Main method
    d = isDayRange()        # Function calling
    m = isMonthRange()      # Function calling
    y = isYearRange()       # Function calling
    print("------------------------------------------------------------")
    print("Entered Date is(DD/MM/YYYY): ", d, "/", m, "/", y)
    print("------------------------------------------------------------")
    dayofweek(d, m, y)       # Function calling
    print("------------------------------------------------------------")


print("------End of program------")
