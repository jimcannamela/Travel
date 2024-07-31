import requests
import os
from dotenv import load_dotenv

def get_weather(latitude,longitude):
    # get api key
    load_dotenv()
    api_key = os.getenv("VISUAL_CROSSING_API_KEY")
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{latitude},{longitude}?key={api_key}"

    response = requests.request("GET", url)

    # print(response.text)

    result = response.json()

    return result