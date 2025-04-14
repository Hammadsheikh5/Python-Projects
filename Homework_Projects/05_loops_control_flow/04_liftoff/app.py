# Define the main function where the core logic of the program resides
def main():
    
    # Display a welcome message to the user
    print("Welcome to Space Station Liftop Timer!")
    for i in range(10, 0, -1):  # Loop from 10 down to 1
        print(i, end=" ")  # Print numbers in a single line with space
    print("Liftoff!\n")  # Print Liftoff after loop has completed 


# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
    
    
    