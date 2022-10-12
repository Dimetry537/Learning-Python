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

from typing import List
from datetime import date
from datetime import datetime

class Doctor:
    def __init__(self, doctor_name: str, specialization: str):
        self.doctor_name = doctor_name
        self.specialization = specialization

    def __repr__(self) -> List:
         return f"{self.doctor_name}{self.specialization}"

class Ticket:
    def __init__(
        self,
        full_name: str,
        birthday: str,
        diagnosis: str,
        age: int = None,
        date_of_the_ticket: date = None,
        doctor: Doctor = None, 
        date_except: date = None
    ) -> List:
        self.full_name = full_name
        self.birthday = birthday
        self.diagnosis = diagnosis
        self.age = age or self.__calculate_age(self.birthday)
        self.date = date_of_the_ticket or date.today()
        self.doctor: Doctor = doctor
        self.date_except = date_except
    
    @classmethod
    def read_from_file(cls, filename):
        with open(filename, 'r', encoding="utf-8") as file:
            lines: List[str] = file.readlines()
            lines = list(map(lambda line: line[:len(line) - 1], lines))
            full_name = lines[0]
            birthday = lines[1]
            age = lines[2]
            date_of_the_ticket = lines[3]
            diagnosis = lines[4]
            doctor = lines[5]
            date_except = lines[6]
            instance = cls(full_name, birthday, diagnosis, age, date_of_the_ticket, doctor, date_except)
        return instance

    def ticket_in_work_by(self, doctor: Doctor) -> None:
        self.doctor = doctor
        self.date_except = date.today()
    
    def write_to_file(self, filename: str):
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(f'{self.full_name}\n{self.birthday}\n{self.age}\n{self.date}\n{self.diagnosis}\n{self.doctor}\n{self.date_except}\n')
            
    def __calculate_age(self, bidthdate_date: str) -> int:
        born = datetime.strptime(bidthdate_date[:10], '%d.%m.%Y')
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born, born.day))

    def __repr__(self) -> List:
        return f"{self.full_name} | {self.birthday} | {self.age} | {self.date} | {self.diagnosis} | {self.doctor} | {self.date_except}"

# class File:

#     def __init__(self, filename):
#         self.filename = filename
#         self.mode = 'a+'

#     def __enter__(self):
#         self.open_file = open(self.filename, self.mode)
#         return self.open_file

#     def __exit__(self, *args):
#         self.open_file.close()

doctor = Doctor('Dr. D. Maksakov', 'уролог')
ticket = Ticket('Иванов И. И.', '01.01.1977', 'острый фарингит')
ticket.ticket_in_work_by(doctor)

print(ticket)
filename = 'ticket.txt'
ticket.write_to_file(filename)

tiket_restored = Ticket.read_from_file(filename)

print(tiket_restored) # call to method __repr__

print(type(ticket.doctor))
print(type(tiket_restored.doctor))