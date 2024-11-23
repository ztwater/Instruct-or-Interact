class Thermostat:
    def simulate_operation(self):
        """
        simulate the operation of Thermostat. It will automatically start the auto_set_mode method to set the operating mode,
        and then automatically adjust the current temperature according to the operating mode until the target temperature is reached.
        :return time: int, the time it took to complete the simulation.
        """
        start_time = time.time()

        self.auto_set_mode()

        while self.current_temperature != self.target_temperature:
            if self.current_temperature < self.target_temperature:
                # Adjust temperature based on mode
                if self.mode == 'cool':
                    self.current_temperature += 1
                elif self.mode == 'heat':
                    self.current_temperature -= 1
            elif self.current_temperature > self.target_temperature:
                # Adjust temperature based on mode
                if self.mode == 'cool':
                    self.current_temperature -= 1
                elif self.mode == 'heat':
                    self.current_temperature += 1

        end_time = time.time()
        return int(end_time - start_time)