class BitStatusUtil:
    def has(states, stat):
        """
        Check if the current status contains the specified status, and check the parameters whether they are legal.
        :param states: Current status, int.
        :param stat: Specified status, int.
        :return: True if the current status contains the specified status, otherwise False, bool.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.has(6, 2)
        True
        """
        return states & stat == stat