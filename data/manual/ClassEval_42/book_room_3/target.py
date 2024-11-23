class Hotel:
    def book_room(self, room_type, room_number, name):
        if room_type in self.available_rooms:
            if room_number <= self.available_rooms[room_type]:
                if room_type not in self.booked_rooms:
                    self.booked_rooms[room_type] = {}
                
                if name not in self.booked_rooms[room_type]:
                    self.booked_rooms[room_type][name] = room_number
                else:
                    self.booked_rooms[room_type][name] += room_number
                
                self.available_rooms[room_type] -= room_number
                return 'Success!'
            else:
                remaining_rooms = self.available_rooms[room_type]
                if remaining_rooms > 0:
                    return remaining_rooms
                else:
                    return False
        else:
            return False