#A simple exercise that whe gonna show letter by letter a string in reverse mode

def reverse_word(word):
    index = 1

    while index <= len(word):
        print(word[len(word) - index])
        index += 1

word = input('choose an word to reverse: ')
reverse_word(word)