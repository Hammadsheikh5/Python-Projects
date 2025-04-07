# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES = 6  # Each die has 6 sides (standard dice)


# Define the main function where the core logic of the program resides
def main():
    
    """
    Simulates rolling two dice and prints their total
    """
    # Display a welcome message to the user
    print("Welcome to the Dice Rolling Simulator!")
    
    # Generate a random number between 1 and NUM_SIDES for the first die
    die1: int = random.randint(1, NUM_SIDES)
    
    # Generate a random number between 1 and NUM_SIDES for the second die
    die2: int = random.randint(1, NUM_SIDES)
    
    # Calculate the total of both dice
    total: int = die1 + die2

    # Display the number of sides on each die
    print(f"Each die has {NUM_SIDES} sides.")
    
    # Print the result of the first die
    print(f"First die: {die1}")
    
    # Print the result of the second die
    print(f"Second die: {die2}")
    
    # Print the total of the two dice rolls
    print(f"Total of the two dice: {total}")


# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
