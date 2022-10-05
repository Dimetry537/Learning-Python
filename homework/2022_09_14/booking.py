from typing import List
import uuid
from datetime import date
from room_type import RoomType

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