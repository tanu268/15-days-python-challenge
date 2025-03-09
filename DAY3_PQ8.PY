# Create a loop that prints all prime numbers between 1 and 50

for num in range(2, 51):  # Start from 2, since 1 is not prime
    is_prime = True  # Assume number is prime

    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to sqrt(num)
        if num % i == 0:
            is_prime = False  # Not a prime number
            break  # Exit loop early if a divisor is found

    if is_prime:
        print(num, end=" ")  # Print all prime numbers in one line
