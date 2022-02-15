from lib2to3.pytree import Node

from pythonds import Stack

obj = Stack()  # Creating object of stack class


class Prime:
    prime = {}
    prime_anagram = []  # Creating prime_anagram list

    prime_list = prime.prime(0, 1000)  # Creating list of prime number in given range

    for num in prime_list:  # Checking prime number anagram or not

        if num <= 10:
            continue
        number = prime.anagram(num)
        if prime.prime_check(number) and 0 <= number <= 1000:
            prime_anagram.append(number)
            prime_anagram.append(num)
            prime_list.remove(number)

    length = len(prime_anagram)  # finding the length of prime anagram list

    for number in range(length):  # Adding the prime anagram in to stack
        num = Node(prime_anagram[number])
        obj.push(num)

    for number in range(length):  # Printing in reverse order
        data = obj.pop()
        print(data, end=" ")


print("------End of program------")
