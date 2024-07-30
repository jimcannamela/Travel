#  Travel Dashboard
import country
import longlat
import exchange

# ASSUMPTION: User is in the United States and are travelling to a foreign country
# TODO: How do I determine someone's location based on IP address?
default_currency='USD'
'''
MVP

basic flow

user enters which city, country they are travelling to

calls to country state city shall be made to validate the information entered, and retreive the latitude and logitude of the location

call to restcountries shall be made to retreive the country flag, and map

call to the visualcrossing shall be made to retrieve the current and 5-10 day forecast

format this information nice format in a cli

Enhancement

migrate to a web or gui

Stretch

how do we determine current location based on ip address?

add more features

need to find an api or website which would have information on weather seasons

need to find an api which would have airline, car rental and hotel information

need to find an api which has things to do information

'''

# Get country data for list box

countries = country.get_all_countries()

# TODO: need to handle when error is True

# print(type(countries))
# print(countries)
# print(countries['error'])
# print(countries['msg'])

print("Welcome to Travel Dashboard!")

# travel_country = input("Please enter which country you would like to visit: ")

# print(travel_country)

# travel_city = input("Please enter which city in this country you would like to visit: ")

# print(travel_city)

# TODO: put country in a loop
travel_country='Spain'
country_iso2=''
travel_city='Pittsburgh'

for country_item in countries['data']:
    if country_item['name'] == travel_country:
        country_iso2=country_item['Iso2']
        break

print(f"Country name: {travel_country} iso2: {country_iso2}")

if country_iso2 == '':
    print('Country not found, please try a different country')

# get a list of all of the cities for the country

cities = country.get_cities(travel_country)

# TODO: turn this into another list box

if travel_city in cities['data']:
    # get position for city
    position=longlat.get_position(travel_city)
    lat_pos=position[0]['latitude']
    long_pos=position[0]['longitude']
    print(f"The coordinates for your destination city are: {lat_pos}, {long_pos}")
else:
    print(f"We could not find the specified city {travel_city}.")
    # get position for country
    position=country.get_position(country_iso2)
    lat_pos=position['data'].get('lat')
    long_pos=position['data'].get('long')
    print(f"The coordinates for your destination country are: {lat_pos}, {long_pos}")

# get country flag

country_flag=country.get_flag(country_iso2)['data'].get('flag')

print(country_flag)

# get currency

country_currency=country.get_currency(country_iso2)['data'].get('currency')

print(country_currency)

# get exchange rate

country_exchange_rate=exchange.get_exchange_rate(default_currency,country_currency)['conversion_rate']

print(country_exchange_rate)

# get weather

# location_weather=

# 


