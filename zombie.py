class Zombie:
	hunger = 0


vasya = Zombie()
print(type(vasya))
print(vasya.hunger)

print("--------------------------------------------")

petya = Zombie()
print(type(petya))
print(petya.hunger)

petya.hunger += 10

print(petya.hunger)
print(vasya.hunger)






class Zombie:
	def __init__(self, hunger=0):
		print("Родился экземпляр зомби")
		self.hunger = hunger
	def eat(self, brains):
		print("зомби съел", brains, "мозгов")
		self.hunger -= brains


vasya = Zombie(100)
vasya.eat(100)
print(vasya.hunger)

petya = Zombie(100)
print(petya.hunger)

del vasya
print(vasya)