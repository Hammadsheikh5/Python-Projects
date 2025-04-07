# Constants for time conversions
DAYS_PER_YEAR: int = 365.25
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

# Define the main function where the core logic of the program resides
def main():
    
    # Display a welcome message to the user
    print("Welcome to the Time Converter!")
    
    # Calculate the number of seconds in a single year
    seconds_in_a_year: int = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    
    # Print the number of seconds in a year
    print("There are " + str(seconds_in_a_year) + " seconds in a year!")
    
    # Get user input for the number of years
    user_input: int = int(input("Enter the number of years: "))
    
    # Calculate the total number of seconds in the input years
    total_seconds: int = user_input * seconds_in_a_year
    
    # Display the total number of seconds
    print(f"The total number of seconds in {user_input} years is : {total_seconds} seconds.")

# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
