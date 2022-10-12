from typing import List
from doctor import Doctor
from datetime import date
from datetime import datetime

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
    def read_from_file(cls, filename, doctor: Doctor):
        with open(filename, 'r', encoding="utf-8") as file:
            lines: List[str] = file.readlines()
            lines = list(map(lambda line: line[:len(line) - 1], lines))
            full_name = lines[0]
            birthday = lines[1]
            age = lines[2]
            date_of_the_ticket = lines[3]
            diagnosis = lines[4]
            date_except = lines[5]
            instance = cls(full_name, birthday, diagnosis, age, date_of_the_ticket, doctor, date_except)
        return instance

    def ticket_in_work_by(self, doctor: Doctor) -> None:
        self.doctor = doctor
        self.date_except = date.today()
    
    def write_to_file(self, filename: str):
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(f'{self.full_name}\n{self.birthday}\n{self.age}\n{self.date}\n{self.diagnosis}\n{self.date_except}\n')
            
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