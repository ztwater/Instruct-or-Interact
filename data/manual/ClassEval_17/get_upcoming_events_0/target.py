class CalendarUtil:
    def get_upcoming_events(self, num_events):
        upcoming_events = []
        current_date = datetime.now().date()
    
        # Check if the given date is in the past
        if self.date < current_date:
            return "Invalid date. Please provide a future date."
    
        # Generate the next n upcoming events
        for i in range(num_events):
            upcoming_events.append(self.date)
            self.date += timedelta(days=1)
    
        return upcoming_events