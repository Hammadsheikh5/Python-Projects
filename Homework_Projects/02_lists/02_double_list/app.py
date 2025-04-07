# Function to double the values of a list of integers
def double_list(input_list: list[int]):
    # Loop through each element of the input list
    for i in range(len(input_list)):
        # Double each element and update the list
        input_list[i] = input_list[i] * 2
    # Return the updated list
    return input_list


# Define the main function where the core logic of the program resides
def main():
    
    # Display a welcome message to the user
    print("Welcome to the List Doubler!")
    
    # Define an initial list of integers
    int_list: list[int] = [2, 3, 4, 5, 6, 7]
    
    # Print the original list
    print("The original list is: ", int_list) 
    
    # Call the double_list function to double the values of the list
    result = double_list(int_list)
    
    # Print the updated list after doubling the values
    print("Doubled list: ", result)
    
    # Print the modified original list (input_list is directly modified)
    print("The original list is: ", int_list)


# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
