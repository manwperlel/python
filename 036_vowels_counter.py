word = input("enter a word:").lower()
vowel_count = 0

for i in word:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowel_count += 1

print(f"your word has {vowel_count} vowels.")