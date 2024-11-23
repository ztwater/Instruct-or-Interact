class MovieBookingSystem:
    def available_movies(start_time, end_time):
        # Assuming there is a movie database or API to fetch the available movies
        movie_database = {
            "Movie 1": {
                "start_time": "09:00",
                "end_time": "11:00"
            },
            "Movie 2": {
                "start_time": "12:00",
                "end_time": "14:00"
            },
            "Movie 3": {
                "start_time": "15:00",
                "end_time": "17:00"
            }
        }
    
        available_movies = []
    
        for movie, timings in movie_database.items():
            movie_start_time = timings["start_time"]
            movie_end_time = timings["end_time"]
    
            if start_time <= movie_start_time <= end_time or start_time <= movie_end_time <= end_time:
                available_movies.append(movie)
    
        return available_movies