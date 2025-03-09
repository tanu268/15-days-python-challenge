#Calculate the sum of digits of a given number.

num = int(input("Enter a number: "))  
sum_digits = 0  

while num > 0:  
    sum_digits += num % 10  # Extract last digit and add to sum
    num //= 10  # Remove last digit

print("Sum of digits:", sum_digits)
