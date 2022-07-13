from game.inventory import Inventory
from game.item import Item

inventory = Inventory()

inventory.add(Item('test'))
inventory.add(Item('test 2'))
print(inventory)

print(inventory.remove('test'))
print(inventory.remove('test 2'))
print(inventory)
print(inventory.remove('null'))
print(inventory)

print(inventory.add(Item('knife')))
print(inventory.add(Item('sword')))

print(inventory)