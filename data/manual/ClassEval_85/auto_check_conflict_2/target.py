class Thermostat:
    def auto_check_conflict(self):
        if self.mode == "cool" and self.current_temperature < self.target_temperature:
            return True
        elif self.mode == "heat" and self.current_temperature > self.target_temperature:
            return True
        elif self.mode == "auto" and (self.current_temperature < self.target_temperature or self.current_temperature > self.target_temperature):
            return True
        else:
            return False