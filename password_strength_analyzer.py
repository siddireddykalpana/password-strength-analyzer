# Password Strength Analyzer
# Unique Python Project

import re
import random
import string
import hashlib

# Store old passwords (optional feature)
old_passwords = []

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should contain at least 8 characters.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number Check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special Character Check
    if re.search(r"[!@#$%^&*()_+=<>?/]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Check repeated password
    hashed = hashlib.sha256(password.encode()).hexdigest()

    if hashed in old_passwords:
        feedback.append("This password was already used before.")
    else:
        old_passwords.append(hashed)

    # Strength Level
    if score == 5:
        strength = "Very Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback


# Function to generate strong password suggestions
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Main Program
print("===== PASSWORD STRENGTH ANALYZER =====")

while True:
    user_password = input("\nEnter your password: ")

    strength, feedback = check_password_strength(user_password)

    print(f"\nPassword Strength: {strength}")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print("-", item)

    # Suggest stronger password
    if strength != "Very Strong":
        print("\nSuggested Strong Password:")
        print(generate_strong_password())

    choice = input("\nDo you want to check another password? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you for using Password Strength Analyzer!")
        break