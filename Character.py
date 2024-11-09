import random
class Character():
    def __init__(self, name, health, age):
        self.name = name
        self.health = health
        self.age = age
        self.inventory = []

    def take_item(self,item):
        self.inventory.append(item)
        print(f'{self.name} взял {item}')
    def drop_item(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f'{self.name} выбросил {item}')
        else:
            print(f'У {self.name} нет {item}')

class Swordsman(Character):
    def __init__(self,name,health,age,damage):
        super().__init__(self, name, health, age)
        self.damage = damage

    def swordsman_attack(self,target):
        dmg = self.damage
        target.health -= dmg
        print(f'{self.name} нанес {target.name} {dmg} урона! У {target.name} осталось {target.health} HP')

class Mage(Character):
    def __init__(self,name,health,age,mana):
        super().__init__(self,name,health,age)
        self.mana = mana

    def mage_attack(self):
        mana = self.mana - 35
        print(f'{self.name} использует навык! (ост. {mana} маны')

class Cleymor(Character):
    def __init__(self,name,health,age,damage,power):
        super().__init__(self,name,health,age)
        self.power = power
        self.damage = damage

    def cleymor_attack(self,target):
        dmg = self.damage * self.power
        target.health -= dmg
        print(f'{self.name} нанес {target.name} {dmg} урона (x1.2)! У {target.name} осталось {target.health} HP')

class Archer(Character):
    def __init__(self,name,health,age,damage,accuracy):
        super().__init__(self,name,health,age)
        self.accuracy = accuracy
        self.damage = damage

    def archer_attack(self,target):
        num = random.randint(1,100)
        if num > self.accuracy:
            dmg = self.damage * 1.5
        target.health -= dmg
        print(f'{self.name} нанес {target.name} {dmg} урона(!!!) (точн. 50)! У {target.name} осталось {target.health} HP')





class Item():
    def __init__(self,name,value):
        self.name = name
        self.value = value

person1 = Character('Аято',100,27)
# swordsman1 = Swordsman('Райден',100,33,40)
mage1 = Mage('Эмилия',80,22,100)
cleymor1 = Cleymor('Итто',150,40,100,1.2)
archer1 = Archer('Фишль',100,90,80,50)
# swordsman1.swordsman_attack(mage1)

#sword = Item('sword',20)



