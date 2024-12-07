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
    def __init__(self,name,health,mana,damage):
        super().__init__(name,health)
        self.mana = mana
        self.damage = damage

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

item1 = Item('Яблоко', 5)

#swordsman1 = Swordsman('Райден',100,20)
#mage1 = Mage('Эмилия',80,100)
#cleymor1 = Cleymor('Итто',150,75,1)
#archer1 = Archer('Фишль',75,80,50)


player_live = True
def main_story():

    print('Путешествуя по различным мирам,ты попал в мир,именуемый как Тейват.')
    print('Но однажды,в нем началась катастрофа. Желая покинуть его,на границе с небесами тебе заградило путь Божество. Твои силы не могли сравниться с силами Безымяной Богини,и ты проиграл.')
    print('Очнувшись спустя время,ты не обнаружил ни своего врага,ни разрушений,вызваными катастрофой,ни своих сил и умений.Сколько лет прошло,где твои силы,и как тебе выбраться? Пусть за это время,твое имя навсегда останется в истории этого мира.')
    name = input('Введи свое имя')
    print('К чему лежет твоя душа? Выбери цифру')
    player_class = int(input('1) Мечник 2) Стрелок 3) Маг'))
    if player_class == 1:
        player = Swordsman(name, 120, 30)
    if player_class == 2:
        player = Archer(name, 90, 30, 50)
    if player_class == 3:
        player = Mage(name, 100, 100, 35)
#---------------------------------------------------------------------------------------------------
    def fight(target):
        if player_class == 2:
            num = random.randint(0,100)
            if num <= player.accuracy:
                player.damage = player.damage * 1.3
            else:
                player.damage = player.damage

        if player_class == 3:
            num = int(input('Сколько маны потратить?'))
            mana_mnozitel = num // 10
            player.damage = player.damage * mana_mnozitel
        while (player.health > 0) or (target.health >0):
            target.health -= player.damage
            print(f'Ты атакуешь {target.name}! У {target.name} осталось {target.health} HP')
            if player.health <= 0:
                print('Ты погиб')
                player_live = False
                break
            player.health -= target.damage
            print(f'{target.name} атакует тебя! У тебя осталось {player.health} HP')
            if target.health <= 0:
                print(f'{target.name} мертв')
                break
            time.sleep(2)
#--------------------------------------------------------------------------------------------------

    print('Ты проснулся на берегу моря. Отправляйся в лес!')
    print('В лесу ты встретил врага - Слайма!')
    monster1 = Swordsman('Слайм',100, 10)
    fight(target=monster1)
    player.take_item(item1.name)
    print('Со слайма тебе выпало яблоко! Это хороший способ получать ресурсы.')
    time.sleep(4)
    print('Ты отправился дальше. Ты пришел в город ветра - Мондштадт.Каждый город в этом мире подчиняется Архонтам 7 элементов природы.')






while player_live == True:
    main_story()
