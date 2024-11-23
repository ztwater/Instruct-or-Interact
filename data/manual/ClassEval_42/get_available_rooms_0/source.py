class Hotel:
    def get_available_rooms(room_type):
        # Assume there is a list of rooms called 'rooms' with each room having a 'type' attribute
        # Count the number of rooms that match the given room_type
        count = 0
        for room in rooms:
            if room.type == room_type:
                count += 1
        return count