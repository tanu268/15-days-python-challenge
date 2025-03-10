#Write a function to check if a number is even or odd and return "Even" or "Odd" accordingly

def is_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

print(is_even(127))
       