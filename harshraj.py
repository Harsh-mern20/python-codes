import re
def password_strength_analyzer(password):
    score = 0
    feedback = []
    if len(password) > 15:
        score += 3
    elif 12 <= len(password) <= 15:
        score += 2
    else:
        score -= 2
        feedback.append("Consider using at least 12 characters.")
    if re.search(r'[A-Z]', password):
        score += 2
    else:
        feedback.append("Include at least one uppercase letter.")
    if re.search(r'[a-z]', password):
        score += 2
    else:
        feedback.append("Include at least one lowercase letter.")
    if re.search(r'[0-9]', password):
        score += 2
    else:
        feedback.append("Include at least one number.")
    if re.search(r'[@$!%*?&]', password):
        score += 3
    else:
        feedback.append("Include at least one special character (e.g., @$!%*?&).")
    common_patterns = ['password', '123456', 'qwerty', 'abc', 'letmein', 'welcome']
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 5
        feedback.append("Avoid using common patterns or dictionary words.")
    if score < 0:
        strength = "Weak"
    elif 0 <= score <= 6:
        strength = "Moderate"
    else:
        strength = "Strong"

    return score, strength, feedback

def main():
    password = input("Enter a password to analyze: ")
    score, strength, feedback = password_strength_analyzer(password)

    print(f"\nPassword Strength Score: {score}")
    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions for improvement:")
        for suggestion in feedback:
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()