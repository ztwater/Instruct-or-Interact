class CalendarUtil:
    def get_upcoming_events(date, n):
        upcoming_events = []
        current_date = datetime.datetime.now().date()
        
        # Check if the given date is in the past
        if date < current_date:
            return "Invalid date. Please provide a future date."
        
        # Generate the next n upcoming events
        for i in range(n):
            upcoming_events.append(date)
            date += datetime.timedelta(days=1)
        
        return upcoming_events