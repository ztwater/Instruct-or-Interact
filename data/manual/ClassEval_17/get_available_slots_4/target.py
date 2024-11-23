class CalendarUtil:
    def get_available_slots(self, date):
        """
        Get all available time slots on a given date.
        :param date: The date to get available time slots for, datetime.
        :return: A list of available time slots on the given date, list.
        """
        # Check if provided date is valid
        if not isinstance(date, datetime):
            raise ValueError("Invalid date format. Please provide a valid datetime object.")
            
        # Create a list to store available time slots
        available_slots = []
        
        # Iterate through events and find available time slots
        for event in self.events:
            event_date = event['date'].date()
            if event_date == date.date():
                start_time = event['end_time']
                end_time = start_time + timedelta(hours=1)
                available_slots.append((start_time, end_time))
        
        return available_slots