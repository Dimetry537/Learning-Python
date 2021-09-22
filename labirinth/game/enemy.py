''' создать уровень сложности
реакции противника (сон, станлок, броски, сценарий)
дракон проснулся...
ударь в голову, в горло и т.д.
набор действий для противника
названия игроков: человек, большой паук, собака, дракон, минотавр, скелет, летучие мыши, крысы, медведь.
типы атак у противника (список атак).
здоровье у противника
жизненный цикл (где-то появляется, как-то действует, как-то нейтрализуется (словом, оружием)). Конечный автомат
невелирование атак
у противника всегда есть имя и история
противник может убежать в соседнюю комнату и сделать засаду.
Состояния атаки (ожидание, встревожен, сбежал, обезврежен).
'''
from random import random
from .dialog import Dialog
from .fight import Fight
from .sneak import Sneak

class Enemy:
    def __init__(
        self, name: str, 
        history: str, 
        dialog_filename: str,
        fight_filename: str,
        sneak_filename: str,
    ) -> None:
        self.name = name
        self.history = history
        self.dialog = Dialog(dialog_filename)
        self.fight = Fight(fight_filename)
        self.sneak = Sneak(sneak_filename)

    def introduce(self) -> None:
        print(self.history)

    def start_interaction(self, player_action: str) -> None:
        # TODO: change state machine
        if player_action == 'speak':
            self.start_speak()
        elif player_action == 'attack':
            self.start_attack()
        elif player_action == 'sneak':
            if self.start_sneak():
                print("You sneaked on %s", self.name)
            else:
                print("%s noticed you! Prepare to fight!", self.name)
                self.start_fight()
        elif player_action == 'avoid':
            if random() % 2 == 0:
                print("You avoided %s", self.name)
            else:
                print("You failed to avoid %s", self.name)
                self.start_attack()
        else:
            print("action %s is confusing %s please try again.", player_action, self.name)
            print("You can use speak, attack, sneak or avoid words for action.")
