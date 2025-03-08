def count_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}  # Set of vowels
    text = text.lower()  # Convert to lowercase
    count = 0  # Initialize counter

    for char in text:  # Loop through each character
        if char in vowels:  # Check if it's a vowel
            count += 1

    return count  # Return the final count

# Example usage
input_text = "World"
print(f"Number of vowels: {count_vowels(input_text)}")
