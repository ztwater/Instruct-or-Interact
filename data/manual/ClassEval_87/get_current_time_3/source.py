class TimeUtils:
    def get_current_time():
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        return current_time