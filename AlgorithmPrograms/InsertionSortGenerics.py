def insertionSort(array):       # Function to array operation

    print("Sorted array by sorted generic in ascending: ", end="\n")
    generic_sorted1 = sorted(array)
    print(generic_sorted1)

    print("Sorted array by sorted generic in descending: ", end="\n")
    generic_sorted2 = sorted(array, reverse=True)
    print(generic_sorted2)


if __name__ == '__main__':

    array = ['grape', 'banana', 'strawberry', 'apple', 'peach', 'cherry']       # Array to be sorted
    print("Array before sorting: ", array)

    insertionSort(array)       # Function calling


print("------End of program------")
