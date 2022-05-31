num = int(input("Enter a Number: \n"))
if num < 0:
	print("Please enter a positive integer")

elif num == 1:
    print("1 is not a prime number, So it does not have any prime factors")

else:
    print("Prime Factors of ",num, "are: ")
    for i in range(2, num + 1):
        if num % i == 0:
            count = 1
            for j in range(2, (i // 2 + 1)):
                if (i % j == 0):
                    count = 0
                    break
            if (count == 1):
                print(i)

print("----End of Program-----")
