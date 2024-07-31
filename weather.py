import requests
import os
from dotenv import load_dotenv

def get_weather(latitude,longitude):
    # get api key
    load_dotenv()
    api_key = os.getenv("VISUAL_CROSSING_API_KEY")
    # TODO: determine which portions are really needed, and retreive only those.
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{latitude},{longitude}?key={api_key}"
    # url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city},{country}?key={api_key}"  <-- this may be a better way

    response = requests.request("GET", url)

    # print(response.text)

    result = response.json()

    return result