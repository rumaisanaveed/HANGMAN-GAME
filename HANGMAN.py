import random

def printWord(lst):
    for i in lst:
        print(i,end = " ")

def printUsedWords(usedWords):
    for i in usedWords:
        print(i,end = " ")

words = ["program","write","eat","candy","pakistan","love","programming","think","the","of","can","coding","python",
         "java","javascript","html","css","react","sad","true","math","physics","chemistry","are","am","this","fan",
         "jam","hat","turkey","dubai","jakarta","islamabad","toffee","coffee","tom","jerry"]
userPermission = "y"
while userPermission != "n":
    word = random.choice(words)
    randomWord = list(word)
    guessList = []
    for i in range(len(word)):
        guessList.append("-")
    missedWords = 0
    usedWords = []
    while guessList != randomWord:
        printWord(guessList)
        print()
        guess = input("Guess a letter of word:")
        usedWords.append(guess)
        if guess in word:
            count = word.count(guess)
            if count > 1:
                indexes = []
                for index,char in enumerate(word):
                    if char == guess:
                        indexes.append(index)
                for i in indexes:
                    guessList[i] = guess
            else:
                idx = word.index(guess)
                guessList[idx] = guess
        if guess not in word:
            print(guess,"is not in the word.")
            missedWords += 1
        print("You have used these words",end = " ")
        printUsedWords(usedWords)
        print()
        if missedWords == len(word):
            print(f"Oops!You lose.You don't have any more lives to play.")
            break
    print("The word is",word)
    if missedWords == 0:
        print("Congratulations! You won.You missed 0 time.")
    elif missedWords == 1:
        print(f"You missed {missedWords} time.")
    else:
        print(f"You missed {missedWords} times.")
    userPermission = input("Enter y to continue and n to exit :")
