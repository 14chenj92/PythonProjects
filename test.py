import random
wordlist = ["books","painting","animals"] # change curly braces to brackets

def getword ():
    return random.choice(wordlist).upper()

def play (word):
    wordcompletion = "_"*len(word)
    guessed = False
    guessedletters = []
    guessedwords = []
    tries = 6
    print("Let's play Hangman")

    while not guessed and tries > 0:
        print(display_hangman(tries))
        print("Word:",wordcompletion)
        print("Guessed Letters:", ",".join(guessedletters))
        guess = input("Please guess a letter").upper()

        if len (guess) == 1 and guess.isalpha():
            if guess in guessedletters :
                print("You already guessed this letter")
            elif guess not in word :
                print(guess,"is not in the word")
                tries -= 1
                guessedletters.append(guess)
            else :
                print("Good job!",guess,"is in the word")
                guessedletters.append(guess)
                wordaslist = list(wordcompletion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    wordaslist[index] = guess
                wordcompletion = "".join(wordaslist)
                if "_" not in wordcompletion:
                    guessed = True 
        elif len(guess) == len(word)and guess.isalpha() :
            if guess in guessedwords:
                print("You already guessed the word")
            elif guess != word:
                print(guess, " is not the word")
                tries -= 1
                guessedletters.append(guess)
            else :
                guessed = True
                wordcompletion = word
        else :
            print("Not a valid guess")

    print(display_hangman(tries))
    if guessed:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Sorry, you ran out of tries. The word was:", word)

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

# Function to start the game
def main():
    while True:
        word = getword()
        play(word)
        if input("Play Again? (Y/N): ").upper() != "Y":
            break

if __name__ == "__main__":
    main()
