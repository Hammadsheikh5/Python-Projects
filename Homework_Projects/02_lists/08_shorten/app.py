MAX_LENGTH : int = 3

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

def shorten(lst:list[int]):
    if len(lst)>MAX_LENGTH:
        print("List is too long, removing items...")
        for i in range(len(lst)- MAX_LENGTH):
            item = lst.pop()
            print("Removed item : " , item)
            print("List after removing item : " , lst)
    else:
        print("List is short enough, no need to remove items.")
        return
    

# Define the main function where the core logic of the program resides
def main():
    
    # Display a welcome message to the user
    print("Welcome to !")
    lst : list[int] = get_number_list()
    print("Original list" ,lst)
    shorten(lst)
    # print("Original list" ,lst)



# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
    
    