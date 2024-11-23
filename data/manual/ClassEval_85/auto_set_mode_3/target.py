class Thermostat:
    def auto_set_mode(self):
        """
        Automatically set the operating mode by comparing with the current temperature and target temperature. 
        If the current temperature is lower than the target temperature, the operating mode is set to 'heat', otherwise it is set to 'cool'.
        """
        if self.current_temperature < self.target_temperature:
            self.mode = 'heat'
        else:
            self.mode = 'cool'