import re

year = input("Enter a year: ")
if re.match("[0-9]{4}", year):
    if (int(year) % 400 == 0) and (int(year) % 100 == 0):
        print("{0} is a leap year".format(year))

    elif (int(year) % 4 == 0) and (int(year) % 100 != 0):
        print("{0} is a leap year".format(year))

    else:
        print("{0} is not a leap year".format(year))
else:
    print("Please enter the correct year format")

print("----End of Program-----")