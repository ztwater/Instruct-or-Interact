class Thermostat:
    def simulate_operation(self):
        """
        simulate the operation of Thermostat. It will automatically start the auto_set_mode method to set the operating mode,
        and then automatically adjust the current temperature according to the operating mode until the target temperature is reached.
        :return time: int, the time it took to complete the simulation.
        >>> thermostat = Thermostat(20.4, 37.5, 'cool')
        >>> thermostat.simulate_operation()
        18
        """
        self.auto_set_mode()
        
        while self.current_temperature != self.target_temperature:
            if self.mode == 'heat':
                if self.current_temperature < self.target_temperature:
                    self.current_temperature += 1
                elif self.current_temperature > self.target_temperature:
                    self.current_temperature -= 1
            elif self.mode == 'cool':
                if self.current_temperature > self.target_temperature:
                    self.current_temperature -= 1
                elif self.current_temperature < self.target_temperature:
                    self.current_temperature += 1
            time.sleep(1)
        
        return int(time.process_time())