class CalendarUtil:
    def get_available_slots(self, date):
        """
        Get all available time slots on a given date.
        :param date: The date to get available time slots for, datetime.
        :return: A list of available time slots on the given date, list.
        """
        available_slots = []
        for event in self.events:
            if event['date'].date() == date.date():
                available_slots.append((event['end_time'], event['start_time'] + timedelta(days=1)))
        return available_slots