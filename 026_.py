cut = "not"
number_password = 0

while cut == "not":
    password = input("enter a password: ")
    number_password = len(password)
    if number_password < 8:
        print("la contraseña debe tenr al menos 8 caracteres")
    elif password == "password" or password ==  "12345678":
        print("esta contraseña es muy comun")
    else:
        cut = "yes"

print("tu contraseña es segura!")