# Given a list of integers, find all the even numbers and store them in a new list

list = [23 , 34 , 67 , 97 , 4 ]

newlist = []

for i in list:
    if i % 2 == 0:
        newlist.append(i)

print("Even number : ", newlist)
