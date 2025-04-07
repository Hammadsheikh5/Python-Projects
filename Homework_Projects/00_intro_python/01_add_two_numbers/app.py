# Define the main function where the core logic of the program resides
def main():
    
    # Display a welcome message to the user
    print("Welcome to the Add Two Number Program!")
    
    # Prompt the user to enter the first number
    first_number = int(input("Enter the first number: "))

    # Prompt the user to enter the second number
    second_number = int(input("Enter the second number: "))

    # Calculate the sum of the two numbers
    total_sum = first_number + second_number

    # Print the total sum with an appropriate message
    print("The sum of", first_number, "and", second_number, "is:", total_sum)


# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()

