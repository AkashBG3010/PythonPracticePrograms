def get_permutation(string, i=0):
    if i == len(string):
        print("".join(string))

    for j in range(i, len(string)):
        words = [c for c in string]

        words[i], words[j] = words[j], words[i]         # swap

        get_permutation(words, i + 1)


word = str(input("Enter a word: \n"))
print("Permutation combinations of ", word, "are: ")
get_permutation(word)


print("------End of program------")
