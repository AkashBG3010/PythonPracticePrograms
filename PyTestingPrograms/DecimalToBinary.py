def decimalToBinary(num):       # Function to calculate binary values
    if num >= 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')


if __name__ == '__main__':      # Main method starts
    dec_val = int(input("Enter the decimal value to be converted: \n"))  # reads decimal value from user
    if dec_val >= 1:
        print("Binary Value after converted: ")
        decimalToBinary(dec_val)  # Calling function
    else:
        print("Invalid Input!")

print("\n")
print("------End of program------")
