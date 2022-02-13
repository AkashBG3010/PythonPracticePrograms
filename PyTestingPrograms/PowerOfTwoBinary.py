def swapNibbles(test_num):
    swapped = int((test_num & 0x0F) << 4 | (test_num & 0xF0) >> 4)
    print("Number after swapping Nibbles through bytes: \n", swapped)
    num = swapped
    return isPower(num)


def decimalToBinary(new_num):  # Function to calculation
    if new_num >= 1:
        decimalToBinary(new_num // 2)
    print(new_num % 2, end='')


def isPower(num):  # Find Log n in different bases and check if the value is an integer
    new_num = num
    if (num == 0):
        flag = 0
    while (num != 1):
        if (num % 2 != 0):
            flag = 0
        num = num // 2

    flag = 1

    if flag == 1:
        print(new_num, " is the power of 2")
    else:
        print(new_num, " is not the power of 2")

    print("Decimal value of ", new_num, "is: ")
    decimalToBinary(new_num)


test_num = int(input("Enter a two (or more) digit number: \n"))  # Reading User input

if test_num > 9:  # validating
    swapNibbles(test_num)  # Function calling
else:
    print("Entered number cannot be swapped!")  # Error message

print("\n")
print("----------End of Program-----------")
