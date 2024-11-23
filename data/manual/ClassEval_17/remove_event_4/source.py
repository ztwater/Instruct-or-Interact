class CalendarUtil:
    def remove_event(calendar, event):
        if event in calendar:
            calendar.remove(event)
            print("Event removed successfully.")
        else:
            print("Event not found in the calendar.")
    