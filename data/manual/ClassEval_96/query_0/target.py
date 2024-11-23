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
        city_info = weather_list.get(self.city)
        if city_info is None:
            return None
        
        weather = city_info.get('weather')
        temperature = city_info.get('temperature')
        temperature_units = city_info.get('temperature units')
        
        if temperature_units.lower() != tmp_units.lower():
            if temperature_units.lower() == 'celsius' and tmp_units.lower() == 'fahrenheit':
                temperature = self.celsius_to_fahrenheit(temperature)
            elif temperature_units.lower() == 'fahrenheit' and tmp_units.lower() == 'celsius':
                temperature = self.fahrenheit_to_celsius(temperature)
        
        return temperature, weather