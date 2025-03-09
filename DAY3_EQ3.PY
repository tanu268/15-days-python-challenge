#Implement a program that finds the largest number in a list.

number = [34 , 54 , 67 , 36 , 98]

largest = number[0]

for num in number:
    if num > largest :
        largest = num
        
        
print("The largest number is: " , largest)


#print(max(list))