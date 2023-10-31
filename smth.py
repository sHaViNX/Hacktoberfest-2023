def is_valid_password(password):
    if len(password) < 6 or len(password) > 12:
        return "Password is not valid."
    
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "$#@%" for c in password)
    
    if has_lower and has_upper and has_digit and has_special:
        return "Password is valid."
    else:
        return "Password is not valid."

# Read the input password
password = input("Enter Stand Type password: ")

# Check and print the validity of the password
result = is_valid_password(password)
print(result)
