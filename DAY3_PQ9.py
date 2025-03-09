# Given a list of words, count the number of words with more than five characters

words = ["apple", "banana", "cherry", "grape", "mango", "strawberry"]

count = 0  # Initialize counter

for word in words:
    if len(word) > 5:  # Check if word length is greater than 5
        count += 1  

print("Number of words with more than 5 characters:", count)
