# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, room):
        self.room = room

    def __str__(self):
        return f'Room: {self.room.room_name}\nDescription: {self.room.desc}'

    def new_direction(self, direction):
        if direction == 'n':
            if hasattr(self.room, 'n_to'):
                self.room = self.room.n_to
            else:
                print('=====Woops, you can\'t go that way=====')
        if direction == 's':
            if hasattr(self.room, 's_to'):
                self.room = self.room.s_to
            else:
                print('=====Woops, you can\'t go that way=====')
        if direction == 'w':
            if hasattr('self.room', 'w_to'):
                self.room = self.room.w_to
            else:
                print('=====Woops, you can\'t go that way=====')
        if direction == 'e':
            if hasattr(self.room, 'e_to'):
                self.room = self.room.e_to
            else:
                print('=====Woops, you can\'t go that way=====')
