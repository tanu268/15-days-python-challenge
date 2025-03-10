 #Create a function that takes a number as input and prints its multiplication table.

def multiplication(n):
    for i in range(1,11):
      print(f"{n}x{i}={n*i}")

multiplication(3)