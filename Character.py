class Character():
    def __init__(self,name,health,strenght):
        self.name = name
        self.health = health
        self.strenght = strenght
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

    def attack(self,other):
        dmg = self.strenght
        other.health -= dmg
        print(f'{self.name} нанес {other.name} {dmg} урона! У {other.name} осталось {other.health} HP')

class Mage(Character):
    def __int__(self,name,health,strenght,mana):
        super().__init__(self,name,health,strenght)
        self.mana = mana

    def cast_navik(self,minus_mana):
        self.mana -= minus_mana
        print(f'{self.name} использует заклинание, расходуя {minus_mana} маны (Остал. {self.mana})')

class Varvor(Character):
    def __int__(self,name,health,strenght,yarost):
        super().__init__(self,name,health,strenght)
        self.yarost = yarost

    def attack(self,yarost,other):
        dmg = self.strenght
        other.health -= dmg * yarost
        print(f'{self.name} нанес {other.name} {dmg} урона! (Бонус {yarost}!). У {other} осталось {other.health} HP')





class Item():
    def __init__(self,name,value):
        self.name = name
        self.value = value

person = Character('Аято',100,15)
person2 = Character('Райден',50,40)
mage = Mage('Эмилия',70,40,100)
varvor = Varvor('Итто',150,30)


#sword = Item('sword',20)
