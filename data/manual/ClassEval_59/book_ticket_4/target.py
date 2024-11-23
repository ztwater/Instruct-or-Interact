class MovieBookingSystem:
    def book_ticket(self, name, seats_to_book):
        # Check if the movie exists in self.movies
        for movie in self.movies:
            if movie['name'] == name:
                movie_seats = movie['seats']
                
                # Check if there are enough available seats for booking
                if len(seats_to_book) <= np.count_nonzero(movie_seats == 0):
                    # Update the available seats and booked seats
                    for seat in seats_to_book:
                        movie_seats[seat[0]][seat[1]] = 1
                    movie['available_seats'] -= len(seats_to_book)
                    movie['booked_seats'] += len(seats_to_book)
                    return "Booking success."
                else:
                    return "Booking failed."
        
        # Movie not found
        return "Movie not found."