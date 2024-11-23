class TimeUtils:
    def get_current_date(self):
        """
        Return the current date in the format of "%Y-%m-%d"
        :return: string
        >>> timeutils.get_current_date()
        "2023-06-14"
        """
        current_date = self.datetime.strftime("%Y-%m-%d")
        return current_date
