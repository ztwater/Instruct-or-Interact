class CalendarUtil:
    def get_available_slots(self, date):
        """
        Get all available time slots on a given date.
        :param date: The date to get available time slots for, datetime.
        :return: A list of available time slots on the given date, list.
        """
        available_slots = []
        start_time = datetime(date.year, date.month, date.day, 0, 0)
        end_time = datetime(date.year, date.month, date.day, 23, 59)
    
        # Check if there are any events on the given date
        events_on_date = self.get_events(date)
        if not events_on_date:
            available_slots.append((start_time, end_time))
            return available_slots
    
        # Sort the events by start time
        events_on_date.sort(key=lambda x: x['start_time'])
    
        # Check for available slots between events
        for i in range(len(events_on_date) - 1):
            slot_start_time = events_on_date[i]['end_time']
            slot_end_time = events_on_date[i + 1]['start_time']
            if slot_start_time < slot_end_time:
                available_slots.append((slot_start_time, slot_end_time))
    
        # Check for available slots before the first event
        first_event_start_time = events_on_date[0]['start_time']
        if start_time < first_event_start_time:
            available_slots.append((start_time, first_event_start_time))
    
        # Check for available slots after the last event
        last_event_end_time = events_on_date[-1]['end_time']
        if last_event_end_time < end_time:
            available_slots.append((last_event_end_time, end_time))
    
        return available_slots