# Function to read names and numbers from user and store in a dictionary
def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create an empty dictionary to store name-number pairs

    while True:
        try:
            name = input("Enter a name (or press Enter to stop): ").strip()  # Get user input for name
            if name == "":  # Stop the loop if input is empty
                break
            number = input("Enter a number for " + name + ": ").strip()  # Get user input for phone number
            phonebook[name] = number  # Store the name-number pair in the dictionary
        except ValueError:
            print("❌ Invalid input! Please try again.\n")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}")


    return phonebook  # Return the populated phonebook


# Function to print all entries in the phonebook
def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    print("\n📒 Phonebook Entries:")
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")  # Display name and associated number


# Function to allow user to search for numbers by name
def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    print("\n🔍 Lookup Phone Numbers:")
    while True:
        name = input("Enter name to lookup (or press Enter to stop): ").strip()  # Ask for name to search
        if name == "":  # Exit condition
            print("Exiting lookup...\n")
            break
        try:
            # Check if name exists in the phonebook
            if name not in phonebook:
                print(f"⚠️ {name} is not in the phonebook.\n")
            else:
                print(f"📞 {name}'s number is: {phonebook[name]}\n")
        except ValueError:
            # This is a catch-all if something unexpected goes wrong during lookup
            print("❌ An error occurred while looking up the name. Please try again.\n")


# Define the main function where the core logic of the program resides
def main():
    print("\n📞 Welcome to the Simple Phonebook App! Easily store and look up contacts by name.\n")

    
    phonebook = read_phone_numbers()  # Read entries from user
    print_phonebook(phonebook)        # Print all entries
    lookup_numbers(phonebook)         # Allow name-based lookup




# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
    
    
    