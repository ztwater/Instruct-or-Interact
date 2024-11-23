class TimeUtils:
    def get_minutes(self, string_time1, string_time2):
        """
        Calculate how many minutes have passed between two times, and round the results to the nearest
        :return: int, the number of minutes between two times, rounded off
        >>> timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
        60
        """
        # Convert string_time1 and string_time2 to datetime objects
        datetime1 = self.string_to_datetime(string_time1)
        datetime2 = self.string_to_datetime(string_time2)
    
        # Calculate the time difference in minutes
        time_difference = (datetime2 - datetime1).total_seconds() / 60
    
        # Round the result to the nearest minute
        rounded_minutes = round(time_difference)
    
        return rounded_minutes