import requests
import os
from dotenv import load_dotenv

# # API variables


# EXCHANGE_API_URL="https://v6.exchangerate-api.com/v6/"

# import requests

# # Where USD is the base currency you want to use
# url = 'https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/USD'
# GET https://v6.exchangerate-api.com/v6/YOUR-API-KEY/pair/EUR/GBP
# # Making our request
# response = requests.get(url)
# data = response.json()

# # Your JSON object
# print data
		

def get_exchange_rate(fromCurrency,toCurrency):
    # get api key
    load_dotenv()
    api_key = os.getenv("EXCHANGE_API_KEY")
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{fromCurrency}/{toCurrency}"

    response = requests.request("GET", url)

    # print(response.text)

    result = response.json()

    return result