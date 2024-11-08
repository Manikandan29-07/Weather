
import requests
from django.conf import settings

def get_weather_data(city):
    api_key = 'e771ac004ecb8bd40740087d16cb6958'
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}&units=m"
    response = requests.get(url)
    return response.json()
