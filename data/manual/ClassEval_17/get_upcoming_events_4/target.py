class CalendarUtil:
    def get_upcoming_events(self, num_events):
        """
        Get the next n upcoming events from the current date.
        :param num_events: The number of upcoming events to get, int.
        :return: A list of the next n upcoming events from the current date, list.
        """
        upcoming_events = []
        current_date = datetime.now().date()

        # Generate the next n upcoming events
        for event in self.events:
            event_date = event['date'].date()
            if event_date >= current_date and len(upcoming_events) < num_events:
                upcoming_events.append(event)

        return upcoming_events