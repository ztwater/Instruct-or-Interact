class MovieBookingSystem:
    def add_movie(self, name, price, start_time, end_time, n):
        """
        Add a new movie into self.movies
        :param name: str, movie name
        :param price: float, price for one ticket
        :param start_time: str
        :param end_time: str
        :param n: int, the size of seats(n*n)
        """
        movie = {
            'name': name,
            'price': price,
            'start_time': datetime.strptime(start_time, "%H:%M"),
            'end_time': datetime.strptime(end_time, "%H:%M"),
            'seats': np.zeros((n, n))
        }
        self.movies.append(movie)