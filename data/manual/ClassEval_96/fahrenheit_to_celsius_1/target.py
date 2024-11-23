class WeatherSystem:
    def fahrenheit_to_celsius(self):
        """
        Convert the temperature from Fahrenheit to Celsius.
        :return: the temperature in Celsius, float.
        """
        celsius = (self.temperature - 32) * 5/9
        return celsius