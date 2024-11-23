class BitStatusUtil:
    def has(states, stat):
        """
        Check if the current status contains the specified status,and check the parameters whether they are legal.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :return: True if the current status contains the specified status,otherwise False,bool.
        """
        if isinstance(states, int) and isinstance(stat, int):
            return (states & stat) == stat
        else:
            return False