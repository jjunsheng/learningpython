#write a program to find the largest number in a list

numbers = [0, 2, 3, 65, 7, 1]
largest_number = 0

for number in numbers:
    if number >= largest_number:
        largest_number = number
print(largest_number)

#solution
numbers = [0, 2, 3, 66, 7, 1]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)