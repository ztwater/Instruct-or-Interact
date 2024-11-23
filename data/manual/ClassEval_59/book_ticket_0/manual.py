### Method Description:
    def book_ticket(self, name, seats_to_book):
        """
        Book tickets for a movie. Change the seats value in self.movies if book successfully.
        :param name: str, movie name
        :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2), ...]
        :return: str, booking status message. "Movie not found." for no such movie.
                "Booking success." for successfully booking, or "Booking failed." otherwise
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.book_ticket('Batman', [(0, 0), (0, 1)])
        'Booking success.'
        >>> system.book_ticket('Batman', [(0, 0)])
        'Booking failed.'
        >>> system.book_ticket('batman', [(0, 0)])
        'Movie not found.'
        """

### Solution Code:
    def book_ticket(self, name, seats_to_book):
        for movie in self.movies:
            if movie['name'] == name:
                for seat in seats_to_book:
                    if movie['seats'][seat[0]][seat[1]] == 0:
                        movie['seats'][seat[0]][seat[1]] = 1
                    else:
                        return "Booking failed."
                return "Booking success."
        return "Movie not found."

### Source Code:
    def book_ticket(self, movie_name, num_tickets):
        # Check if the movie exists in self.movies
        if movie_name in self.movies:
            # Check if there are enough available seats for booking
            if self.movies[movie_name]['available_seats'] >= num_tickets:
                # Update the available seats and booked seats
                self.movies[movie_name]['available_seats'] -= num_tickets
                self.movies[movie_name]['booked_seats'] += num_tickets
                return True
            else:
                return False
        else:
            return False

### Predicted Code:
    def book_ticket(self, name, seats_to_book):
        """
        Book tickets for a movie. Change the seats value in self.movies if book successfully.
        :param name: str, movie name
        :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2), ...]
        :return: str, booking status message. "Movie not found." for no such movie.
                "Booking success." for successfully booking, or "Booking failed." otherwise
        """
        # Check if the movie exists in self.movies
        for movie in self.movies:
            if movie['name'] == name:
                # Check if there are enough available seats for booking
                if len(seats_to_book) <= np.count_nonzero(movie['seats'] == 0):
                    # Update the available seats and booked seats
                    for seat in seats_to_book:
                        movie['seats'][seat[0]][seat[1]] = 1
                    return "Booking success."
                else:
                    return "Booking failed."
        # Movie not found
        return "Movie not found."

### Adaptation:
Total number: 51
### Raw Output:
```
def book_ticket(self, name, seats_to_book):
    """
    Book tickets for a movie. Change the seats value in self.movies if book successfully.
    :param name: str, movie name
    :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2), ...]
    :return: str, booking status message. "Movie not found." for no such movie.
            "Booking success." for successfully booking, or "Booking failed." otherwise
    """
    # Check if the movie exists in self.movies
    for movie in self.movies:
        if movie['name'] == name:
            # Check if there are enough available seats for booking
            if len(seats_to_book) <= np.count_nonzero(movie['seats'] == 0):
                # Update the available seats and booked seats
                for seat in seats_to_book:
                    movie['seats'][seat[0]][seat[1]] = 1
                return "Booking success."
            else:
                return "Booking failed."
    # Movie not found
    return "Movie not found."
```

### Test Code:
class MovieBookingSystemTestBookTicket(unittest.TestCase):
    def setUp(self):
        self.system = MovieBookingSystem()
        self.system.add_movie('Batman', 49.9, '17:05', '19:25', 3)

    # book successfully
    def test_book_ticket_1(self):
        result = self.system.book_ticket('Batman', [(0, 0), (1, 1), (2, 2)])
        self.assertEqual(result, 'Booking success.')
        self.assertEqual(self.system.movies[0]['seats'][0][0], 1)
        self.assertEqual(self.system.movies[0]['seats'][1][1], 1)
        self.assertEqual(self.system.movies[0]['seats'][2][2], 1)

    # seat is not available
    def test_book_ticket_2(self):
        self.system.book_ticket('Batman', [(0, 0)])
        result = self.system.book_ticket('Batman', [(0, 0)])
        self.assertEqual(result, 'Booking failed.')
        self.assertEqual(self.system.movies[0]['seats'][0][0], 1)

    def test_book_ticket_3(self):
        result = self.system.book_ticket('batman', [(0, 0)])
        self.assertEqual(result, 'Movie not found.')
        self.assertEqual(self.system.movies[0]['seats'][0][0], 0)

    def test_book_ticket_4(self):
        result = self.system.book_ticket('Batman', [(0, 0), (1, 1)])
        self.assertEqual(result, 'Booking success.')
        self.assertEqual(self.system.movies[0]['seats'][0][0], 1)
        self.assertEqual(self.system.movies[0]['seats'][1][1], 1)

    def test_book_ticket_5(self):
        result = self.system.book_ticket('Batman', [(0, 0)])
        self.assertEqual(result, 'Booking success.')
        self.assertEqual(self.system.movies[0]['seats'][0][0], 1)

### Test Output:
# 0 errors, 1 failures in 5 runs.
# errors:
# failures:
#     AssertionError:
#         test_book_ticket_2: 'Booking success.' != 'Booking failed.'


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.movies
# method_dependencies: 


