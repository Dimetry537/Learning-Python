# Автомобильный сервис
# Классы - техническая карта, механик


from typing import List
from datetime import date

class Mechanic:
    def __init__(self, name, specialization) -> None:
        self.name = name
        self.specialization = specialization

    def __repr__(self) -> List:
        return f"{self.name} | {self.specialization} |"


class TechnicalCard:
    def __init__(self, car_brand, state_number, mileage, tech_comments) -> None:
        self.car_brand = car_brand
        self.state_number = state_number
        self.mileage = mileage
        self.tech_comments = tech_comments
        self.mechanic: Mechanic = None
        self.work_started = None

    def take_in_work_by(self, mechanic: Mechanic) -> None:
        self.mechanic = mechanic
        self.work_started = date.today()

    def __repr__(self) -> List:
        return f"| {self.car_brand} | {self.state_number} | {self.mileage} | {self.tech_comments} | {self.mechanic} {self.work_started} "

mechanic = Mechanic('Vasa', 'Everything')
mb_card = TechnicalCard('MB', 'o111oo77', 12345, 'Problem with stearing')
print(mb_card)
mb_card.take_in_work_by(mechanic)
print(mb_card)