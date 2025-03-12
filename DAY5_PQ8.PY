#Given a list of names, count the number of names that start with a vowe

def count_names_starting_with_vowel(names):
    return sum(1 for name in names if name[0].lower() in "aeiou")


names = ["Alice", "Bob", "Eve", "Oscar", "Uma", "Charlie"]
print(count_names_starting_with_vowel(names))
