from words import words  # Import a list of words from the 'words' module
import random  # Import the random module to pick a word randomly

def play_game():
    # Step 1: Randomly choose a word from the list
    word = random.choice(words).lower()  # Convert to lowercase to keep input consistent

    # Step 2: Prepare sets for tracking progress
    word_letters = set(word)  # Unique letters in the chosen word
    guessed_letters = set()  # Letters guessed by the user
    attempts = 10  # Total attempts allowed

    # Welcome message
    print("🎭 Welcome to Hangman! Can you guess the word? 🔤")

    # Step 3: Game loop runs while the user still has attempts and letters to guess
    while attempts > 0 and word_letters:

        display_word = []  # This will hold the current state of the guessed word

        # Step 4: Build the word display with guessed letters and dashes
        for letter in word:
            if letter in guessed_letters:
                display_word.append(letter)  # Show letter if guessed
            else:
                display_word.append("-")  # Hide letter if not yet guessed

        # Step 5: Display current progress
        print(" ".join(display_word))

        # ✅ Show guessed letters so far
        print("\n🧠 Guessed letters so far:", " ".join(sorted(guessed_letters)))

        # Step 6: Ask user to guess a letter
        guess = input("🔤 Guess a letter: ").lower()

        # Step 7: Validate user input
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter! Try again.")
        elif guess in word_letters:
            guessed_letters.add(guess)      # Add to guessed
            word_letters.remove(guess)      # Remove from word letters (correct guess)
            print("✅ Correct!")
        else:
            guessed_letters.add(guess)      # Add even wrong guesses to avoid repeat
            attempts -= 1                   # Decrease attempts
            print(f"❌ Wrong! You have {attempts} attempts left.")

            # Step 8: Show simple hangman-style stages
            hangman_stages = [
                "🙂",             # 10 attempts left – Full health
                "😐",             # 9 attempts left
                "😯",             # 8 attempts left
                "😧",             # 7 attempts left
                "😨 |",           # 6 attempts left
                "😰 /|",          # 5 attempts left
                "🥶 /|\\",        # 4 attempts left
                "🫣 /|\\",        # 3 attempts left
                "😱 /|\\ /",      # 2 attempts left
                "😱 /|\\ / \\",   # 1 attempt left
                "💀 GAME OVER"    # 0 attempts left – You lost
            ]

            # Display hangman based on how many attempts are left (if under 10)
            if attempts < 10:
                print("\t", hangman_stages[9 - attempts])  # Adjust index based on remaining attempts

    # Step 9: Check win/lose condition
    if not word_letters:
        print(f"🎉 Congratulations! You guessed the word: {word.upper()} 🏆\n")
    else:
        print(f"💀 Game Over! The correct word was: {word.upper()}\n")

# Run the game only if the script is executed directly
# This condition ensures that the main game function runs only when not imported
if __name__ == "__main__":
    play_game()
