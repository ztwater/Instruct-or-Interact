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
        start_time = datetime.strptime(start_time, "%H:%M")
        end_time = datetime.strptime(end_time, "%H:%M")

        available_movies = []

        for movie in self.movies:
            movie_start_time = movie["start_time"]
            movie_end_time = movie["end_time"]

            if start_time <= movie_start_time <= end_time or start_time <= movie_end_time <= end_time:
                available_movies.append(movie["name"])

        return available_movies