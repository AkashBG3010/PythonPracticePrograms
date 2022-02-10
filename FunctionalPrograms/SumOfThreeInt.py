arr = []        # Initiating an array
count = 0       # Initiating Count variable
num = int(input("Enter the number of integers to be entered in the array: \n"))     # Reading user input
while count < num:      # Iterate till the given condition holds good
    element = int(input("Enter number: \n"))        # Reading the user input
    arr.append(element)     # Adding the element/input to the array
    count = count + 1       # Incrementing the counter
print(arr)     # Printing the entered inputs as an array

if len(arr) >= 3:   # Validating the condition
    print("The number list whose sum equals to '0'(Triplets) are: ")
    for i in range(0, int(len(arr))-2):     # Iterating for number-1 in a single triplet

        for j in range(i + 1, int(len(arr))-1):     # Iterating for number-2 in a single triplet

            for k in range(j + 1, int(len(arr))):       # Iterating for number-3 in a single triplet

                if arr[i] + arr[j] + arr[k] == 0:       # Checking the sum af all three number is equal to 0
                    print(arr[i], arr[j], arr[k])       # Printing the number/triplets
                    print("")
else:
    print("Array should contain minimum of 3 digits to perform this operation")     # Error statement

print("----End of Program-----")