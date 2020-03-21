#if name is less than 3 characters long
#name must be at least 3 characters
#otherwise if it's more than 50 characters long
#name can be a maximum of 50 chatacters
#otherwise
#name looks good

name = input('Name : ')

if len(name) < 3:
    print("Name must be a minumum of 3 characters. Please try again.")

elif len(name) > 50:
    print("Name can be a maximum of 50 characters. Please try again.")

else:
    print("Name looks good!")

