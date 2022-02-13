def binarySearchAppr(array, start, end, word):      # check condition

    sorted_array = sort_array(array)

    if end >= start:  # If element is present at the middle
        mid = start + (end - start) // 2
        if sorted_array[mid] == word:  # If element is smaller than mid
            return mid
        elif sorted_array[mid] > word:  # Else the element greater than mid
            return binarySearchAppr(sorted_array, start, mid - 1, word)
        else:
            return binarySearchAppr(sorted_array, mid + 1, end, word)
    else:  # Element is not found in the array
        return -1


def sort_array(array):
    sorted_array = sorted(array)
    return sorted_array


array = ['cat', 'dog', 'bird', 'fish', 'elephant', 'horse', 'tiger', 'lion']
print("Array is: ", array)
start = 0       # Variables
end = len(array) - 1

word = str(input("Enter the word to be searched in the array: \n"))
result = binarySearchAppr(array, start, end, word)

if result != -1:
    print("Array after sorted: ", sort_array(array))
    print("Entered word-", word, " is present at index ", int(result))
else:
    print("Entered word-", word, " is not present in array")

print("------End of program------")
