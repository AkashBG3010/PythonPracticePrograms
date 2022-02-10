import array as arr

arr = []
count = 0
num = int(input("Enter the number of integers to be entered in the array: \n"))
while count < num:
    element = int(input("Enter number: \n"))
    arr.append(element)
    count = count + 1
print(arr)

if len(arr) >= 3:
    print("The number list whose sum equals to '0'(Triplets) are: ")
    for i in range(0, int(len(arr))-2):

        for j in range(i + 1, int(len(arr))-1):

            for k in range(j + 1, int(len(arr))):

                if arr[i] + arr[j] + arr[k] == 0:
                    print(arr[i], arr[j], arr[k])
                    print("")
else:
    print("Array should contain minimum of 3 digits to perform this operation")

print("----End of Program-----")