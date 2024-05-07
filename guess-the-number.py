import random

print("Welcome to GUESS THE NUMBER.")
print("i'm thinking of a number between 1 to 100, can you guess it?")

user_guess = 0
guesses = 0
random_number = random.randrange(101)
while user_guess != random_number:
    user_guess = int(input("enter your guess:"))
    if user_guess < random_number:
        print("Too low! Try Again.")
    elif user_guess > random_number:
        print("Too High! Try Again.")
    else:
        print(f"Congratulations! You guessed the number {random_number} correctly in {guesses} guesses.")
        break
    guesses += 1
    
        