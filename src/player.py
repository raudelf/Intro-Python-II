# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, room):
        self.room = room

    def __str__(self):
        return f'Room: {self.room.room_name}\nDescription: {self.room.desc}'
