class CalendarUtil:
    def get_events(self, date):
        """
        Get all events on a given date.
        :param date: The date to get events for,datetime.
        :return: A list of events on the given date,list.
        """
        filtered_events = [event for event in self.events if event['date'] == date]
        
        return filtered_events