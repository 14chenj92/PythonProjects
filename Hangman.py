import random

# List of words for the game
word_list = ['wares', 'soup']

# Function to choose a random word from the list
def get_word():
    return random.choice(word_list).upper()

# Function to play the Hangman game
def play(word):
    # Create a string of underscores representing the word to be guessed
    word_completion = "_" * len(word)
    # Initialize variables
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!\n")
    
    while not guessed and tries > 0:
        # Display the current state of the hangman and the word being guessed
        print(display_hangman(tries))
        print("Word:", word_completion)
        print("Guessed Letters:", ", ".join(guessed_letters))
        # Get user input for a guess
        guess = input("Please guess a letter or word: ").upper()
        
        # Handling guesses
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")

    # Display the final state of the hangman and outcome of the game
    print(display_hangman(tries))
    if guessed:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Sorry, you ran out of tries. The word was:", word)

# Function to display the Hangman stages
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
        word = get_word()
        play(word)
        if input("Play Again? (Y/N): ").upper() != "Y":
            break

if __name__ == "__main__":
    main()
