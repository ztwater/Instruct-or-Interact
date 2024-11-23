class TimeUtils:
    def get_current_time(self):
        """
        Return the current time in the format of '%H:%M:%S'
        :return: string
        """
        current_time = self.datetime.strftime('%H:%M:%S')
        return current_time