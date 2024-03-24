def process_user_input(user_input):
    commands = {
        "help": "Sure, I can help you. What do you need assistance with?",
        "issue": "Please describe the issue you're facing in detail.",
        "contact support": "You can reach our support team at support@example.com."
        # Add more commands and responses as needed
    }

    # Convert user input to lowercase for case-insensitive matching
    user_input_lower = user_input.lower()

    # Check if any command is present in the user input
    for command, response in commands.items():
        if command in user_input_lower:
            return response

    return "No predefined command found."

def main():
    user_input = input("Enter your text: ")
    response = process_user_input(user_input)
    print(response)

if __name__ == "__main__":
    main()

def categorize_issue(user_input):
    # Define the categories and their associated keywords
    categories = {
        "login": ["login", "sign in", "password"],
        "performance": ["slow", "performance", "speed"],
        "error": ["error", "bug", "issue"]
    }

    # Convert the user input to lowercase
    user_input = user_input.lower()

    # Iterate over the categories
    for category, keywords in categories.items():
        # If any of the category's keywords are in the user input, return the category
        if any(keyword in user_input for keyword in keywords):
            return category

    # If no category was found, return 'other'
    return "other"

# Test the function
user_input = "I'm having issues with the login process."
print(f"Category of issue: {categorize_issue(user_input)}")
