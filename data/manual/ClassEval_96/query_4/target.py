class WeatherSystem:
    def query(self, weather_list, tmp_units='celsius'):
        """
        Query the weather system for the weather and temperature of the city, and convert the temperature units based on the input parameter.
        :param weather_list: a dictionary of weather information for different cities, dict.
        :param tmp_units: the temperature units to convert to, str.
        :return: the temperature and weather of the city, tuple.
        """
        self.weather_list = weather_list
        city_info = self.weather_list.get(self.city)
    
        if city_info:
            self.weather = city_info.get('weather')
            self.temperature = city_info.get('temperature')
    
            if tmp_units.lower() == 'fahrenheit':
                self.temperature = self.celsius_to_fahrenheit(self.temperature)
    
        return self.temperature, self.weather