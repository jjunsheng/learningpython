#handle errors in python program
age = int(input('Age: '))
print(age)

#exit code 0 means code run successfully without any error
#anything code other than 0 means crash
#to handle value error use > *try except*

try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid value')

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')
