# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES = 6  # Each die has 6 sides (standard dice)

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    # Generate a random number between 1 and NUM_SIDES for the first die
    die1: int = random.randint(1, NUM_SIDES)
    
    # Generate a random number between 1 and NUM_SIDES for the second die
    die2: int = random.randint(1, NUM_SIDES)
    
    # Calculate the total of both dice
    total: int = die1 + die2
    
    #First Die
    print("First die : " , die1)
    #Second Die
    print("Second die : " , die2)
    # Print the total of the two dice rolls
    print("Total of two dice:", total)

# Define the main function where the core logic of the program resides
def main():
    # Display a welcome message to the user (this message is incomplete)
    print("Welcome to the Dice Roller Simulator!") 
    
    # Define a variable 'die1' in the main function with a fixed value (10)
    die1: int = 10
    
    # Print the initial value of 'die1' in the main function
    print("die1 in main() starts as: " + str(die1))
    
    # Call the roll_dice() function three times to simulate rolling dice
    roll_dice()
    roll_dice()
    roll_dice()
    
    # Print the value of 'die1' again in the main function after rolling dice
    # This demonstrates that the value of 'die1' remains unchanged
    print("die1 in main() is: " + str(die1))

# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
