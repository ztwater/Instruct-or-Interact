class WeatherSystem:
    def query(city, unit):
        # Query the weather system for the weather and temperature of the city
        weather = query_weather(city)
        temperature = query_temperature(city)
        
        # Convert the temperature units based on the input parameter
        if unit == 'C':
            temperature = convert_to_celsius(temperature)
        elif unit == 'F':
            temperature = convert_to_fahrenheit(temperature)
        
        return weather, temperature