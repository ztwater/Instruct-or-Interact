class MovieBookingSystem:
    def book_ticket(self, name, seats_to_book):
        """
        Book tickets for a movie. Change the seats value in self.movies if book successfully.
        :param name: str, movie name
        :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2), ...]
        :return: str, booking status message. "Movie not found." for no such movie.
                "Booking success." for successfully booking, or "Booking failed." otherwise
        """
        # Find the movie in self.movies
        movie = next((movie for movie in self.movies if movie['name'] == name), None)
    
        if movie:
            # Convert seats_to_book to a set for efficient membership checking
            seats_to_book = set(seats_to_book)
    
            # Check if all seats in seats_to_book are available
            if all(movie['seats'][row][col] == 0 for row, col in seats_to_book):
                # Update the seats to 1 to indicate that they are booked
                for row, col in seats_to_book:
                    movie['seats'][row][col] = 1
    
                return 'Booking success.'
            else:
                return 'Booking failed.'
        else:
            return 'Movie not found.'