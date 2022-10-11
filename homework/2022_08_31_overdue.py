# Цель углубить знания по классам, уметь писать несколько классов вместе
# создать класс (сигнального талона), в котором сохраняются запросы с ФИО, датой рождения, возрастом, адресом проживания, диагнозом
# интерфейс, в котором мы будем вводить эти сигнальные талоны
# интерфейс должен иметь меню (по цифре):
#  1. Добавить талон
#  2. Показать все талоны
#  3. Удалить талон
#  4. Взять талон в работу
# * Написать класс медика, и при взятии талона назначать медика на талон (через какой-то индентификатор - отдельное поле в классе)
# Tiket safe to file - Отдельный метод сохранения в фаил - отдельный метод загрузки из фаила
# имя фаила id, передаешь в конструктор только id - читает фаил с таким названием

from tkinter.messagebox import NO
from typing import List
from datetime import date

class Doctor:
    def __init__(self, doctor_name: str):
        self.doctor_name = doctor_name
            
    def __repr__(self) -> List:
         return f"{self.doctor_name}"

class Ticket:
    def __init__(self, full_name: str, birthday, diagnosis: str) -> List:
        self.full_name = full_name
        self.birthday = birthday
        self.age = 
        self.date = date.today()
        self.diagnosis = diagnosis
        self.doctor: Doctor = None
        self.date_except = None
        
    def calculate_age(born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born, born.day))
    
    def ticket_in_work_by(self, doctor: Doctor) -> None:
        self.doctor = doctor
        self.date_except = date.today()
            
    def __repr__(self) -> List:
        return f"{self.full_name} | {self.birthday} | {self.age} | {self.date} | {self.diagnosis} | {self.doctor} | {self.date_except}"

class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()

doctor = Doctor('Dr. D. Maksakov')
ticket = Ticket('Иванов И. И.', '01.01.1977', )