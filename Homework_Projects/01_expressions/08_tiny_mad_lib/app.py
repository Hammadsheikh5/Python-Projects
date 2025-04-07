# Sentence start template to be used in the program
SENTENCE_START: str = "Learning to code is an amazing journey. With Python, I was able to create my "

# Define the main function where the core logic of the program resides
def main():
    
    # Display a welcome message to the user
    print("Welcome to the Mad Libs game!")
    
    # Ask the user to input an adjective and store it in the 'adjective' variable
    adjective :str = input("Please type an adjective and press enter. ")
    
    # Ask the user to input a noun and store it in the 'noun' variable
    noun :str = input("Please type a noun and press enter. ")
    
    # Ask the user to input a verb and store it in the 'verb' variable
    verb :str = input("Please type a verb and press enter. ")
    
    # Print out the full sentence formed by combining the sentence start with user input
    print(f"{SENTENCE_START} {adjective} {noun} {verb} .")

# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
