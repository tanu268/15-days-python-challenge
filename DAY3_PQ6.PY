# Implement a program that prints the multiplication table of a given number

num = int(input("Enter a number"))

for i in range(1,11):
    print(f"{num}X{i} = {num*i}")