# Define the main function where the core logic of the program resides
def guess_the_number():
    # Set the initial range
    low = 1
    high = 100

    print("\n🎮 Welcome to the number guessing game!")
    print(f"Think of a number between {low} and {high}, and I will try to guess it.")
    input("Press Enter to continue...")

    attempts = 0  # Initialize the number of attempts

    while True:
        # Computer makes a guess using binary search logic
        guess = (low + high) // 2
        attempts += 1  # Increment attempt count

        print(f"\nIs your number {guess}?")
        # Ask user for feedback
        correct_guess = input(
            "Enter 'h' for higher, 'l' for lower, or 'c' for correct: "
        ).lower()

        # If the guess is correct
        if correct_guess == "c":
            print("\n🎉 Congratulations! I guessed your number.")
            print(f"✅ It took me {attempts} attempts to guess your number.")
            break
        # If the actual number is higher than the guess
        elif correct_guess == "h":
            low = guess + 1
        # If the actual number is lower than the guess
        elif correct_guess == "l":
            high = guess - 1
        # Handle invalid inputs
        else:
            print("❌ Invalid input. Please enter 'h', 'l', or 'c'.")

    print("\nThanks for playing! 🙌")


# Run the game only if the script is executed directly
# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == "__main__":
    guess_the_number()
