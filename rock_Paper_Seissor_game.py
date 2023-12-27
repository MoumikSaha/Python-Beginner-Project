import random

option = ['rock','paper','seissor']

# taking user input to play
while True:
    userInput = input(f'Enter your choice {option} :  ').lower()
    if userInput not in option:
        print("Invalid Enter")
        continue
    
# taking computer input to play   
    computerInput= random.choice(option)
    print(f"Computer Choose: {computerInput}")

# Comparing both inputs

    if userInput == computerInput:
        print("Its a tie!")
    elif userInput == "rock" and computerInput == "seissor":
        print("You Won!")
    elif userInput == "paper" and computerInput == "rock":
        print("You Won!")
    elif userInput == "seissor" and computerInput == "paper":
        print("You Won!")
    else:
        print("Computer won!")
    
    # Asking user to play again
    play_again= input("Do you want to play again? (y/n): ")
    if play_again != "y":
        break
print("Thanks for playing")