# Define the main function where the core logic of the program resides
def main():
    # Display a welcome message to the user
    print("Welcome to the Last Element Finder!")

    # Define a list of integers
    numbers: list[int] = [2, 5, 8, 9, 6, 4, 2, 46]

    # Get the last element using length - 1 (zero-indexed)
    print("Last element using len - 1:", numbers[len(numbers) - 1])

    # Get the last element using negative indexing
    print("Last element using -1 index:", numbers[-1])

    # Remove and return the last element using pop()
    last_item_removed = numbers.pop(-1)  # This will remove the last element from the list and return it
    print("Removed last element:", last_item_removed)

    # Print the new last element after popping
    print("New last element:", numbers[-1])  # This will print the new last element of the list after the pop operation

# Ensure the main function runs only when this script is executed directly
if __name__ == '__main__':
    main()

    
