def minimumNumber(n, password):
    has_digit = False
    has_lower = False
    has_upper = False
    has_special = False
    special_characters = "!@#$%^&*()-+"

    # Check each character in the password to see if it meets one of the criteria
    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True 
        elif char in special_characters:
            has_special = True
    
    # Count the number of types of characters that are missing
    missing_types = 0
    if not has_digit:
        missing_types += 1
    if not has_lower:
        missing_types += 1
    if not has_upper:
        missing_types += 1
    if not has_special:
        missing_types += 1

    return max(missing_types, 6 - n)

# Example usage
n = 3
password = "Ab1@"
print(minimumNumber(n, password))  # Output: 3
