class player:
	def __init__(self, hp, name, money, inventory, speed, armor, attack):
		print("появление")
		print("-----------------------------")
		self.hp = hp
		self.name = name
		self.money = money
		self.inventory = inventory
		self.speed = speed
		self.armor = armor
		self.attack = attack


	def take_damage(self, damage):
		print("Ай, я получил", damage, "урона")
		self.hp -= damage


	def heal(self, heal):
		print("Я вылечил", heal, "hp")
		self.hp += heal


	def show_stats(self):
		print(self.hp)
		print(self.name)
		print(self.money)
		print(self.inventory)
		print(self.speed)
		print(self.attack)



vasya = player(100, "Vasya", 0, [], 10, 5, 3)
vasya.show_stats()

vasya.take_damage(50)

vasya.heal(40)

