class BitStatusUtil:
    def add(states, stat):
        """
        Add a status to the current status,and check the parameters whether they are legal.
        :param states: Current status, int.
        :param stat: Status to be added, int.
        :return: The status after adding the status, int.
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise TypeError("Parameters must be of type int")

        return states + stat
