def mergeSort(array):      # Function to perform merge sorting operation
    if len(array) > 1:
        mid = len(array) // 2      # Finding the mid of the array
        left = array[:mid]       # Dividing the array elements
        right = array[mid:]        # into 2 halves
        mergeSort(left)        # Sorting the first half
        mergeSort(right)       # Sorting the second half

        i = j = k = 0

        while i < len(left) and j < len(right):        # Copy data to temp arrays L[] and R[]
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):       # Checking if any element was left
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


def printList(array):     # Function to print the list
    for i in range(len(array)):     # Traversing till the array length
        print(array[i], end=" ")
    print()


if __name__ == '__main__':      # Main code to run if it is true

    array = [0, 9856, 12, 116, 13, 5, 62, 79, 65874]       # Array list
    print("Given array is", end="\n")
    printList(array)         # Function calling

    mergeSort(array)            # Function calling
    print("Sorted array is: ", end="\n")
    printList(array)         # Function calling
