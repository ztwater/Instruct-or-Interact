class Thermostat:
    def simulate_operation(self):
        # Start the auto_set_mode method to set the operating mode
        self.auto_set_mode()
    
        # Rest of the code to simulate the operation of the Thermostat
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
            elif self.mode == 'off':
                break
    
            # Simulating some delay between temperature adjustments
            time.sleep(0.5)
    
        end_time = time.time()
        return int(end_time - start_time)