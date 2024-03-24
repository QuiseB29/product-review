
def check_name_length(name):
    return len(name) >= 2
#function that checks the length of name

def main():
    first_name = input('Enter your first name:')
    last_name = input("Enter your last name:")
    #input names
    if not check_name_length(first_name) or not check_name_length(last_name):
        print("Error: Both first and last name should be at least 2 characters long. ")
        
    else:
        print("Both first and last names meet the length requirement.")
        
if __name__ == "__main__":
    main()
    
def check_password_complexity(password):
    # Check if password length is at least 8 characters
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    # Check if password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."

    # Check if password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter."

    # Check if password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit."

    # If all criteria are met, return True
    return True, "Password meets complexity requirements."

# Test the function
password = input("Enter your password: ")
is_complex, message = check_password_complexity(password)
print(message)

    
