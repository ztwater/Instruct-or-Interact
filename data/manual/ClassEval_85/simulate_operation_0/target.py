class Thermostat:
    def simulate_operation(self):
        self.auto_set_mode()
        
        start_time = time.time()
        while self.current_temperature != self.target_temperature:
            if self.current_temperature < self.target_temperature:
                self.current_temperature += 1
            else:
                self.current_temperature -= 1
            time.sleep(1)
            
        return int(time.time() - start_time)