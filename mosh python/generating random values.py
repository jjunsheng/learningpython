# build in modules in python
# https://docs.python.org/3/py-modindex.html
# project > external libraries > python 3.7 > lib
import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10, 20))

members = ["John", "Mary", "Bob", "Mosh"]
leader = random.choice(members)
print(leader)