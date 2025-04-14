# Define the minimum voting ages for each fictional country
PETURKSBOUIPO_AGE: int = 16  # Peturksbouipo's voting age
STANLAU_AGE: int = 25        # Stanlau's voting age
MAYENGUA_AGE: int = 48       # Mayengua's voting age

# Define the main function where the core logic of the program resides
def main():
    """
    This function prompts the user for their age and checks if they are eligible
    to vote in the three fictional countries: Peturksbouipo, Stanlau, and Mayengua.
    """
    
    try:
        # Prompt the user to enter their age, and convert the input to an integer
        user_age = int(input("\nHow old are you? "))
        
        # Check if the user's age is greater than or equal to Peturksbouipo's voting age
        if user_age >= PETURKSBOUIPO_AGE:
            # Inform the user they can vote in Peturksbouipo
            print(f"\nYou can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
        else:
            # Inform the user they cannot vote in Peturksbouipo
            print(f"\nYou cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
        
        # Check if the user's age is greater than or equal to Stanlau's voting age
        if user_age >= STANLAU_AGE:
            # Inform the user they can vote in Stanlau
            print(f"\nYou can vote in Stanlau where the voting age is {STANLAU_AGE}.")
        else:
            # Inform the user they cannot vote in Stanlau
            print(f"\nYou cannot vote in Stanlau where the voting age is {STANLAU_AGE}.")
        
        # Check if the user's age is greater than or equal to Mayengua's voting age
        if user_age >= MAYENGUA_AGE:
            # Inform the user they can vote in Mayengua
            print(f"\nYou can vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
        else:
            # Inform the user they cannot vote in Mayengua
            print(f"\nYou cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.\n")
    
    except ValueError:
        # Handle the case where the user enters a non-integer input
        print("Invalid input! Please enter a valid age as a number.")

# This condition checks if this file is being run directly (not imported as a module)
# If so, it calls the main() function to start the program
if __name__ == '__main__':
    main()
