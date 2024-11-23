class MovieBookingSystem:
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