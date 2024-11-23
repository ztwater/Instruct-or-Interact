class TimeUtils:
    def get_minutes(self, string_time1, string_time2):
        # Convert string_time1 and string_time2 to datetime objects
        datetime1 = self.string_to_datetime(string_time1)
        datetime2 = self.string_to_datetime(string_time2)
    
        # Calculate the time difference in minutes
        time_difference = (datetime2 - datetime1).total_seconds() / 60
    
        # Round the result to the nearest minute
        rounded_minutes = round(time_difference)
    
        return rounded_minutes