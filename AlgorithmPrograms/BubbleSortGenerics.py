def bubbleSort(array):      # Function to array operation
    n = len(array)

    for i in range(n):  # Traverse through all array elements
        swapped = False  # Last i elements are already in place

        for j in range(0, n - i - 1):  # traverse the array from 0 to n-i-1. Swap if the element

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True  # found is greater than the next element

        if not swapped:  # IF no two elements were swapped by inner loop, then break
            break


array = [99, 34, 73, 1, 65234, 22, 11, 54, 985]     # Array to be sorted
print("Array before Sorting :", array)

bubbleSort(array)       # Function calling

print("Array After Sorting :")
for i in range(len(array)):     # printing each elements after sorting
    print("%d" % array[i], end=" ")

print("------End of program------")
