import requests, os
from test import api_key

def get_weather(city):
	weather_key = api_key
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()
	name = weather['name']
	desc = weather['weather'][0]['description']
	temp = weather['main']['temp']
	return [name, desc, temp]

	# label['text'] = format_response(weather)
 
# get_weather('New York')