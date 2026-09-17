my_string = "my string"
my_other_string = 'my other string'
print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string) # Concatenation (adding a space looks cleaner)

# String with a newline
my_new_line_string = "this is a string \nwith new line"
print(my_new_line_string)

# String with a tab
my_tab_string = "\t this is a string with tab"
print(my_tab_string)

# String with both a tab and a newline
my_tab_string = "\t This is a string with a tab\n and a newline."
print(my_tab_string)

# Escaping characters to print them as literal text
my_escaped_string = "\\t this is a string with \\n" 
print(my_escaped_string)

# Modern f-string (Refactored for cleaner code)
name, last_name, age = "cristhian", "ferreira", 16
print(f"My name is {name} {last_name} and my age is {age}")