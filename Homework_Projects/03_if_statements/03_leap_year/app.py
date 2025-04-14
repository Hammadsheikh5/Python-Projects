# Define the main function where the core logic of the program resides
def main():
    
    # Display a welcome message to the user
    print("Welcome to Leap Year Finder!")
    try:
        # Take user input for the year
        year = int(input("\nPlease enter a year: "))
        
        # Check if the year is a leap year
        # A year is a leap year if:
        # 1. It is divisible by 4 and NOT divisible by 100, OR
        # 2. It is divisible by 400
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print("\nThat's a leap year!\n")  # Print message if the year is a leap year
        else:
            print("\nThat's not a leap year.\n")  # Print message if the year is not a leap year
    
    except ValueError:
        print("\nInvalid input! Please enter a valid numeric year.\n")  # Handle invalid input


# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
    
    