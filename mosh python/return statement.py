#create functions that return value
def square(number):
    return number * number


result = square(3)
print(result)

#directly inside the print function without defining a separate variable
print(square(4))


def square(number):
    print(number * number)


#none return absent of a value
#be default all functions in python return none, can use return to solve
print(square(3))
