class MovieBookingSystem:
    def book_ticket(self, name, seats_to_book):
        """
        Book tickets for a movie. Change the seats value in self.movies if book successfully.
        :param name: str, movie name
        :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2), ...]
        :return: str, booking status message. "Movie not found." for no such movie.
                "Booking success." for successfully booking, or "Booking failed." otherwise
        """
        for movie in self.movies:
            if movie['name'] == name:
                seats = np.array(movie['seats'])
                for seat in seats_to_book:
                    row, col = seat
                    if seats[row][col] == 1:
                        return "Booking failed."
                    else:
                        seats[row][col] = 1
                movie['seats'] = seats
                return "Booking success."
        return "Movie not found."