# This is a variable
music = "john"
print(music)

my_string_variable = "my string variable"
print(my_string_variable)
print("This is the value of:", my_string_variable)


# Single-line variables
# Be careful not to abuse this syntax!
name, last_name, age, alias = "cristhian", "ferreira", 16, "cris"
print(f"My name is {name} {last_name}, my age is {age}, and my alias is {alias}")


# Changing the type
name = 35
age = "cristhian"

print(name)
print(age)

# Forcing the type (Type hinting)
address: str = "My address"
address = 35
print(type(address))


# Inputs 

'''
name = input("What is your name? ")
last_name = input("What is your last name? ")
age = input("How old are you? ")
'''


# Numbers do not need quotes
my_int_variable = 5
print(my_int_variable)
print(type(my_int_variable))


# 'str()' converts an int to a str
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)


# This is a text string
# The data type (int, bool, str, etc.) does not matter
print(my_bool_variable, my_int_variable, my_string_variable)


# 'int()' converts decimals to integers (whole numbers)
hello = 5.5
print(hello)
print(int(hello))


# 'len()' counts characters
guitar = 'george'
print(len(guitar))