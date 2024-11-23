class Hotel:
    def check_out(available_rooms, room_type, number):
        if room_type in available_rooms:
            available_rooms[room_type] -= number
            if available_rooms[room_type] < 0:
                available_rooms[room_type] = 0
        return available_rooms