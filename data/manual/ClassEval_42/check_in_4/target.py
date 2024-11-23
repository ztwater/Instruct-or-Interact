class Hotel:
    def check_in(self, room_type, room_number, name):
        # Check if the specified room type exists in the booked_rooms dictionary
        if room_type not in self.booked_rooms:
            return False
    
        # Check if the specified room number exceeds the available quantity
        if room_number > self.booked_rooms[room_type].get(name, 0):
            return False
    
        # Remove the person's name from the booked_rooms dictionary
        if room_number == self.booked_rooms[room_type].get(name, 0):
            del self.booked_rooms[room_type][name]
        else:
            self.booked_rooms[room_type][name] -= room_number
    
        return True