#Create a program that takes a year as input and checks if it is a leap year or not


num = int(input("Enter year : "))
if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
    print("The year is a leap year")
else:
    print("The year is not a leap year")