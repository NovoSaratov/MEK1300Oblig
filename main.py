import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if user_guess < number:
            print(f"Too low! Try again. Attempts left: {max_attempts - attempts}")
        elif user_guess > number:
            print(f"Too high! Try again. Attempts left: {max_attempts - attempts}")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
            break

        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number}.")
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again == "yes":
                guess_number()
            elif play_again == "no":
                break


guess_number()