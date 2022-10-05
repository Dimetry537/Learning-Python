

class Room:
    def __init__(self, room_type, number) -> None:
        self.number = number
        self.type = room_type

    def clean(self):
        self.type.clean_room(self)