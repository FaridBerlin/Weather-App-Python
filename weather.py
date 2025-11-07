from dotenv import load_dotenv
from pprint import pprint
import requests
import os


load_dotenv()

def get_current_weather(city: str = "Berlin"):

    request_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=metric"

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Current Weather Conditions ***\n')

    city = input("\nPlease enter city name: ")
    # Check for empty input and set default city
    if not bool(city.strip()):
        city = "Berlin"

    weather_data = get_current_weather(city)
    
    print('\n')
    pprint(weather_data)

    
    