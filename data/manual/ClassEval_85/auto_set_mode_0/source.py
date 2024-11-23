class Thermostat:
    def auto_set_mode(current_temperature, target_temperature):
        if current_temperature < target_temperature:
            operating_mode = 'heat'
        else:
            operating_mode = 'cool'
        return operating_mode