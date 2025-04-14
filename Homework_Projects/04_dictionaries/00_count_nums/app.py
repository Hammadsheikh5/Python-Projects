# Define the main function where the core logic of the program resides
def main():
    
    # Create an empty list to store the valid number entries
    numbers = []

    # Start an infinite loop to keep asking the user for input
    while True:
        # Ask the user to enter a number (as a string)
        user_input = input("Enter a number (or press Enter to stop): ")

        # If the input is empty (user pressed Enter), exit the loop
        if user_input == "":
            break

        try:
            # Try converting the input to an integer
            number = int(user_input)

            # If successful, add the number to the list
            numbers.append(number)

        except ValueError:
            # Handle the case where the input is not a valid integer
            print("⚠️ Invalid input! Please enter a valid number.")

    # Initialize an empty dictionary to store the frequency of each number
    number_count = {}

    # Count how many times each number appears in the list
    for number in numbers:
        if number in number_count:
            number_count[number] += 1  # If already in dictionary, increment its count
        else:
            number_count[number] = 1   # If not in dictionary, initialize with 1
    
    print(number_count)

    # Print the count of each number
    print("\n📊 Number counts:\n")
    for number, count in number_count.items():
        print(f"● {number} appears {count} time(s).\n")

# Ensure that the main() function only runs if the script is executed directly
if __name__ == '__main__':
    main()
