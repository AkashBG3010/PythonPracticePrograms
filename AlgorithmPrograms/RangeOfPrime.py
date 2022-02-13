if __name__ == '__main__':

    start, end, i, j, flag = 0, 0, 0, 0, 0         # Declare the variables

    print("Enter lower(least) element of the interval: \n", end="")     # Ask user to enter lower value of interval
    start = int(input())  # Take input
    print(start)

    print("Enter upper(last) element of the interval: \n", end="")     # Ask user to enter upper value of interval
    end = int(input())  # Take input
    print(end)

    print("Prime numbers between", start, "and", end, "are: \n", end="")         # Print display message

    for i in range(start, end + 1):       # Traverse each number in the interval

        if i == 1:    # Skip 1 as 1 is neither prime nor composite
            continue
        flag = 1        # flag variable to tell if i is prime or not

        for j in range(2, i // 2 + 1):
            if i % j == 0:
                flag = 0
                break

        if flag == 1:     # flag = 1 means i is prime and flag = 0 means i is not prime
            print(i, end=" ")


print("----End of Program-----")