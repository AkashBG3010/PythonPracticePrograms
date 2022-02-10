num = int(input("Enter the power: "))
if num < 0:
    print("Please enter a positive integer")
elif num == 0:
    print("2^0 = 1")
elif num <= 31:
    for i in range(1, num+1):
        value = 2 ** i
        print("2^", i, "=", value)
else:
    print("Invalid input!")
print("----End of Program-----")