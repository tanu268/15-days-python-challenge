#Write a Python function to check if a given string is a palindrome

def is_palindrome(s):
    return list(s) == list(reversed(s))

string = input("Enter a string")

print("The given string is a palinderome"
      if is_palindrome(string)
        else
            "The string is not palindrome")