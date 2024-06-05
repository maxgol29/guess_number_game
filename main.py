import random as r

print("Welcome to the Number Guessing Game!", "I'm thinking of a number between 1 and 100", sep='\n')

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts = 0

if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print("I gave you 7 attempts to guess my number")
    attempts = 7

computer_number = r.randrange(1, 101)



player_win = False

while attempts != 0 and player_win == False:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_number = int(input("Make a guess: "))

    if user_number > computer_number:
        print("Too high")
        attempts -= 1
    elif user_number < computer_number:
        print("Too low")
        attempts -= 1
    else:
        print(f"You guessed the number! It's {user_number}")
        player_win = True
        break
    if attempts == 0:
        print(f"You lost! The nuber was {computer_number}")
        break
    print("Guess again")





