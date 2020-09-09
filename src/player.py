# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, room):
        self.room = room

    def __str__(self):
        return f'Room: {self.room.room_name}\nDescription: {self.room.desc}'

    def new_direction(self, direction):
        if direction == 'n':
            self.room = self.room.n_to
        if direction == 's':
            self.room = self.room.s_to
        if direction == 'w':
            self.room = self.room.w_to
        if direction == 'e':
            self.room = self.room.e_to
