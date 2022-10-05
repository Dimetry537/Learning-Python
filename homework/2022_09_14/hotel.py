from typing import List
import uuid
from datetime import date
from room_type import RoomType
from booking import Booking
from registration import Registration, RegistrationError


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
                room = booking.room_type.pick_room()
                registration = Registration(first_name, last_name, passport_number, room)
                self.registrations.append(registration)
                return registration
        raise RegistrationError()

    def check_out(self, passport_number: str) -> None:
        for registration in self.registrations:
            if passport_number == registration.passport_number:
                registration.check_out()
                registration.room.clean_room()