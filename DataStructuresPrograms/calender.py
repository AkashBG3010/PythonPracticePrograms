import calendar


def calender(year, month):
    print(calendar.month(year, month))


if __name__ == '__main__':

    def isYearRange():  # Function to validate year input
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


    def isMonthRange():  # Function to validate month input
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


    year = isYearRange()
    month = isMonthRange()
    print("------------------------------------------------------------")
    calender(year, month)
    print("------------------------------------------------------------")

print("------End of program------")
