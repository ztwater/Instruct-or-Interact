class Thermostat:
    def set_mode(self, mode):
        """
        Set the working mode of the thermostat.
        :param mode: str, working mode. only ['heat', 'cool']
        """
        self.mode = mode