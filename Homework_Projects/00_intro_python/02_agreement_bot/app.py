# Define the main function where the core logic of the program resides
def main():
    
    # Display a welcome message to the user
    print("Welcome to the Favorite Animal Program!")
    
    # Ask the user about their favorite animal
    user_input = input("What's your favorite animal? ")
    
    # Respond with the user's favorite animal using string interpolation
    print(f"My favorite animal is also {user_input.lower()}!")


# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()