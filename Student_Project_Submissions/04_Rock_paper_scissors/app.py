import random  # Importing the random module to allow computer to choose randomly

# Function to get the computer's random choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]  # Possible choices
    return random.choice(choices)  # Randomly return one choice



# Function to determine the winner of a round
def determine_winner(user_choice, computer_choice):
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")  # Show both choices

    # Condition when both choices are the same
    if user_choice == computer_choice:
        return "tie"
    # User wins scenarios
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "user"
    else:
        return "computer"  # All other cases: computer wins

# Function to play the game repeatedly and track points
def play_game():
    """Plays multiple rounds of Rock, Paper, Scissors and tracks scores."""

    user_points = 0  # Initialize user's score
    computer_points = 0  # Initialize computer's score

    print("\n🎮 Welcome to Rock, Paper, Scissors Game!")
    print("Type 'exit' anytime to quit the game.\n")

    # Game loop: runs until user types 'exit'
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors) or type 'exit' to quit: ").lower()

        # Allow user to exit the game
        if user_input == "exit":
            break

        # Validate user input
        if user_input not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice. Please enter rock, paper, or scissors.\n")
            continue  # Skip to next loop iteration if invalid

        # Get computer's random choice
        computer_choice = get_computer_choice()

        # Determine who won the round
        result = determine_winner(user_input, computer_choice)

        # Update and display points based on result
        if result == "user":
            print("✅ You win this round!\n")
            user_points += 1
        elif result == "computer":
            print("💻 Computer wins this round!\n")
            computer_points += 1
        else:
            print("😐 It's a tie!\n")

        # Show current score
        print(f"🏆 Score → You: {user_points} | Computer: {computer_points}\n")

    # Final score display after exit
    print("\n🎯 Final Results:")
    print(f"Your Points: {user_points}")
    print(f"Computer Points: {computer_points}")

    # Declaring final result
    if user_points > computer_points:
        print("🎉 Congratulations! You won the game!\n")
    elif user_points < computer_points:
        print("😔 Oh no! Computer won the game.\n")
    else:
        print("🤝 It's a draw overall!\n")

    print("Thanks for playing! 👋\n")

# Run the game only if the script is executed directly
# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == "__main__":
    play_game()
