# Define the main function where the core logic of the program resides
def main():
    
    # Display a welcome message to the user
    print("\nWelcome to the Fruit Shop! 🍇 🥝 🍒 🏪 🛒")
    
    # Dictionary containing favorite fruits and their respective prices
    fav_fruits = {
        "grapes": 3.5,         # Price per unit of grapes
        "oranges": 15.0,       # Price per unit of oranges
        "pineapple": 10.0,     # Price per unit of pineapple
        "custard_apple": 2.5,  # Price per unit of custard apple
        "lychee": 5.0,         # Price per unit of lychee
        "mango": 4.0           # Price per unit of mango
    }

    # Initialize a variable to store the total cost
    total_price = 0
    
    # Start a loop to repeatedly ask the user for their fruit preferences
    while True:
        
        # Loop through each fruit in the dictionary
        for fruit in fav_fruits:
            
            # Start an inner loop to handle user input for the number of fruits
            while True:
                try:
                    
                    # Ask the user how many of this fruit they want
                    bought = int(input(f"\nHow many ({fruit}) do you want?: "))
                    break  # Break out of the loop if the input is valid
                except ValueError:
                    # Handle case where user input is not a valid integer
                    print("\nInvalid input! Please enter a valid number\n")
                
            # Get the price of the current fruit from the dictionary
            price = fav_fruits[fruit]
            
            # Add the cost of this fruit to the total price
            total_price += price * bought

        # After looping through all fruits, display the total price
        print(f"\nYour total is ${total_price} 💸💲")

        # Thank the user for shopping
        print(f"Thank you for shopping 💗🤝\n")
        
        # Exit the loop after processing all fruits
        break

# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
