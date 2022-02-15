from pythonds.basic import Deque


def input_data():  # Function to validate month input
    while True:
        try:
            aStting = str(input("Enter the word: \n"))
            return aStting
        except (ValueError, TypeError):
            print("Invalid input! Please try again..")
            continue

    return input_data()


def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


print(palchecker(input_data()))

print("------End of program------")
