# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, room_name, desc, room_items=[]):
        self.room_name = room_name
        self.desc = desc
        self.room_items = room_items
