class TimeUtils:
    def add_seconds(self, seconds):
        current_time = self.datetime
        new_time = current_time + datetime.timedelta(seconds=seconds)
        return new_time.strftime('%H:%M:%S')