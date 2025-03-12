# Write a function to count the number of vowels in a given string.

def count_vowels(text):
    vowels = {'a','e','i','o','u'}
    text = text.lower()
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

input_text = "World"
print(f"Number of vowels: {count_vowels(input_text)}")