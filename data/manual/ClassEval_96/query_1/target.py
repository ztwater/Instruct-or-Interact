class WeatherSystem:
    def query(self, weather_list, tmp_units='celsius'):
        """
        Query the weather system for the weather and temperature of the city, and convert the temperature units based on the input parameter.
        :param weather_list: a dictionary of weather information for different cities, dict.
        :param tmp_units: the temperature units to convert to, str.
        :return: the temperature and weather of the city, tuple.
        """
        city_weather = weather_list.get(self.city)
        
        if city_weather:
            weather = city_weather.get('weather')
            temperature = city_weather.get('temperature')

            # Convert the temperature units based on the input parameter
            if tmp_units.lower() == 'celsius':
                temperature = self.celsius_to_fahrenheit(temperature)
            elif tmp_units.lower() == 'fahrenheit':
                temperature = self.fahrenheit_to_celsius(temperature)
            
            return temperature, weather
        
        return None, None