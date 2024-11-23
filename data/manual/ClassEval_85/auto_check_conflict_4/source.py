class Thermostat:
    def auto_check_conflict(operating_mode, current_temperature, target_temperature):
        if operating_mode == "cool" and current_temperature < target_temperature:
            return True
        elif operating_mode == "heat" and current_temperature > target_temperature:
            return True
        elif operating_mode == "auto" and (current_temperature < target_temperature or current_temperature > target_temperature):
            return True
        else:
            return False