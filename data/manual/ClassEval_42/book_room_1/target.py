class Hotel:
    def book_room(self, room_type, room_number, name):
        """
        Check if there are any rooms of the specified type available.
        if rooms are adequate, modify available_rooms and booked_rooms and finish booking, or fail to book otherwise.
        :param room_type: str
        :param room_number: int, the expected number of specified type rooms to be booked
        :param name: str, guest name
        :return: if number of rooms about to be booked doesn't exceed the remaining rooms, return str 'Success!'
                 if exceeds but quantity of available rooms is not equal to zero, return int(the remaining quantity of this room type).
                 if exceeds and quantity is zero or the room_type isn't in available_room, return False.
        """
        if room_type not in self.available_rooms or not isinstance(room_number, int) or not isinstance(name, str):
            return False
    
        if room_number <= self.available_rooms[room_type]:
            if room_type not in self.booked_rooms:
                self.booked_rooms[room_type] = {}
            self.booked_rooms[room_type][name] = room_number
            self.available_rooms[room_type] -= room_number
            return 'Success!'
        elif self.available_rooms[room_type] > 0:
            return self.available_rooms[room_type]
        else:
            return False