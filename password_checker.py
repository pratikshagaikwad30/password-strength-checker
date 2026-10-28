
import math
import string
import getpass


COMMON_PASSWORDS = {
    "password",
    "password123",
    "12345678",
    "qwerty123",
    "admin123",
    "welcome123",
    "iloveyou"
}


def check_password(password):
    length_ok = len(password) >= 12
    upper_ok = any(c.isupper() for c in password)
    lower_ok = any(c.islower() for c in password)
    digit_ok = any(c.isdigit() for c in password)
    special_ok = any(c in string.punctuation for c in password)

    # Estimate the character pool size
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)

    entropy = (
        len(password) * math.log2(pool)
        if pool > 0 else 0
    )
    dictionary_risk = password.lower() in COMMON_PASSWORDS

    score = sum([
        length_ok, upper_ok, lower_ok,
        digit_ok, special_ok
    ])

    if score <= 2:
        strength = "Weak"
    elif score <= 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Exceptional"

    print("\n--- Password Analysis ---")
    print("Length:", len(password))
    print("Length >= 12:", length_ok)
    print("Uppercase:", upper_ok)
    print("Lowercase:", lower_ok)
    print("Digits:", digit_ok)
    print("Special characters:", special_ok)
    print(f"Estimated entropy: {entropy:.2f} bits")
    if dictionary_risk:
        strength = "Weak"
    print("Strength:", strength)
    
    print("Common password detected:", dictionary_risk)

    if dictionary_risk:
        print("WARNING: This is a common password. Choose a unique one.")


    if not length_ok:
        print("Feedback: Use at least 12 characters.")
    if not upper_ok:
        print("Feedback: Add an uppercase letter.")
    if not lower_ok:
        print("Feedback: Add a lowercase letter.")
    if not digit_ok:
        print("Feedback: Add a digit.")
    if not special_ok:
        print("Feedback: Add a special character.")

    if score == 5 and entropy >= 70:
        print("Your password meets the basic policy and entropy target.")
    else:
        print("Review the feedback above to improve your password.")

password = getpass.getpass("Enter a test password: ")
check_password(password)
