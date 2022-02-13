def findNumber(high):
    low = 0
    mid = (low + high) / 2

    print("Enter your choice below: ")
    print("1) Number greater than ", mid)
    print("2) Number equal to ", mid)
    print("3) Number less than ", mid)
    choice = str(input())

    if choice == '1':
        if high - mid == 1:
            findNumber(high, high)
            return
        findNumber(mid, high)
        return

    elif choice == '2':
        print("Got the guessed number: ", mid)
        return

    elif choice == '3':
        findNumber(low, mid)
        return
    else:
        print("Invalid selection!")


print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print('"Please select any number and remember in mind"')
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

high = int(input("Enter the upper range : \n"))

findNumber(high)


print("------End of program------")
