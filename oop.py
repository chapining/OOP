class NPC:
    IS_ALIVE = True

    def __init__(self):
        self.TEST = False


class Zombie(NPC):
    SPEED = 100
    def __init__(self, NAME="default", HP = "100", FULLNESS = 0):
        super().__init__()
        self.NAME = NAME
        self.HP = HP
        self.FULLNESS = FULLNESS

    def eat(self):
        self.FULLNESS += 10
        print("Brains-s-s-s!")

    @classmethod
    def change_SPEED(cls, SPEED):
        cls.SPEED += SPEED


class Human(NPC):
    def __init__(self, FULLNESS = 100):
        self.FULLNESS = FULLNESS


    def eat(self):
        self.FULLNESS += 5
        print("om-nom-nom")


z1 = Zombie(NAME = "Bob", HP = 150, FULLNESS = 50)
z2 = Zombie(NAME = "Bobby", HP = 90)
h1 = Human(FULLNESS = 95)


print(z1.NAME)
print(z2.NAME)
print(z1.HP)
print(z2.HP)
print(z1.FULLNESS)
print(z2.FULLNESS)


print()
print()


print(z1.SPEED)
print(z2.SPEED)

Zombie.change_SPEED(10)

print(z1.SPEED)
print(z2.SPEED)

print(z2.IS_ALIVE)
print(z1.TEST)


print(h1.FULLNESS)
h1.eat()
print(h1.FULLNESS)


