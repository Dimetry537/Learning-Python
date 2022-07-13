# у игрока есть здоровье, инвентарь, одета одежда(броня), он может носить что-то в руках.
# пользователь умеет сохранять на диск, должен быть статический метод загрузки пользователя по готовым параметрам.
# в начале игрок закружается с пустым инвентарем, и 100 здоровье, и без брони
# игрок может получать урон, но в броне урон не получает(урон получает броня).
# игрок может применять оружие и брать оружие и вещи из инвентаря.
# игрок может выводить свой инвентарь.
# расчет урона по сравнению с объектом, от корого получен урон.
# во время боя использовать метод броска кубика
# сделать отдельно систему боя.
from .inventory import Inventory
from .item import Item
from .armor import Armor
from .weapon import Weapon
from .game_over_error import GameOverError

class Player:
    def __init__(self) -> None:
        self.health = 100
        self.inventory = Inventory()
        self.armor = None# написать класс брони
        self.weapon = None

    def wield_item(self, name: str) -> None:
        armor_or_weapon = self.inventory.find(name)
        if isinstance(armor_or_weapon, Armor):
            self.armor = armor_or_weapon
        elif isinstance(armor_or_weapon, Weapon):
            self.weapon = armor_or_weapon
        elif armor_or_weapon is None:
            print("You can wear only armor or weapon, item %s is in your inventory" % name)
        else:
            print("You can wear only armor or weapon, item %s is not a weapon" % name)

    """
    Method to reduce player health

    :raises GameOverError: in case health is less than zero
    """
    def take_damage(self, damage) -> None:
        if self.armor != None:
            damage = self.armor.absorb(damage)
        if self.health - damage < 0:
            raise GameOverError("You're dead. Game over.")
        self.health -= damage

    def add_to_inventory(self, item: Item) -> None:
        if self.inventory.add(item):
            print('Item added to inventory')
        else:
            print('Inventory is full, please remove something before add')

    def remove_from_inventory(self, name: str) -> None:
        if self.inventory.remove(name):
            print('You dropped %s' % name)
        else:
            print('There is no such item as %s' % s)

    def __repr__(self) -> str:
        output = "Player with health %s and %s " % (self.health, self.inventory)
        if self.armor != None:
            output += "and with armor %s " % self.armor
        if self.weapon != None:
            output += "and with weapon %s " % self.weapon

        return output