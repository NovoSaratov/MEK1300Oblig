import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("please enter a number")
            continue
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
            while True:
                play_again = input("Do you want to play again? (yes/no): ").lower()

                if play_again == "yes":
                    guess_number()
                    break
                elif play_again == "no":
                    break
                else:
                    print("Error: Please enter 'yes' or 'no'.")

            break



guess_number()