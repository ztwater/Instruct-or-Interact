class CalendarUtil:
    def remove_event(self, event):
        """
        Remove an event from the calendar.
        :param event: The event to be removed from the calendar, dict.
        """
        if event in self.events:
            self.events.remove(event)
            print("Event removed successfully.")
        else:
            print("Event not found in the calendar.")
