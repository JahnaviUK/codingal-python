def is_valid_age(age):
    """Checks if the entered age is realistic and valid."""
    return 0 < age <= 120

try:
    user_input = input("Enter your age: ")
    age = int(user_input)

    if is_valid_age(age):
        print(f"Age {age} is valid.")
    else:
        print("Error: The age entered is not realistic. Please enter a valid age between 1 and 120.")
except ValueError:
    print("Error: Please enter a number only (no letters or symbols).")