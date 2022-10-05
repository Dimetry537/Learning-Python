from typing import List
import uuid
from datetime import date
from room import Room

class Registration:
    def __init__(self, first_name: str, last_name: str, passport_number: str, room: Room) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number
        self.room = room
        self.created_at = date.today()
        self.departured_at = None

    def check_out(self) -> None:
        self.departured_at = date.today()

    def __repr__(self) -> str:
        return f"Room #{self.room}: {self.first_name, self.last_name, self.passport_number, self.created_at}"

class RegistrationError(BaseException):
    pass