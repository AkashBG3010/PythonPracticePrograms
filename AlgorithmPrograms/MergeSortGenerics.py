def mergeSort(array):      # Function to perform merge sorting operation
    print("Sorted array by sorted generic in ascending: ", end="\n")
    generic_sorted1 = sorted(array)
    print(generic_sorted1)

    print("Sorted array by sorted generic in descending: ", end="\n")
    generic_sorted2 = sorted(array, reverse=True)
    print(generic_sorted2)


if __name__ == '__main__':      # Main code to run if it is true

    array = [0, 9856, 12, 116, 13, 5, 62, 79, 65874]       # Array list
    print("Given array is", end="\n")

    mergeSort(array)            # Function calling

print("------End of program------")
