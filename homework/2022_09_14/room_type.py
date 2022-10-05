from typing import List
import uuid
from datetime import date
from room import Room

class RoomType:
    def __init__(self, type, room_numbers: List[int]) -> None:
        self.type: str = type
        self.available_rooms: List[Room] = [Room(self, room_number) for room_number in room_numbers]

    def clean_room(self, room: Room):
        self.available_rooms.append(room)

    def pick_room(self) -> Room:
        available = self.available_rooms.pop()
        return available

    def __repr__(self) -> str:
        return f"RoomType: {self.type}"