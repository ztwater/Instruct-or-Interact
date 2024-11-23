class TimeUtils:
    def get_minutes(time1, time2):
        # Convert time1 and time2 to datetime objects
        datetime1 = datetime.strptime(time1, "%H:%M")
        datetime2 = datetime.strptime(time2, "%H:%M")
    
        # Calculate the time difference in minutes
        time_difference = (datetime2 - datetime1).total_seconds() / 60
    
        # Round the result to the nearest minute
        rounded_minutes = round(time_difference)
    
        return rounded_minutes