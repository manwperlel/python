### Arithmetic Operators ###

print(3 + 3)
print(3 - 3)
print(3 * 3)
print(3 / 3)
print(3 % 2)   # Remainder
print(10 // 3) # Floor division (rounds down)
print(2 ** 3)  # Exponentiation / Raised to the power of

print(2 ** 3 + 7 // 58 - 67 % 45)

print("hello " + "Python " + "how is it going?") 
print("hello " + str(5))
print("hello " * 5) 
print("hello " * (2 ** 3)) 

my_float = 2.5 * 2
print("hello " * int(my_float))

### Comparison Operators ###

print(3 > 4)  # Is greater than?
print(3 < 4)  # Is less than?
print(3 >= 4) # Is greater than or equal to?
print(3 <= 4) # Is less than or equal to?
print(3 == 4) # Is equal to?
print(3 != 4) # Is not equal to? / Is different?



print("hello" > "python")
print("hello" < "python") 
print("hello" <= "python") 
print("hello" == "python") 
print("hello" != "python") 
print("aaaa" >= "abaa") # Alphabetical order (lexicographical)
print(len("aaaa") >= len("abaa")) 


### Logical Operators ###

print(3 > 4 and "hello" > "python") 
print(3 > 4 or "hello" > "python") 
print(3 < 4 and "hello" < "python") 
print(3 < 4 or "hello" > "python") 
print(not 3 > 4 and "hello" > "python") # Fixed Python syntax for 'not'