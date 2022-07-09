class Gear():
    def __init__(self, ratio) -> None:
        self.ratio = ratio

class Rider():
    def __init__(self) -> None:
        self.power = 10

class Bicycle():
    def  __init__(self, rider) -> None:
        self.width = 10
        self.length = 110
        self.height = 50 
        self.gears = [Gear(0.3), Gear(0.5), Gear(0.6)]
        self.selected_gear = self.gears[0]
        self.mass = 100
        self.rider = rider
        self.brake_power = 0.5
        self.speed = 0
    
    def move(self):
        self.speed += self.rider.power * self.selected_gear.ratio

    def change_gear(self, number_of_gear) -> bool:
        if number_of_gear > len(self.gears):
            return False

        self.selected_gear = self.gears[number_of_gear]

        return True

    def slow_down(self, force = None):
        if force == None:
            self.speed -= self.brake_power
        else:
            self.speed -= force


rider = Rider()
bicycle = Bicycle(rider)
bicycle.move()
bicycle.change_gear(2)
bicycle.move()
bicycle.slow_down()
bicycle.change_gear(2)