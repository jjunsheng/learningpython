# classify mammals and have dog and cat inherit the def
class Mammal:
    def walk(self):
        print("walk")


# you can have more than 2 inheritance, stupid mosh did'nt explain
class Attack:
    def claw(self):
        print("scratch")


# this is DRY, if walk needs editing we will need to edit 2 times
class Dog(Mammal, Attack):
    def bark(self):
        print("Bark")


class Cat(Mammal, Attack):
    def meow(self):
        print("meow")


kitty1 = Cat()
kitty1.walk()
kitty1.meow()
kitty1.claw()