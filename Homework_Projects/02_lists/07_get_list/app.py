
# Function to collect integer inputs from the user and return them as a list
def get_number_list():
    number_list: list[int] = []
    print("Enter numbers one by one. Press Enter without typing to stop.")
    
    while True:
        user_input = input("Enter a number: ")
        
        # Stop if the input is empty
        if user_input == "":
            break
        
        try:
            number = int(user_input)
            number_list.append(number)
        except ValueError:
            print("Invalid input. Please enter an integer.")

    return number_list

# Define the main function where the core logic of the program resides
def main():
    print("Welcome to the get list app!")
    
    # Get a list of numbers from the user
    number_list = get_number_list()

    print("Your list is:", number_list)
    

# Ensure the main function runs only when this script is executed directly
if __name__ == '__main__':
    main()
