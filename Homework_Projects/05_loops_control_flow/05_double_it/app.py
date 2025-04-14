# Define the main function where the core logic of the program resides
def main():
    
    # Display a welcome message to the user
    print("Welcome to the Doubling Program! 🔢 🚀")  # This is the welcome message shown to the user.
    
    # Ask the user for an initial number
    user_input = input("\nEnter a number to start doubling: ")  # Prompt the user to input a number.

    # Check if the input is a valid number (i.e., all characters are digits)
    if not user_input.isdigit():
        # If the input is not a valid number, print an error message
        print("\nInvalid number. Please enter a valid number.\n")
    else:
        # If the input is a valid number, convert it to an integer
        user_num = int(user_input)
        
        # Check if the number is greater than or equal to 100
        if user_num >= 100:
            # If the number is greater than or equal to 100, ask the user to enter a smaller number
            print("\nPlease enter a number smaller than 100.\n")
        else:
            # Keep doubling the number until it reaches 100 or more
            while user_num < 100:
                user_num = user_num * 2  # Double the number
                print(user_num, end=" ")  # Print the current value of the number (without new line)

# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()  # Call the main function to execute the program
