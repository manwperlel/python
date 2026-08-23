print("Menu:")
print("Press 1 to convert from number to word")
print("Press 2 to convert from word to number")

option = int(input("Choose an option: "))

if option == 1:
    print("Number-to-word converter")
elif option == 2:
    print("Word-to-number converter")
else:
    print("Invalid option")

if option == 1:
    number = int(input("Enter the number you want to convert: "))
    if number == 1:
        print("one")
    elif number == 2:
        print("two")
    elif number == 3:
        print("three")
    elif number == 4:
        print("four")
    elif number == 5:
        print("five")
    else:
        print("This number is unknown")

if option == 2:
    word = input("Enter the word you want to convert: ")
    if word == "one":
        print(1)
    elif word == "two":
        print(2)
    elif word == "three":
        print(3)
    elif word == "four":
        print(4)
    elif word == "five":
        print(5)
    else:
        print("This word is unknown")