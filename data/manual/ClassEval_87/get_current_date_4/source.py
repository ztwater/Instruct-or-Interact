class TimeUtils:
    def get_current_date():
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        return current_date