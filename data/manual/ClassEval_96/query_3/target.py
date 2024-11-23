class WeatherSystem:
    def query(self, weather_list, tmp_units = 'celsius'):
        """
        Query the weather system for the weather and temperature of the city,and convert the temperature units based on the input parameter.
        :param weather_list: a dictionary of weather information for different cities,dict.
        :param tmp_units: the temperature units to convert to, str.
        :return: the temperature and weather of the city, tuple.
        >>> weatherSystem = WeatherSystem('New York')
        >>> weather_list = {'New York': {'weather': 'sunny','temperature': 27,'temperature units': 'celsius'},'Beijing': {'weather': 'cloudy','temperature': 23,'temperature units': 'celsius'}}
        >>> weatherSystem.query(weather_list)
        (27, 'sunny')

        """

        # Get the weather and temperature of the city from the weather_list
        weather = weather_list[self.city]['weather']
        temperature = weather_list[self.city]['temperature']
        temperature_units = weather_list[self.city]['temperature units']

        # Convert the temperature units based on the input parameter
        if tmp_units == 'celsius' and temperature_units == 'fahrenheit':
            temperature = self.fahrenheit_to_celsius(temperature)
        elif tmp_units == 'fahrenheit' and temperature_units == 'celsius':
            temperature = self.celsius_to_fahrenheit(temperature)

        return temperature, weather