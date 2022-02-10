import re

year = input("Enter a year: ")  # Reading User Input
if re.match("[0-9]{4}", year):  # Validating to match the given condition with regex
    if (int(year) % 400 == 0) and (int(year) % 100 == 0):  # leap yer condition
        print("{0} is a leap year".format(year))

    elif (int(year) % 4 == 0) and (int(year) % 100 != 0):  # leap yer condition
        print("{0} is a leap year".format(year))

    else:
        print("{0} is not a leap year".format(year))  # Printing the final statement
else:
    print("Please enter the correct year format")       # Error statement

print("----End of Program-----")