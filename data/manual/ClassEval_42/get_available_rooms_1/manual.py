### Method Description:
    def get_available_rooms(self, room_type):
        """
        Get the number of specific type of available rooms.
        :param room_type: str, the room type that want to know
        :return: int, the remaining number of this type rooms.
        >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        >>> hotel.get_available_rooms('single')
        5
        """

### Solution Code:
    def get_available_rooms(self, room_type):
        return self.available_rooms[room_type]

### Source Code:
    def get_available_rooms(room_type):
        # Assume there is a list of rooms called 'rooms' with each room having a 'type' attribute
        # Count the number of rooms that match the given room_type
        count = 0
        for room in rooms:
            if room.type == room_type:
                count += 1
        return count

### Predicted Code:
    def get_available_rooms(self, room_type):
        """
        Get the number of specific type of available rooms.
        :param room_type: str, the room type that want to know
        :return: int, the remaining number of this type rooms.
        """
        count = self.available_rooms.get(room_type, 0)
        return count

### Adaptation:
Total number: 21
### Raw Output:
```
    def get_available_rooms(self, room_type):
        """
        Get the number of specific type of available rooms.
        :param room_type: str, the room type that want to know
        :return: int, the remaining number of this type rooms.
        """
        count = self.available_rooms.get(room_type, 0)
        return count
```

### Test Code:
class HotelTestAvailableRooms(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel('Test Hotel', {'single': 3, 'double': 2, 'triple': 2})

    def test_get_available_rooms(self):
        result = self.hotel.get_available_rooms('single')
        self.assertEqual(result, 3)

    def test_get_available_rooms_2(self):
        self.hotel.book_room('single', 2, 'guest 1')
        result = self.hotel.get_available_rooms('single')
        self.assertEqual(result, 1)

    def test_get_available_rooms_3(self):
        self.hotel.book_room('single', 3, 'guest 1')
        result = self.hotel.get_available_rooms('single')
        self.assertEqual(result, 0)

    def test_get_available_rooms_4(self):
        self.hotel.book_room('single', 3, 'guest 1')
        result = self.hotel.get_available_rooms('double')
        self.assertEqual(result, 2)

    def test_get_available_rooms_5(self):
        self.hotel.book_room('single', 3, 'guest 1')
        result = self.hotel.get_available_rooms('triple')
        self.assertEqual(result, 2)

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.available_rooms
# method_dependencies: 


