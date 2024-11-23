class Thermostat:
    def auto_check_conflict(self):
        """
        Check if there is a conflict between the operating mode and the relationship between the current temperature and the target temperature.
        If there is a conflict, the operating mode will be adjusted automatically.
        :return: True if mode isn't conflict with the relationship between the current temperature and the target temperature, or False otherwise.
        """
        if self.mode == "cool" and self.current_temperature < self.target_temperature:
            return True
        elif self.mode == "heat" and self.current_temperature > self.target_temperature:
            return True
        elif self.mode == "auto" and (self.current_temperature < self.target_temperature or self.current_temperature > self.target_temperature):
            return True
        else:
            return False