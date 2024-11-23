class CalendarUtil:
    def remove_event(self, event):
        if event in self.events:
            self.events.remove(event)
            print("Event removed successfully.")
        else:
            print("Event not found in the calendar.")