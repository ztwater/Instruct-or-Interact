class Hotel:
    def book_room(self, room_type, room_number, name):
        if room_type not in self.available_rooms:
            return False
    
        if room_number > self.available_rooms[room_type]:
            if self.available_rooms[room_type] == 0:
                return False
            else:
                return self.available_rooms[room_type]
    
        if room_type not in self.booked_rooms:
            self.booked_rooms[room_type] = {}
            
        if name not in self.booked_rooms[room_type]:
            self.booked_rooms[room_type][name] = room_number
        else:
            self.booked_rooms[room_type][name] += room_number
    
        self.available_rooms[room_type] -= room_number
    
        return 'Success!'