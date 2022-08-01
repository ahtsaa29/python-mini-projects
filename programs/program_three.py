# Print characters from a string that are present at an even index number

word = input("please enter a word: ")

length = len(word)

for i in range(1, length, 2):
    print(word[i])
