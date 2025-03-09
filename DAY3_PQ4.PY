#  Create a program that generates the Fibonacci sequence up to a given number of terms

def fib(n):

    a = 0
    b = 1

    if n == 1:
        print(a)

    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)

fib(10)