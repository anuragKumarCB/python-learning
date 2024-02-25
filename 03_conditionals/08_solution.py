# Problem: Check if a password is "Weak", "Medium", or "Strong".
# Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

# take user password
user_password = input("Please enter your password for strength check : ")

# get password length
password_length = len(user_password)

# based on password length provide password strength
if password_length < 6:
    password_strength = "Weak"

elif password_length <= 10:
        password_strength = "Medium"

else:
    password_strength = "Strong"

print("Your password strength is", password_strength)
