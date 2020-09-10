

chars = input("What's ur word (capitals please): ")

#sortedList = []
allWords = []

sortedWord = ''.join(sorted(chars))
print(sortedWord)


with open("scrabble_words.txt", 'r') as scrabble:
    
    for i in scrabble:
        temp = i.strip()
        temp = ''.join(sorted(temp))
        print(temp)

        
        
