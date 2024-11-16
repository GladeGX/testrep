
import random
class Character():
    def __init__(self, name, health):
        self.name = name
        self.health = health
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
    def __init__(self,name,health,damage):
        super().__init__(name, health)
        self.damage = damage

    def swordsman_attack(self,target):
        if self.health > 0:
            dmg = self.damage
            target.health-=dmg
            print(f'{self.name} нанес {target.name} {dmg} урона! У {target.name} осталось {target.health} HP')
        else:
            print(f'{self.name} мертв.')

class Mage(Character):
    def __init__(self,name,health,mana):
        super().__init__(name,health)
        self.mana = mana

    def mage_attack(self):
        if self.health > 0:
            mana = self.mana - 35
            print(f'{self.name} использует навык! (ост. {mana} маны)')
        else:
            print(f'{self.name} мертв.')

class Cleymor(Character):
    def __init__(self,name,health,damage,power):
        super().__init__(name,health)
        self.power = power
        self.damage = damage

    def cleymor_attack(self,target):
        if self.health > 0:
            dmg = self.damage * self.power
            target.health -= dmg
            print(f'{self.name} нанес {target.name} {dmg} урона (x1.2)! У {target.name} осталось {target.health} HP')
        else:
            print(f'{self.name} мертв.')
class Archer(Character):
    def __init__(self,name,health,damage,accuracy):
        super().__init__(name,health)
        self.accuracy = accuracy
        self.damage = damage

    def archer_attack(self,target):
        if self.health > 0:
            num = random.randint(1,100)
            dmg = self.damage
            if num > self.accuracy:
               dmg = dmg * 1.5
               target.health -= dmg
               print(f'{self.name} нанес {target.name} {dmg} урона(!!!) (точн. 50)! У {target.name} осталось {target.health} HP')
            else:
               target.health -= dmg
               print(f'{self.name} нанес {target.name} {dmg} урона (точн. 50)! У {target.name} осталось {target.health} HP')
        else:
            print(f'{self.name} мертв.')


class Item():
    def __init__(self,name,value):
        self.name = name
        self.value = value
        self.effect = random.randint(-50,50)







person1 = Character('Аято',100)
swordsman1 = Swordsman('Райден',100,20)
mage1 = Mage('Эмилия',80,100)
cleymor1 = Cleymor('Итто',150,30,1.2)
archer1 = Archer('Фишль',75,80,50)






#действия
