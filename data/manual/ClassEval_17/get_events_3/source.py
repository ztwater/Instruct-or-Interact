class CalendarUtil:
    def get_events(date):
        # Assuming events are stored in a list of dictionaries
        events = [
            {'date': '2021-01-01', 'event': 'New Year'},
            {'date': '2021-02-14', 'event': 'Valentine\'s Day'},
            {'date': '2021-03-17', 'event': 'St. Patrick\'s Day'},
            # ... more events ...
        ]
        
        # Filter events based on the given date
        filtered_events = [event['event'] for event in events if event['date'] == date]
        
        return filtered_events