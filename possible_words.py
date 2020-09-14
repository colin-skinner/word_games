

chars = input("What's ur word: ").upper() 
allWords = []



sortedWord = ''.join(sorted(chars))
print(sortedWord)


with open("scrabble_words.txt", 'r') as scrabble:
    
    for line in scrabble:

            organized = line.strip()
            organized = ''.join(sorted(organized))

            if sortedWord == organized:
                allWords.append(line)

print(allWords)
