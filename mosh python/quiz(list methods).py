#write a program to remove the duplicates in a list
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for number in numbers:
    if number in uniques:
        pass
    else:
        uniques.append(number)
print(uniques)

#mosh solution
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)