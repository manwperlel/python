"""
======================================================================
Python Fundamentals & Syntax Reference Guide
======================================================================

1. BUILT-IN FUNCTIONS & STRING METHODS
----------------------------------------------------------------------
print()     -> Outputs data to the standard console.
input()     -> Prompts the user for text input (returns a string).
type()      -> Identifies the data type of a value or variable.
len()       -> Calculates the length/count of items in a sequence.
int()       -> Converts a compatible value to an integer.
float()     -> Converts a value to a floating-point number.
str()       -> Converts a value to its string representation.
range()     -> Generates a sequence of numbers (start, stop, step).
.lower()    -> Converts all characters in a string to lowercase.

2. ARITHMETIC OPERATORS
----------------------------------------------------------------------
+   -> Addition (also concatenates strings)
-   -> Subtraction
*   -> Multiplication (also repeats strings)
/   -> Division (always returns a float)
//  -> Floor division (truncates decimals, rounds down)
%   -> Modulo (returns the remainder of division)
**  -> Exponentiation (raises to the power of)

3. COMPARISON & MEMBERSHIP OPERATORS
----------------------------------------------------------------------
>   -> Greater than
<   -> Less than
>=  -> Greater than or equal to
<=  -> Less than or equal to
==  -> Equal to
!=  -> Not equal to (different)
in  -> Returns True if a sequence contains a specified value.

4. LOGICAL OPERATORS
----------------------------------------------------------------------
and  -> Returns True if both conditions evaluate to True.
or   -> Returns True if at least one condition evaluates to True.
not  -> Inverts the boolean result (True becomes False, and vice versa).

5. CONTROL FLOW (Conditionals & Loops)
----------------------------------------------------------------------
if       -> Executes code block if condition is True.
elif     -> Evaluates alternative condition if preceding ones were False.
else     -> Fallback block; executes if no conditions were met.
while    -> Repeats a block of code as long as a condition is True.
for      -> Iterates over a sequence (range, string, list, etc.).
break    -> Terminates the loop immediately.
continue -> Skips the rest of the current iteration and moves to the next.

6. SEQUENCE OPERATIONS, FORMATTING & ASSIGNMENT
----------------------------------------------------------------------
+=, -=   -> In-place arithmetic assignment operators.
[index]  -> Accesses an element at a specific zero-based index.
f"{var:.2f}" -> F-string formatting for fixed decimal places (e.g., currency).

======================================================================
"""

print(type("I am a string"))          # Type 'str'
print(type(42))                        # Type 'int'
print(type(3.14159))                   # Type 'float'
print(type(True))                      # Type 'bool'
print(type(print("Hello, world!")))    # Type 'NoneType'