# Input string
text = input("Enter a string: ")

# Initialize counters
vowels = 0
consonants = 0
digits = 0
special_chars = 0

# Define what counts as a vowel
vowel_list = "aeiouAEIOU"

for char in text:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        if char in vowel_list:
            vowels += 1
        else:
            consonants += 1
    elif not char.isspace(): # Count everything else that isn't a space
        special_chars += 1

# Output results
print("-" * 30)
print(f"Vowels:           {vowels}")
print(f"Consonants:       {consonants}")
print(f"Digits:           {digits}")
print(f"Special Chars:    {special_chars}")
print("-" * 30)
print(f"Total Characters: {len(text)}")