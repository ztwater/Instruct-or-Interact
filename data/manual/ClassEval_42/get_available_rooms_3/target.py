class Hotel:
    def get_available_rooms(self, room_type):
        """
        Get the number of specific type of available rooms.
        :param room_type: str, the room type that want to know
        :return: int, the remaining number of this type rooms.
        """
        count = 0
        if room_type in self.available_rooms:
            count = self.available_rooms[room_type]
        return count