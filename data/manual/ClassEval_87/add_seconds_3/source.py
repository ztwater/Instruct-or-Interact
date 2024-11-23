class TimeUtils:
    def add_seconds(seconds):
        current_time = datetime.datetime.now()
        new_time = current_time + datetime.timedelta(seconds=seconds)
        return new_time