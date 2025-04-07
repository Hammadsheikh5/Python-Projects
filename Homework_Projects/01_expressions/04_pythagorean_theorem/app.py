import math  # Import the math library so we can use the sqrt function

# Define the main function where the core logic of the program resides
def main():
    
    # Display a welcome message to the user
    print("Welcome to the Pythagorean Theorem Calculator!")
    
    # Get the lengths of sides AB and AC from the user
    side_AB: float = float(input("Enter the length of AB: "))
    side_AC: float = float(input("Enter the length of AC: "))
    
    # Calculate the length of the hypotenuse BC using the Pythagorean theorem
    side_BC: float = math.sqrt(side_AB ** 2 + side_AC ** 2)
    
    # Display the calculated length of the hypotenuse
    print(f"The length of the hypotenuse BC is: {side_BC:.2f} units.")

# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
