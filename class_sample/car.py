class Gear():
    def __init__(self, ratio: float, max_speed: int) -> None:
        self.ratio = ratio
        self.max_speed = max_speed

class Driver():
    def __init__(self) -> None:
        self.accelerator = 0

class Car():
    def  __init__(self) -> None:
        self.name = "Mersedes C43 AMG"
        self.width = 2016
        self.length = 4692
        self.height = 1402
        self.mass = 1690
        self.brake_power = 0.5
        self.speed = 0
        self.engine = Engine()
        self.transmission = Transmission()
        self.ecu = ECU(self.transmission, self.engine, self)
    
    def status(self):
        return {
            "speed" : self.speed
        }

class Engine():
    def __init__(self) -> None:
        self.power = 390
        self.torgue = 520
        self.type_engine = "front"
        self.piston_count = 6
        self.class_engine = "V"
        self.gasoline = 100
        self.rev_counter = 0
    
    def start(self) -> None:
        self.rev_counter = 1000

    def stop(self) -> None:
        self.rev_counter = 0

    def status(self):
        return {
            "rev": self.rev_counter
        }

# 1st/2nd/3rd/4th/5th/6th/7th/8th/9th gear	5.35/3.24/2.25/1.64/1.21/1.00/0.87/0.72/0.60
class Transmission():
    def __init__(self) -> None:
        self.gear = "Parking"
        self.current_gear_number = -1

        self.gears = [
            Gear(5.35, 40),
            Gear(3.24, 80),
            Gear(2.25, 120),
            Gear(1.64, 160),
            Gear(1.21, 220),
            Gear(1, 250),
            Gear(0.87, 250),
            Gear(0.72, 250),
            Gear(0.6, 250),
        ]
        self.name = "9G-tronic"

    def shift_gear(self, new_gear: int):
        self.current_gear_number = new_gear
        self.gear = self.gears[new_gear]

    def status(self):
        return {
            'current_gear': self.current_gear_number,
            'gears': self.gears
        }

class ECU():
    def __init__(self, transmission: Transmission, engine: Engine, car: Car) -> None:
        self.transmission = transmission
        self.engine = engine
        self.car = car


    def change_gear(self, new_gear: int = None):
        transmission_status = self.transmission.status()
        engine_status = self.engine.status()
        car_status = self.car.status()
        if transmission_status['current_gear'] < 9 and engine_status['rev'] > 5500:
            self.transmission.shift_gear(transmission_status['current_gear'] + 1)

        if new_gear is not None:
            if car_status['speed'] > transmission_status['gears'][new_gear].max_speed:
                raise BaseException('Ты не охуел?')

car = Car()
car.speed = 200
car.transmission.shift_gear(6)
car.ecu.change_gear(3)