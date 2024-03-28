import re

def assess_password_strength(password):
    # Define criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r"[A-Z]", password)
    lowercase_criteria = re.search(r"[a-z]", password)
    digit_criteria = re.search(r"\d", password)
    special_char_criteria = re.search(r"[ !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]", password)

    # Evaluate password strength based on criteria
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return "Strong"
    elif length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria:
        return "Moderate"
    elif length_criteria and (uppercase_criteria or lowercase_criteria):
        return "Weak"
    else:
        return "Very Weak"

# Get user input for password
password = input("Enter your password: ")

# Assess password strength
strength = assess_password_strength(password)

# Provide feedback to user
print("Password strength:", strength)
