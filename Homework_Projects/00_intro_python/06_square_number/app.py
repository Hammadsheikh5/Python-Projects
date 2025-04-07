# Define the main function where the core logic of the program resides
def main():
    
    # Optional: You can display a welcome message
    print("Welcome to the Square Calculator!")

    # Prompt the user for a number
    user_input = float(input("Type a number to see its square: "))

    # Calculate the square
    result = user_input * user_input

    # Print the result
    print(f"{user_input} squared is {result}")

    #OPtional Prints
    # print(f"{user_input} squared is {user_input ** 2}")
    # Calculate the square of the user number and display message with squared value



# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
