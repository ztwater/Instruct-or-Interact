class MovieBookingSystem:
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