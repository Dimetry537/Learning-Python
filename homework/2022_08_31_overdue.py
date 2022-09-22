# Цель углубить знания по классам, уметь писать несколько классов вместе
# создать класс (сигнального талона), в котором сохраняются запросы с ФИО, датой рождения, возрастом, адресом проживания, диагнозом
# интерфейс, в котором мы будем вводить эти сигнальные талоны
# интерфейс должен иметь меню (по цифре):
#  1. Добавить талон
#  2. Показать все талоны
#  3. Удалить талон
#  4. Взять талон в работу
# * Написать класс медика, и при взятии талона назначать медика на талон (через какой-то индентификатор - отдельное поле в классе)

from typing import List


class Ticket:
    def __init__(self, full_name, birthday, age, date, diagnosis, date_except) -> List:
        self.full_name = full_name
        self.birthday = birthday
        self.age = age
        self.date = date
        self.diagnosis = diagnosis
        self.date_except = date_except
        
    def __repr__(self) -> List:
        return f"{self.full_name} | {self.birthday} | {self.age} | {self.date} | {self.diagnosis} | {self.date_except}"
        
class Doctor:
        def __init__(self, doctor_name):
            self.doctor_name = doctor_name
            
        def __repr__(self) -> List:
            return f" | {self.doctor_name}"
        
ticket = Ticket()


print(ticket)