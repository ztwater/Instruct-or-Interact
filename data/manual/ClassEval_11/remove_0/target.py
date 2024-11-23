class BitStatusUtil:
    def remove(states, stat):
        """
        Remove the specified status from the current status,and check the parameters whether they are legal.
        :param states: Current status, int.
        :param stat: Specified status, int.
        :return: The status after removing the specified status, int.
        """
        if not isinstance(states, int):
            print("Error: states should be an integer.")
            return states
        
        if not isinstance(stat, int):
            print("Error: stat should be an integer.")
            return states
        
        if stat & states:
            states = states & ~stat
            print("Specified status removed successfully.")
        else:
            print("Specified status not found in current status.")
        
        return states