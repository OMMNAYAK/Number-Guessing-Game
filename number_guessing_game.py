import random

def number_guessing_game():
    """A simple number guessing game where the user guesses a secret number."""

    print("=" * 40)
    print("   Welcome to the Number Guessing Game!")
    print("=" * 40)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?\n")

    # Generate a random secret number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    # Keep looping until the user guesses correctly
    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("⚠️  Please enter a valid whole number!\n")
            continue

        attempts += 1

        if guess < 1 or guess > 100:
            print("⚠️  Please guess a number between 1 and 100!\n")
            attempts -= 1  # Don't count out-of-range guesses
            continue
        elif guess < secret_number:
            print(f"📉 Too low! Try a higher number.\n")
        elif guess > secret_number:
            print(f"📈 Too high! Try a lower number.\n")
        else:
            # Correct guess!
            print("=" * 40)
            print(f"🎉 Correct! The secret number was {secret_number}!")
            print(f"🏆 You guessed it in {attempts} attempt{'s' if attempts != 1 else ''}!")
            print("=" * 40)
            break

    # Provide performance feedback based on number of attempts
    if attempts <= 5:
        print("⭐ Outstanding! You're a natural!")
    elif attempts <= 10:
        print("👍 Great job! Well played!")
    elif attempts <= 15:
        print("😊 Not bad! Keep practicing!")
    else:
        print("💪 Better luck next time! Keep trying!")

    # Ask if the user wants to play again
    play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if play_again in ("yes", "y"):
        print()
        number_guessing_game()
    else:
        print("\nThanks for playing! Goodbye! 👋")


# Entry point
if __name__ == "__main__":
    number_guessing_game()
