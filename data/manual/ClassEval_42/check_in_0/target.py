class Hotel:
    def check_in(self, room_type, room_number, name):
        # Check if the specified room type is in the booked_rooms
        if room_type not in self.booked_rooms:
            return False
    
        # Check if the specified room number is greater than the quantity in booked_rooms
        if room_number > self.booked_rooms[room_type].get(name, 0):
            return False
    
        # If the specified room is booked by the specified person, remove their name
        if room_number == self.booked_rooms[room_type].get(name, 0):
            del self.booked_rooms[room_type][name]
        else:
            self.booked_rooms[room_type][name] -= room_number