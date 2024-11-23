class TimeUtils:
    def add_seconds(self, seconds):
        """
        Add the specified number of seconds to the current time
        :param seconds: int, number of seconds to add
        :return: string, time after adding the specified number of seconds in the format '%H:%M:%S'
        >>> timeutils.add_seconds(600)
        "19:29:22"
        """
        current_time = self.datetime
        new_time = current_time + datetime.timedelta(seconds=seconds)
        return new_time.strftime("%H:%M:%S")