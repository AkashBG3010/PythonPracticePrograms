import random
list = [1,2]    # initiated variables
tail_counter = 0
head_counter = 0

num = int(input("Enter the number of times the coin to be flipped: "))  # user input
for values in range(num):  # Iterating for given number of times
    if random.choice(list) == 1:
        tail_counter = tail_counter + 1
    else:
        head_counter = head_counter + 1

totalCount = num
tailPercentage = (tail_counter / totalCount) * 100  # Calculating tails percentage
headPercentage = (head_counter / totalCount) * 100  # Calculating heads percentage
print("Total tail count is: ",tail_counter,"and the percentage is:",tailPercentage)
print("Total head count is: ",head_counter,"and the percentage is:",headPercentage)

print("----End of Program-----")