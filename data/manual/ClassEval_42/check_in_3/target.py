class Hotel:
    def check_in(self, room_type, room_number, name):
        """
        Check if the room of the specified type and number is booked by the person named name.
        Remove this name when check in successfuly (room_number is equal to specific person's booked_rooms).
        When the actual check in quantity (room_number) is less than the booked quantity,
        number in booked_rooms will be booked quantity minus actual quantity.
        :param room_type: str, check in room type
        :param room_number: int, check in room number
        :param name: str, person name
        :return: False if the room_type is not in the booked_rooms or room_number is higher than quantity in booked rooms.
        """
        if room_type not in self.booked_rooms:
            return False
        
        if name not in self.booked_rooms[room_type] or self.booked_rooms[room_type][name] < room_number:
            return False
        
        if self.booked_rooms[room_type][name] == room_number:
            del self.booked_rooms[room_type][name]
        else:
            self.booked_rooms[room_type][name] -= room_number
        
        return True