# Set the minimum height requirement to ride (in inches)
MINIMUM_HEIGHT = 50  # Minimum height required

# Define the main function where the core logic of the program resides
def main():
    
    # Display a welcome message to the user
    print("🎢 Welcome to the Thrill Ride Height Checker! 🎢")
    print("Let's see if you're tall enough to ride.\n")
    
    # Start an infinite loop to repeatedly ask for user input
    while True:
        # Prompt user to enter their height or press Enter to quit
        user_input = input("How tall are you (in inches)? (Press Enter to stop) ").strip()
        
        # Check if the input is an empty string (i.e., user pressed Enter)
        if user_input == "":
            # Display exit message and break the loop
            print("\nExiting Program...\nGoodbye!\n")
            break

        try:
            # Try converting the user input to an integer
            user_height = int(user_input)
            
            # Check if the user's height meets or exceeds the minimum height requirement
            if user_height >= MINIMUM_HEIGHT:
                print("\n✅ You're tall enough to ride!\n")
            else:
                print("\n❌ You're not tall enough to ride, but maybe next year!\n")    

        except ValueError:
            # Handle the case where the input is not a valid integer
            print("\n⚠️ Invalid Input! Please enter a number.\n")        

# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
