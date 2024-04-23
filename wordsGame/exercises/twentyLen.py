fin = open('wordsGame\words.txt')

for word in fin:
    if(len(word) > 19):
        print(word)