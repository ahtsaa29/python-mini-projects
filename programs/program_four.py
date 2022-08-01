# Remove first n characters from a string


def remove_char():
    word = input("please enter a word: ")
    num = int(input("trim from ?? "))
    print(word)
    x = word[num:]
    return x


print(remove_char())
