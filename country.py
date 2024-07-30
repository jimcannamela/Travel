####  GET COUNTRY DATA 

# This module makes all of the calls to the countries now API
# to retrieve information about a country

import requests


# Retrieves a list of all countries for validation.
# TODO: determine how to build a list box with this data

def get_all_countries():
    
    url = "https://countriesnow.space/api/v0.1/countries/iso"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    result = response.json()

    # print(response.text)

    return result

# Retrieves a list of all of the cities for a country

def get_cities(country):

    url = "https://countriesnow.space/api/v0.1/countries/cities"

    payload = {
        "country": country
    }

    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)

    result = response.json()

    return result

# Retrieves the curency for a country

def get_currency(iso2):

    url = "https://countriesnow.space/api/v0.1/countries/currency"

    payload = {
        "iso2": iso2
    }
        
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)

    result = response.json()

    return result


# Retreives the flag url for a country

def get_flag(iso2):

    url = "https://countriesnow.space/api/v0.1/countries/flag/images"

    payload = {
        "iso2": iso2
    }
        
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)

    result = response.json()

    return result

# # Retreives the longitude and latitude for a country
# # TODO: need to investigate if the other API is at the city level
########## found an api at API ninja for cities
##########    if city is not found we can get the country position

def get_position(iso2):

    url = "https://countriesnow.space/api/v0.1/countries/positions"

    payload = {
        "iso2": iso2
    }
        
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)

    result = response.json()

    return result

### End of Module ###