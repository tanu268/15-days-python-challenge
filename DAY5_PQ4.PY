# Write a Python program to check if a given string is a pangram (contains all letters of the alphabet)

import string  # Import module to get all lowercase letters

# Input string
sentence = "The quick brown fox jumps over the lazy dog"

# Convert to lowercase
sentence = sentence.lower()

# Get all lowercase letters (a-z)
alphabet_set = set(string.ascii_lowercase)

# Create a set to store letters found in the sentence
letters_in_sentence = set()

# Loop through the sentence and add only letters to the set
for char in sentence:
    if char.isalpha():  # Check if it's a letter (ignores spaces, numbers, etc.)
        letters_in_sentence.add(char)

# Check if all alphabets are present
if letters_in_sentence == alphabet_set:
    print("✅ The given string is a pangram.")
else:
    print("❌ The given string is NOT a pangram.")