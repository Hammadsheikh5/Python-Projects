# Define the main function where the core logic of the program resides
def main():
    
    # Display a welcome message to the user
    print("Welcome to the Feet to Inches Converter!")
    
    # Prompt the user for input and convert it to an integer
    user_input: int = int(input("Enter The Number of Feet: "))
    
    # Convert feet to inches (1 foot = 12 inches)
    inches: float = user_input * 12.0
    
    # Display the result
    print(f"{user_input} feet is equal to {inches} inches.")

# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
