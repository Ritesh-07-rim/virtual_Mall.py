class Character:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def attack(self):
        print(f"{self.name} attacks with health {self.health}")

class Warrior(Character):
    def attack(self):
        #super().attack()
        print(f"{self.name} uses sword with health {self.health}")


class Mage(Character):                
    def attack(self):
        #super().attack()
        print(f"{self.name} uses magic with health {self.health}")

class Archer(Character):
    def attack(self):
       # super().attack()
        print(f"{self.name} uses bow with health {self.health}")



character = [
Warrior("Abhimanyu",100),
Mage("krishna",80),
Archer("surya-putra-karn",50) ]


for char in character:
    char.attack()