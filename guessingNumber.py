import random

limit = int(input("Enter your limit: "))
secret_number = random.randint(0, limit)
guess_time = 4
guess_count = 0

# print(secret_number)  #just incase to see the secret number in advance

while guess_count<guess_time:
    guess = int(input(f"Guess the number between 0 and {limit} : "))
    guess_count += 1
    if guess < secret_number:
        print("below the secret number")
    elif guess > secret_number:
        print("Above the secret number")
    elif guess == secret_number:
        print("Congratulations! You won")
        break
else:
    print("Try another time")