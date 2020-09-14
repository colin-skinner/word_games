word = ""

legal = True


with open(r'/Users/magi-nerv/Desktop/Menlo/ATCS/word_games/scrabble_words.txt') as scrabble:

    while legal:

        word = word + input("Add a character: ").upper()

        length = len(word)
        works = False;

        for line in scrabble:
            line = line.strip()
            if len(line) > length and line.startswith(word):
                works = True
                legal = True



    print(word + " isn't a valid word")
