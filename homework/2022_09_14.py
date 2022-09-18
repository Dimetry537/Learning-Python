# Цель углубить знания по классам, уметь писать несколько классов вместе
# Задача:
# что осталось - написать функцию выселения в классе отеля, которая будет делать пометку в объекте регистрации о времени выселения
from typing import List
import uuid
from datetime import date

class RoomType:
    def __init__(self, type, room_numbers) -> None:
        self.type: str = type
        self.room_numbers: List[int] = room_numbers
        self.available_rooms: List[int] = self.room_numbers

    def clean_room(self, room_number: int):
        pass

    def pick_room(self) -> int:
        available = self.available_rooms.pop()
        return available

    def __repr__(self) -> str:
        return f"RoomType: {self.type}"


class Booking:
    def __init__(self, first_name: str, last_name: str, room_type: RoomType) -> None:
        self.id = uuid.uuid4()
        self.first_name = first_name
        self.last_name = last_name
        self.room_type = room_type

    def __repr__(self) -> str:
        return f"Booking: {self.first_name, self.last_name, self.room_type}"

    def __str__(self) -> str:
        return f"Booking for {self.last_name}, {self.first_name}"


class Registration:
    def __init__(self, first_name: str, last_name: str, passport_number: str, room_number: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number
        self.room_number = room_number
        self.created_at = date.today()
        self.departured_at = None

    def __repr__(self) -> str:
        return f"Room number #{self.room_number}: {self.first_name, self.last_name, self.passport_number, self.created_at}"

class RegistrationError(BaseException):
    pass

class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.bookings: List[Booking] = []
        self.registrations: List[Registration] = []
        self.room_types: List[RoomType] = [
            RoomType("King Suite", [145, 144]), 
            RoomType("Penthouse", [146])
        ]

    def book_room(self, firstname: str, lastname: str, roomtype: str) -> Booking:
        for room_type in self.room_types:
            if room_type.type == roomtype:
                booking = Booking(first_name=firstname, room_type=room_type, last_name=lastname)
                self.bookings.append(booking)
                return booking
        raise RegistrationError()
       
    def all_bookings(self) -> List[Booking]:
        return self.bookings

    def cancel_booking(self, booking: Booking) -> None:
        self.bookings.remove(booking)

    def registration(self, first_name: str, last_name: str, passport_number: str) -> Registration:
        for booking in self.bookings:
            if booking.first_name == first_name and booking.last_name == last_name:
                room_number = booking.room_type.pick_room()
                registration = Registration(first_name, last_name, passport_number, room_number)
                self.registrations.append(registration)
                return registration
        raise RegistrationError()

hotel = Hotel("Ramada")
dmitry_booking = hotel.book_room("Dmitry", "Maksakov", "King Suite")
denis_booking = hotel.book_room("Denis", "Korobitsin", "Penthouse")
print(hotel.all_bookings())
hotel.cancel_booking(denis_booking)
print(hotel.all_bookings())
dmitry_registration = hotel.registration("Dmitry", "Maksakov", "741234123")
try:
    denis_registration = hotel.registration("Denis", "Korobitsin", "6512312341")
except RegistrationError:
    print("You shell not pass, Denis!")
print(dmitry_registration)
