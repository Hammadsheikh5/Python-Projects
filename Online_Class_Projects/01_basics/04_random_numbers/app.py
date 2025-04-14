import random  # Import the random module to generate random numbers

# Constants to define how many numbers to generate and the range
N_NUMBERS: int = 10     # Total numbers to generate
MIN_VALUE: int = 1      # Minimum possible value (inclusive)
MAX_VALUE: int = 100    # Maximum possible value (inclusive)

# Define the main function where the program logic goes
def main():
    """
    This function generates and prints 10 random numbers in the range 1 to 100.
    Each number is separated by a space.
    """
    for _ in range(N_NUMBERS):  # Loop exactly 10 times
        value = random.randint(MIN_VALUE, MAX_VALUE)  # Generate a random number
        print(value, end=" ")  # Print the number on the same line, followed by a space

# Ensure main() runs only if the script is executed directly
if __name__ == '__main__':
    main()
