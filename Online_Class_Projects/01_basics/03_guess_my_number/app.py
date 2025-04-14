import random  # Importing random module to generate random numbers


# Define the main function where the core logic of the program resides
def main():
    
  #This function runs the number guessing game where the user tries to guess a randomly generated number between 0 and 99. Hints are given if the guess is too high or too low.
    
    print("\nWelcome to a number guessing game 🔢🤔")
    print("\nI am thinking of a number between 0 and 99...\n")
    
    # Generate a random number between 0 and 99
    secret_num = random.randint(0, 99)
    
    # Prompt the user to enter an initial guess
    user_guess = int(input("Enter a guess: "))
    # print(secret_num)
    
    # Loop until the user guesses the correct number
    while secret_num != user_guess:
        if user_guess > secret_num:
            print("Your guess is too high ⚡☝")  # Hint if guess is too high
        else:
            print("Your guess is too low 🔅👇")   # Hint if guess is too low
        
        print(" ")  # Print a blank line for readability
        
        # Ask the user for a new guess
        user_guess = int(input("Enter a new guess: "))
    
    # User guessed correctly, print a success message
    print(f"\nCongrats 🎉👏! The number was: {secret_num}\n")  

# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
    
    
    