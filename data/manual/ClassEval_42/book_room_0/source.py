class Hotel:
    def book_room(room_type):
        # Assume there is a list of available rooms called 'available_rooms'
        available_rooms = ['Single', 'Double', 'Suite']
        
        if room_type in available_rooms:
            return f"A {room_type} room is available."
        else:
            return f"No {room_type} rooms are available."