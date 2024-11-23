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
        self.auto_set_mode()  # Start the auto_set_mode method to set the operating mode
        
        start_time = time.time()
        
        while self.current_temperature != self.target_temperature:
            if self.mode == 'cool':
                if self.current_temperature > self.target_temperature:
                    self.current_temperature -= 1
                else:
                    self.current_temperature += 1
            elif self.mode == 'heat':
                if self.current_temperature < self.target_temperature:
                    self.current_temperature += 1
                else:
                    self.current_temperature -= 1
            time.sleep(1)

        end_time = time.time()
        return int(end_time - start_time)