# Function to calculate the sum of numbers in a list
def sum_numbers(numbers: list[int]):
    # Initialize total to 0
    total : int = 0
    # Loop through each number in the list and add it to total
    for number in numbers:
        total += number
    # Return the total sum
    return total


# Define the main function where the core logic of the program resides
def main():
    
    # Display a welcome message to the user
    print("Welcome to the Sum Calculator!")
    
    # Define a list of numbers
    numbers: list[int] = [2, 5, 9, 6, 4, 3, 4]
    
    # Call the sum_numbers function to calculate the sum of the list
    result = sum_numbers(numbers)
    
    # Print the result of the sum
    print(f"The sum of the numbers is: {result}")


# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
