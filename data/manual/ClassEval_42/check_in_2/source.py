class Hotel:
    def check_in(room_type, room_number, name):
        # Assuming you have a list of booked rooms with their details
        booked_rooms = [
            {"room_type": "Single", "room_number": 101, "name": "John"},
            {"room_type": "Double", "room_number": 201, "name": "Jane"},
            {"room_type": "Single", "room_number": 102, "name": "John"},
            {"room_type": "Double", "room_number": 202, "name": "Jane"},
        ]
        
        # Iterate over the booked rooms and check if the specified room is booked by the specified person
        for room in booked_rooms:
            if room["room_type"] == room_type and room["room_number"] == room_number and room["name"] == name:
                return True
        
        return False