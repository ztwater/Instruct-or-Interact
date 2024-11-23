class TimeUtils:
    def get_format_time():
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S")
        return formatted_time