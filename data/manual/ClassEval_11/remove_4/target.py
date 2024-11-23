class BitStatusUtil:
    def remove(states, stat):
        """
        Remove the specified status from the current status,and check the parameters whether they are legal.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :return: The status after removing the specified status,int.
        """
        if isinstance(states, int):
            states_bin = bin(states)[2:]  # Convert states to binary string
            stat_bin = bin(stat)[2:]  # Convert stat to binary string
            if stat_bin in states_bin:
                new_states_bin = states_bin.replace(stat_bin, '')  # Remove stat from states_bin
                new_states = int(new_states_bin, 2)  # Convert new_states_bin back to int
                return new_states
            else:
                print("Specified status not found in current status.")
        else:
            print("Error: states should be an integer.")
    
        if not isinstance(stat, int):
            print("Error: stat should be an integer.")
    
        return None