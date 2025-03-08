#Write a program to check if a number is prime

number = int(input("Enter a number"))

if number%2 == 0 and number != 2:
    print("Number is not prime")

else :
    print("Number is prime")