#In this game, you need to guess a random number from 1 to 100. is gonna have tips if is greater or smaller
import random
def guess_game():
    random_number = random.randint(1, 100)
    guess = 0
    guesses = 0

    while guess != random_number:
        guess = int(input("Choose a number: "))
        if guess == random_number:
            print(f"You win! Number of guesses: {guesses + 1}")
            break
        elif guess > random_number:
            print(f"No, the number is smaller than {guess}")
        elif guess < random_number:
            print(f"No, the number is greater than {guess}")
        guesses += 1

guess_game()

