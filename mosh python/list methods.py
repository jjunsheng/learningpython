numbers = [5, 2, 1, 7, 5, 4]
numbers2 = numbers.copy()

numbers.append(20)
print(numbers)

print(numbers.count(5))
print(5 in numbers)
print(numbers.index(5))

#insert index in specific position
numbers.insert(0, 322)
print(numbers)

#ascending order
numbers.sort()
print(numbers)

#descending order
numbers.reverse()
print(numbers)

#remove specific number
numbers.remove(4)
print(numbers)

#remove last number
numbers.pop()
print(numbers)

#clear all
numbers.clear()
print(numbers)

