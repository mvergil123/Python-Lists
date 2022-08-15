# send internet requests
import http.client
import json


# class
class WeatherApi:


    def __init__(self) -> None:
        
        # create a connection to the api
        self.conn = http.client.HTTPSConnection("yahoo-weather5.p.rapidapi.com")

        # setting a password and username to talk to the api
        self.headers = {
        'X-RapidAPI-Key': "2255b3367emsh3a5f4a2643c57b5p1a43efjsn96722a9f3285",
        'X-RapidAPI-Host': "yahoo-weather5.p.rapidapi.com"
        }



    def get_weather_temperature(self, city):
        # actual request to get the weather
        # sunnyvale
        self.conn.request("GET", f"/weather?location={city}&format=json&u=f", headers=self.headers)

        res = self.conn.getresponse()
        data = res.read()

        # json weather
        weather_data_json = data.decode("utf-8")

        # found code online
        # parse x:
        y = json.loads(weather_data_json)

        # the result is a Python dictionary:
        return int(y["current_observation"]["condition"]["temperature"])









    










