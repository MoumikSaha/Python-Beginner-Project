import random

#taking a random word of list
words_list = ["book","television", "computer", "paradise", "dream",]

#Taking a random word from the from the word of list
def chosen_word():
    return random.choice(words_list)


#current state of the word that has been chosen with guessed letter
def display_word(word, guessed_letter):
    display = ""
    for letter in word:
        if letter in guessed_letter:
            display = display+letter
        else:
            display += "_"
    return display
    
    
def hungman():
    word_to_guess = chosen_word()
    guessed_letter = []
    attempt = 6
    
    print("Welcome to Hungman Game")

    while True:
        print("\nWord You have to guess: ", display_word(word_to_guess, guessed_letter))
        guess = input("Guess a letter/alphabet: ").lower()
        
        #length of the guess should'nt equal to 1 or not in alphabet
        if len(guess) != 1 or not guess.isalpha():
            print("Guess only one letter")
            continue
        
        if guess in guessed_letter:
            print("You've already guessed that letter!")
            continue
        
       #now the guessed letter get add to the end of the guessed_letter list
        guessed_letter.append(guess)
        
        if guess in word_to_guess:
            print("Correct guess")
        else:
            print("Incorrect guess")
            attempt -= 1
            
        if display_word(word_to_guess, guessed_letter) == word_to_guess:
            print("You've guessed the word correctly: ", word_to_guess)
            break
        
        if attempt == 0:
            print("You are run out of guesses, The word was: ", word_to_guess )
            break
        

if __name__ == "__main__":
    hungman()
            
            