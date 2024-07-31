import requests
import os
from dotenv import load_dotenv

def get_exchange_rate(fromCurrency,toCurrency):
    # get api key
    load_dotenv()
    api_key = os.getenv("EXCHANGE_API_KEY")
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{fromCurrency}/{toCurrency}"

    response = requests.request("GET", url)

    # print(response.text)

    result = response.json()

    return result