class TimeUtils:
    def string_to_datetime(self, string):
        """
        Convert the time string to a datetime instance
        :param string: string, string before converting format
        :return: datetime instance
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
        datetime_obj = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
        return datetime_obj