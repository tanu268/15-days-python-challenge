# Write a Python program to check if a given number is a prime number

num = 3445

for i in range(2,num):
    if num % i == 0:
        print(num,"is not a prime")
        break
else:
        print(num,"is a prime")