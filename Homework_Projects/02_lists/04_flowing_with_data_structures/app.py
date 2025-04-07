# Function to append a given message to a list three times
def append_message_three_times(message_list: list[str], message: str):
    for _ in range(3):  # Loop 3 times
        message_list.append(message)  # Append the message to the list

# Define the main function where the program logic resides
def main():
    # Display a welcome message to the user
    print("Welcome to the message duplicator!")

    # Initialize an empty list to hold messages
    messages: list[str] = []

    # Display the initial empty list
    print("List before:", messages)

    # Prompt the user to input a message
    user_message: str = input("Please enter a message to copy: ")

    # Call the function to append the message three times to the list
    append_message_three_times(messages, user_message)

    # Display the updated list after appending
    print("List after:", messages)

# This ensures the main() function only runs when the script is executed directly
if __name__ == '__main__':
    main()
