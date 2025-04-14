# Define the main function where the core logic of the program resides
def main():
    
    
    affirmation = "I am capable of doing anything I put my mind to." 
    while True:
        # Ask the user to type the affirmation
        user_input = input(f"\nPlease type the following affirmation: {affirmation} ")

        if user_input == affirmation:  # Check if the input matches the affirmation
            print("\nThat's right! :)\n")  # Success message
            break  # Exit the loop
        else:
            print("\nHmmm, that was not the affirmation. Please try again.\n")  # Prompt user to try again



# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
    
    
    