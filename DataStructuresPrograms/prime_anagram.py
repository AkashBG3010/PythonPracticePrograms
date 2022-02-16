if __name__ == '__main__':

    a = 0
    b = 0
    i = 0
    j = 0
    list = []
    flag = 0  # Declaring the variables

    lower_bound = int(input("Enter lower bound of the interval: \n"))  # Read user input

    higher_bound = int(input("Enter upper bound of the interval: \n"))  # Read user input

    print("Prime numbers between", lower_bound, "and", higher_bound, "are :\n", end="")  # Print display message

    for i in range(lower_bound, higher_bound + 1):  # Traverse each number in the interval with the help of for loop

        if i == 1:   # Skip 1 as1 is neither prime nor composite
            continue
        flag = 1    # flag variable to tell if i is prime or not

        for j in range(2, i // 2 + 1):
            if i % j == 0:
                flag = 0
                break

        if flag == 1:   # flag = 1 means i is prime and flag = 0 means i is not prime
            list.append(i)

    print(list)
    converted_list = "{}".format(list)

    dict = {}

    for strVal in converted_list:

        key = ''.join(sorted(strVal))

        if key in dict.keys():
            dict[key].append(strVal)
        else:
            dict[key] = []
            dict[key].append(strVal)

    output = ""
    for key, value in dict.items():
        output = output + ' '.join(value) + ' '

    print("Anagram in the range ", lower_bound, "and", higher_bound, "prime numbers list are: ", output)


print("\n")
print("------End of program------")
