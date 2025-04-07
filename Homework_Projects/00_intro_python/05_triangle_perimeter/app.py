# Define the main function where the core logic of the program resides
def main():
    
    # Display a welcome message to the user
    print("Welcome to the Triangle Perimeter Calculator!")

    # Prompt the user to enter the lengths of each side of the triangle
    side_one = float(input("What is the length of side 1? "))
    side_two = float(input("What is the length of side 2? "))
    side_three = float(input("What is the length of side 3? "))

    # Calculate the perimeter
    perimeter = side_one + side_two + side_three

    # Print the perimeter of the triangle
    print(f"The perimeter of the triangle is {perimeter}")


# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
