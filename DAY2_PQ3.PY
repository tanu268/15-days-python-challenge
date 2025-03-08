# Implement a program that checks if a given string is a palindrome

#Create a Python function to check if a given string is a palindrome

def is_palindrome(s):
    return list(s) == list(reversed(s))

string = input("Enter a string: ")
print("The given string is a palindrome" if is_palindrome(string) else "The given string is not a palindrome")


