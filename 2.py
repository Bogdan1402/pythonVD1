class Character:
    def __init__(self, name: str, life: int, bronya: int):
        self.name = name
        self.life = life
        self.bronya = bronya

    def attack(self, who: 'Character'):
        while who.bronya > 0:
            who.bronya -= self.damage
        else:
            who.life -= self.damage
            if who.life <= 0:
                print(f"{who.name} gave over")
        print(f"{self.name} -> {who.name} {self.damage} uron")

class Warrior(Character):
    damage = 1

class Mage(Character):
    damage = 5

cha = Warrior("Join", 5, 0)
cah1 = Mage('Miya', 8, 10)
cha.attack(cha)
cha.attack(cha)
cha.attack(cha)
cha.attack(cha)
cha.attack(cha)