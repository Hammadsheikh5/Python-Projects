import hashlib  # Importing hashlib for password hashing

def hash_password(password):
    """
    This function takes a password as input,
    converts it into bytes, hashes it using SHA-256,
    and returns the hashed password in hexadecimal format.
    """
    # hashlib.sha256() is a hash function that produces a fixed-size hash from a given input.
    # password.encode() converts the password string to bytes since hash functions require bytes.
    # .hexdigest() returns the hash as a string of hexadecimal characters.
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    This function checks if the given email exists in stored_logins
    and verifies if the provided password (hashed) matches the stored hash.
    
    Returns True if the email and password match, otherwise False.
    """
    # Hash the user-entered password using the hash_password function
    hashed_input_password = hash_password(password_to_check)
    
    # Print the hashed password for debugging purposes (this will show what is being compared)
    print(hashed_input_password)

    # Check if the email exists in the stored_logins dictionary and if the password hash matches
    if email in stored_logins and stored_logins[email] == hashed_input_password:
        # Return True if both email exists and the password hash matches
        return True
    
    # Return False if login fails (either the email is not found or the password doesn't match)
    return False

def main():
    """
    This function stores user login data (hashed passwords),
    takes user input for email and password,
    and checks login validity using the login() function.
    """
    # Dictionary storing user emails as keys and their hashed passwords as values
    # This simulates a stored login system where actual passwords are not saved, only their hashes.
    stored_logins = {
        "test@example.com": hash_password("mypassword123"),  # The hash of "mypassword123"
        "user@example.com": hash_password("securepass"),     # The hash of "securepass"
        "hammadsheikh@gmail.com": hash_password("12345hammad")  # The hash of "12345hammad"
    }
    
    # Prompt the user to enter their email address
    email = input("\nEnter your email: ")
    
    # Prompt the user to enter their password
    password = input("Enter your password: ")

    # Use the login function to check if the entered email and password are valid
    if login(email, password, stored_logins):
        # If login() returns True (valid email and password), print success message
        print("\nLogin successfully! ✅ 🎉\n")
    else:
        # If login() returns False (invalid email or password), print failure message
        print("\nInvalid email or password! ❌\n")

# This ensures the main() function is called when the script is executed directly,
# but not when the script is imported as a module into another script.
if __name__ == '__main__':
    main()
