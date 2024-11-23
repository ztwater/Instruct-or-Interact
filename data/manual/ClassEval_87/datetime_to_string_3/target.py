class TimeUtils:
    def datetime_to_string(self, datetime):
        """
        Convert a datetime instance to a string
        :param datetime: the datetime instance to convert
        :return: string, converted time string
        """
        return datetime.strftime("%Y-%m-%d %H:%M:%S")