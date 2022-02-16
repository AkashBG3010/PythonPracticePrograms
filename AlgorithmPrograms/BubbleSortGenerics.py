def bubbleSort(array):      # Function to array operation

    print("Sorted array by sorted generic in ascending: ", end="\n")
    generic_sorted1 = sorted(array)
    print(generic_sorted1)

    print("Sorted array by sorted generic in descending: ", end="\n")
    generic_sorted2 = sorted(array, reverse=True)
    print(generic_sorted2)


if __name__ == '__main__':
    array = [99, 34, 73, 1, 65234, 22, 11, 54, 985]     # Array to be sorted
    print("Array before Sorting :", array)

    bubbleSort(array)       # Function calling


print("------End of program------")
