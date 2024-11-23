class WeatherSystem:
    def celsius_to_fahrenheit(self):
        """
        Convert the temperature from Celsius to Fahrenheit.
        :return: the temperature in Fahrenheit, float.
        """
        fahrenheit = (self.temperature * 9/5) + 32
        return fahrenheit