class TimeUtils:
    def string_to_datetime(time_string):
        datetime_obj = datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
        return datetime_obj