import requests
import os
from dotenv import load_dotenv

def get_position(city):
    # get api key
    load_dotenv()
    api_key = os.getenv("NINJA_API_KEY")
    api_url = 'https://api.api-ninjas.com/v1/city?name={}'.format(city)

    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:
        # print(response.text)
        result = response.json()
        return result
    else:
        return ("Error:", response.status_code, response.text)