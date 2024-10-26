class Character():
    def __init__(self,name,health,strenght):
        self.name = name
        self.health = health
        self.strenght = strenght
        self.inventory = []

    def take_item(self,item):
        self.inventory.append(item)
        print(f'Ты взял {item}')
    def drop_item(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f'Ты выбросил {item}')
        else:
            print(f'У тебя нет {item}')

    def attack(self,other):
        dmg = self.strenght
        other.health -= dmg
        print(f'{self.name} нанес {other.name} {dmg} урона! У {other.name} осталось {other.health} HP')





class Item():
    def __init__(self,name,value):
        self.name = name
        self.value = value

chelik = Character('Ayato',100,15)
other = Character('Raiden',50,40)
sword = Item('sword',20)

chelik.take_item('rassekayushiy tuman')
chelik.drop_item('rassekayushiy tuman')
chelik.attack(other)
