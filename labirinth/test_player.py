from game.weapon import Weapon
from game.player import Player, GameOverError
from game.armor import Armor
from game.game_over_error import GameOverError

player = Player()
player.add_to_inventory(Armor('Robe', 0.1))
player.add_to_inventory(Weapon('Sword', 3))
player.wield_item('Robe')
player.wield_item('Sword')
print(player)

player.take_damage(10)

print(player)


axe = Weapon('Axe', 20)
player.take_damage(axe.hit())

print(player)

nuclear_bomb = Weapon('Bomb', 100000)

try:
    player.take_damage(nuclear_bomb.hit())
except GameOverError as error:
    print("Game error: {0}".format(error))
