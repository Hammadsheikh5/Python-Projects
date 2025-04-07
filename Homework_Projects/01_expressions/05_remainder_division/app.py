# Define the main function where the core logic of the program resides
def main():
    
    # Display a welcome message to the user
    print("Welcome to the Division and Remainder Calculator!")
    
    # Get the dividend and divisor as floating-point numbers
    dividend: float = float(input("Please enter a number to be divided: "))
    divisor: float = float(input("Please enter a number to divide by: "))
    
    # Calculate the quotient and remainder
    quotient: float = dividend // divisor  # Integer division
    remainder: float = dividend % divisor  # Modulus to get remainder
    
    # Display the result
    print(f"The result of this division is {quotient} with a remainder of {remainder}.")

# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
