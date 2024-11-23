class TimeUtils:
    def get_current_date(self):
        """
        Return the current date in the format of "%Y-%m-%d"
        :return: string
        """
        current_date = self.datetime.strftime("%Y-%m-%d")
        return current_date