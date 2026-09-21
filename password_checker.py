import string


def check_password(password):
    """Check a password and return (score, rating, feedback).

    Raises:
        TypeError: if password is not a string.
        ValueError: if password is empty.
    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    if password == "":
        raise ValueError("Password cannot be empty")

    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
        feedback.append("Length OK")
    else:
        feedback.append("Too short")

    if any(char.isupper() for char in password):
        score += 1
        feedback.append("Has uppercase letter")
    else:
        feedback.append("Missing uppercase letter")

    if any(char.islower() for char in password):
        score += 1
        feedback.append("Has lowercase letter")
    else:
        feedback.append("Missing lowercase letter")

    if any(char.isdigit() for char in password):
        score += 1
        feedback.append("Has a number")
    else:
        feedback.append("Missing a number")

    if any(char in string.punctuation for char in password):
        score += 1
        feedback.append("Has a special character")
    else:
        feedback.append("Missing a special character")

    if score <= 2:
        rating = "Weak"
    elif score in (3, 4):
        rating = "Medium"
    else:
        rating = "Strong"

    return score, rating, feedback


if __name__ == "__main__":
    try:
        password = input("Enter a password to check: ")
        score, rating, feedback = check_password(password)
        for line in feedback:
            print(line)
        print("Score:", score, "out of 5")
        print("Overall strength:", rating)
    except (TypeError, ValueError) as error:
        print("Invalid input:", error)
    except KeyboardInterrupt:
        print("\nCancelled.")