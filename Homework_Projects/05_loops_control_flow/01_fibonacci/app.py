# Define the main function where the core logic of the program resides
def main():
    
    # Display a welcome message to the user
    print("Welcome to Febonacci Series  !")
    
    """
    This function prints Fibonacci sequence numbers up to a maximum value.
    """
    max_value = 10000  # Define the maximum limit for Fibonacci numbers

    # Initialize the first two Fibonacci numbers
    fib_0, fib_1 = 0, 1
    print(fib_0, fib_1, end=" ")  # Print the first two numbers

    while True:
        next_num = fib_0 + fib_1  # Calculate the next Fibonacci number
        if next_num >= max_value:  # Stop if the next number exceeds max_value
            break
        print(next_num, end=" ")  # Print the next number
        fib_0, fib_1 = fib_1, next_num  # Update values for the next iteration


# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
    
    
    