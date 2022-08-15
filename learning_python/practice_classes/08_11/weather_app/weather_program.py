from weather_api_class import WeatherApi
from user_input import UserInput

class WeatherProgram:

    def __init__(self) -> None:
        self.weather_api = WeatherApi()
        self.input = UserInput()

    def start(self):
        # calling weather api instance method and giving the city as a parameter to that method
        city = self.input.get_city()
        city_temperature = self.weather_api.get_weather_temperature(city)

        if city_temperature > 80:
            print(f"The temperature in {city} is {city_temperature}, it will be hot so wear breathable clothing!")
        else:
            print(f"The temperature in {city} is {city_temperature}, it will be chilly so wear suitable clothing!")

