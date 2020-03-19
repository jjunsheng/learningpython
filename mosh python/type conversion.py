#str & int cannot minus each other, ' 2020 ' is a string
#2020 - '1995' , error


birth_year = input('Birth Year: ')

print(type(birth_year))

age = 2020 - int(birth_year)

print(type(age))
print(age)