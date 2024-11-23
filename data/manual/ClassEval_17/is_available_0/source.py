class CalendarUtil:
    def is_available(calendar, start_time, end_time):
        for event in calendar:
            if start_time < event['end_time'] and end_time > event['start_time']:
                return False
        return True