# Define the main function where the core logic of the program resides
def main():
    
    # Display a welcome message to the user
    print("Welcome to the Fahrenheit to Celsius Converter!")

    try:
        # Prompt the user to enter a temperature in Fahrenheit
        user_input = float(input("Enter temperature in Fahrenheit: "))
        
        # Convert Fahrenheit to Celsius using the given formula
        celsius = (user_input - 32) * 5.0 / 9.0

        # Round the Celsius value to 4 decimal places
        celsius_rounded = round(celsius, 4)

        # Print the result with both Fahrenheit and Celsius values
        print(f"Temperature: {user_input}F = {celsius_rounded}C")

    except ValueError:
        # Handle invalid (non-numeric) input
        print("Please enter a valid numeric value.")


# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
