# Create a function to find the square of each element in a given list

def square(numbers):
    return [num*num for num in numbers]

numbers = [1 , 2 , 4 , 4 ]

print(square(numbers))
