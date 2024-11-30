import random
import time
class Character():
    def __init__(self, name, health,):
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

    def monster_kill(self,target):
        if target.health <= 0:
            print(f'{target.name} мертв.')

    def use_item(self,item):
        if item in self.inventory:
            effect = random.randint(1, 100)
            if effect > 50:
                heal = random.randint(20, 35)
                self.health += heal
                print(f'{self.name} использовал {item}! (+{heal} HP). У {self.name} {self.health} HP.')
            else:
                anti_heal = random.randint(15, 20)
                self.health -= anti_heal
                print(f'{self.name} использовал {item}! (-{anti_heal} HP). У {self.name} {self.health} HP.')
        else:
            print(f'У {self.name} нету {item}!')






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
        self.monster_kill(target)
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
               print(f'{self.name} нанес {target.name} {dmg} урона(!!!) (точн. {self.accuracy})! У {target.name} осталось {target.health} HP')
            else:
               target.health -= dmg
               print(f'{self.name} нанес {target.name} {dmg} урона (точн. {self.accuracy})! У {target.name} осталось {target.health} HP')
        else:
            print(f'{self.name} мертв.')


class Item():
    def __init__(self,name,value):
        self.name = name
        self.value = value










#person1 = Character('Аято',100)
#swordsman1 = Swordsman('Райден',100,20)
#mage1 = Mage('Эмилия',80,100)
#cleymor1 = Cleymor('Итто',150,75,1)
#archer1 = Archer('Фишль',75,80,50)



def main_story():
    print('Путешествуя по различным мирам,ты попал в мир,именуемый как Тейват.')
    print('Но однажды,в нем началась катастрофа. Желая покинуть его,на границе с небесами тебе заградило путь Божество. Твои силы не могли сравниться с силами Безымяной Богини,и ты проиграл.')
    print('Очнувшись спустя время,ты не обнаружил ни своего врага,ни разрушений,вызваными катастрофой,ни своих сил и умений.Сколько лет прошло,где твои силы,и как тебе выбраться? Пусть за это время,твое имя навсегда останется в истории этого мира.')
    name = input('Введи свое имя')
    print(f'Тебя зовут {name}. Ты - Мечник!')
    player = Swordsman(name, 100, 30)
    def fight(target):
        while (player.health <= 0) or (target.health <= 0):
            target.health -= player.damage
            player.health -= target.damage
            time.sleep(2)
            if player.health <= 0:
                print('Ты мертв.')


    print('ты пошел нашел врага')
    monster = Swordsman('Слайм',30, 10)
    player.swordsman_attack(monster)
    print('ты пришел в город тебя попросили зачистить данж'
          'ты пошел в данж')






main_story()
