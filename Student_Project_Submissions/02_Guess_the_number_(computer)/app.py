import random  # Importing random module to generate random numbers

# Define the main function where the core logic of the program resides
def guess_the_number():
    # This function runs the number guessing game where the user tries to guess a randomly generated number between 1 and 100. 
    # Hints are given if the guess is too high or too low.

    print("\nWelcome to a number guessing game 🔢🤔")
    print("\nI am thinking of a number between 1 and 100...\n")

    # Generate a random number between 1 and 100
    secret_num = random.randint(1, 100)

    attempts = 0  # Track the number of user attempts

    # Loop until the correct guess is made
    while True:
        try:
            # Ask user for a guess and try to convert it to an integer
            user_guess = int(input("Enter a guess: "))
        except ValueError:
            # If input is not a valid integer, show message and continue loop
            print("❌ Please enter a valid number!\n")
            continue

        attempts += 1  # Increment attempt count

        # Check if the guess is correct
        if user_guess == secret_num:
            print(f"\nCongrats 🎉👏! You guessed the number in {attempts} attempts. The number was {secret_num}.\n")
            break  # Exit the loop if guessed correctly
        elif user_guess > secret_num:
            print("Your guess is too high ⚡☝\n")  # Hint if guess is too high
        else:
            print("Your guess is too low 🔅👇\n")  # Hint if guess is too low

# Run the game only if the script is executed directly
# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    guess_the_number()

    
    