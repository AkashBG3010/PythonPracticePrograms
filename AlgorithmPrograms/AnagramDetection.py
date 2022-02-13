def areAnagram(string1, string2):     # function to check whether two strings are anagram
    len1 = len(string1)      # lengths of both strings
    len2 = len(string2)

    if len1 != len2:        # If length of both strings is not same, then they cannot be anagram
        return 0

    sorted_string1 = sorted(string1)      # Sort both strings
    sorted_string2 = sorted(string2)

    for i in range(0, len1):      # Compare sorted strings
        if sorted_string1[i] != sorted_string2[i]:
            return 0
    return 1


string1 = str(input("Enter the word1: \n"))
string2 = str(input("Enter the word2: \n"))

if areAnagram(string1, string2):        # Function Calling and printing result
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other")


print("------End of program------")
