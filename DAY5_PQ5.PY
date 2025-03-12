# Given a string, write a function to remove all vowels from it and return the modified string

def remove_vowels(s):
    return "".join([char for char in s if char.lower() not in "aeiou"])

print(remove_vowels("Hello World"))