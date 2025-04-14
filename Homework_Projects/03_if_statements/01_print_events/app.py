# Define the main function where the core logic of the program resides
def main():
    # Display a welcome message to the user
    print("Welcome to the Even Number Printer!")

    # Loop through numbers from 1 to 39 (inclusive)
    for i in range(1, 40):
        # Check if the current number is even
        if i % 2 == 0:
            # Print the even number, keeping it on the same line with a space
            print(i, end=" ")

# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
