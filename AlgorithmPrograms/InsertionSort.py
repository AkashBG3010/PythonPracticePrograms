def insertionSort(array):       # Function to array operation
    print("Array after sorting: ")

    for i in range(1, len(array)):      # Traverse through all array elements
        tmp = array[i]
        j = i - 1;
        while j > 0 and array[j] > tmp:
            array[j + 1] = array[j]
            j = j - 1
            array[j + 1] = tmp
    print(array)        # Printing the elements of array


array = ['grape', 'banana', 'strawberry', 'apple', 'peach', 'cherry']       # Array to be sorted
print("Array before sorting: ", array)

insertionSort(array)       # Function calling


print("------End of program------")
