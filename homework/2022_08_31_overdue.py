# Цель углубить знания по классам, уметь писать несколько классов вместе
# создать класс (сигнального талона), в котором сохраняются запросы с ФИО, датой рождения, возрастом, адресом проживания, диагнозом
# интерфейс, в котором мы будем вводить эти сигнальные талоны
# интерфейс должен иметь меню (по цифре):
#  1. Добавить талон
#  2. Показать все талоны
#  3. Удалить талон
#  4. Взять талон в работу
# * Написать класс медика, и при взятии талона назначать медика на талон (через какой-то индентификатор - отдельное поле в классе)

from tkinter.messagebox import NO
from typing import List
from datetime import date

class Doctor:
        def __init__(self, doctor_name: str):
            self.doctor_name = doctor_name
            
        def __repr__(self) -> List:
            return f"{self.doctor_name}"

class Ticket:
    def __init__(self, full_name: str, birthday, age: int, diagnosis: str) -> List:
        self.full_name = full_name
        self.birthday = birthday
        self.age = age
        self.date = date.today()
        self.diagnosis = diagnosis
        self.doctor: Doctor = None
        self.date_except = None
    
    def ticket_in_work_by(self, doctor: Doctor) -> None:
        self.doctor = doctor
        self.date_except = date.today()

    def tticket_save_to_file(self) -> None:
        with open("id.txt", 'a+') as f:
            
        
    def __repr__(self) -> List:
        return f"{self.full_name} | {self.birthday} | {self.age} | {self.date} | {self.diagnosis} | {self.doctor} | {self.date_except}"
        
ticket = Ticket()
# Tiket safe to file - Отдельный метод сохранения в фаил - отдельный метод загрузки из фаила
# имя фаила id, передаешь в конструктор только id - читает фаил с таким названием

print(ticket)