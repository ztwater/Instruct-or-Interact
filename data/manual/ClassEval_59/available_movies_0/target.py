class MovieBookingSystem:
    def available_movies(self, start_time, end_time):
        """
        Get a list of available movies within the specified time range
        :param start_time: str, start time in HH:MM format
        :param end_time: str, end time in HH:MM format
        :return: list of str, names of available movies
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.available_movies('12:00', '22:00')
        ['Batman']
        """
        available_movies = []
    
        for movie in self.movies:
            movie_start = movie["start_time"]
            movie_end = movie["end_time"]
    
            if start_time <= movie_start <= end_time or start_time <= movie_end <= end_time:
                available_movies.append(movie["name"])
    
        return available_movies
