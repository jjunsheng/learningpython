def greetings(name):
    print(f'Hi {name}!')
    print('Welcome aboard!')


print("Start")
greetings("John")
greetings("Mary")
print("Finish")


#position argument, first position is first, second is second
def greetings(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard!')


print("Start")
greetings("John", "Smith")
greetings("Mary", "Wood")
print("Finish")