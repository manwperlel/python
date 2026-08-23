cut = "not"

while cut == "not":
    password = input("Enter a password: ")
    password_length = len(password)
    
    if password_length < 8:
        print("Password must be at least 8 characters long.")
    elif password == "password" or password == "12345678":
        print("This password is too common.")
    else:
        cut = "yes"

print("Your password is secure!")