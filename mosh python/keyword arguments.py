def greetings(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard!')


#keyword argument, fix position *should always come after positioning argument
print("Start")
greetings(last_name="John", first_name="Smith")
greetings("Smith", last_name="John")
#calc_cost(total=50, shipping=5, discount=0.1)
print("Finish")

