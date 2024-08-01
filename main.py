#  Travel Dashboard
import country
import longlat
import exchange
import weather
from datetime import datetime
from pytz import timezone

# ASSUMPTION: User is in the United States and are travelling to a foreign country
# TODO: How do I determine someone's location based on IP address?
default_currency='USD'
degree_sign = u'\N{DEGREE SIGN}'

def wind_angle_to_direction(angle):
    directions = [
        "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
        "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"
    ]
    idx = int((angle + 11.25) / 22.5) % 16
    return directions[idx]    

def convert_time_format(time_str):
    original_time = datetime.strptime(time_str, "%H:%M:%S")
    formatted_time = original_time.strftime("%I:%M %p").lstrip('0')  
    return formatted_time

# Example usage
time_str = "14:35:45"  # Input time string in hh:mm:ss format
converted_time = convert_time_format(time_str)
print(converted_time)  # Output will be '02:35 PM'

# Get country data for list box

countries = country.get_all_countries()                         # TODO: need to handle when error is True

# print(type(countries))
# print(countries)
# print(countries['error'])
# print(countries['msg'])

print("Welcome to Travel Dashboard!\n")

travel_country = input("\nPlease enter which country you would like to visit: ").capitalize()

# print(travel_country)

travel_city = input("\nPlease enter which city in this country you would like to visit: ").capitalize()

# print(travel_city)

# TODO: put country in a loop to ensure a valid country is chosen for CLI 
country_iso2=''

for country_item in countries['data']:
    if country_item['name'].upper() == travel_country.upper():
        country_iso2=country_item['Iso2']
        break

# print(f"\nCountry name: {travel_country} iso2: {country_iso2}")

if country_iso2 == '':
    print('Country not found, please try a different country')

# get a list of all of the cities for the country

cities = country.get_cities(travel_country)         # TODO: turn this into a list box

# print(cities)

if travel_city in cities['data']:
    # get position for city
    position=longlat.get_position(travel_city)
    if len(position) > 0:
        lat_pos=position[0]['latitude']
        long_pos=position[0]['longitude']
        # print(f"The coordinates for your destination city are: {lat_pos}, {long_pos}")
    else:
        print(f"We could not find the specified city {travel_city}.")
        # get position for country
        position=country.get_position(country_iso2)
        lat_pos=position['data'].get('lat')
        long_pos=position['data'].get('long')
else:
    print(f"We could not find the specified city {travel_city}.")
    # get position for country
    position=country.get_position(country_iso2)
    lat_pos=position['data'].get('lat')
    long_pos=position['data'].get('long')
    # print(f"The coordinates for your destination country are: {lat_pos}, {long_pos}")

# get country flag

country_flag=country.get_flag(country_iso2)['data'].get('flag')   

# print(country_flag) #  TODO: display flag as an icon or emoji?

# get currency

country_currency=country.get_currency(country_iso2)['data'].get('currency')

# print(country_currency)

# get exchange rate

country_exchange_rate=exchange.get_exchange_rate(default_currency,country_currency)['conversion_rate']

print(f"\n{travel_city}, {travel_country}")

print(f"\n\tCurrent exchange rate for USD to {country_currency} is {country_exchange_rate}")

# get weather

location_weather=weather.get_weather(lat_pos,long_pos)


local_timezone = timezone(location_weather['timezone'])
local_time = datetime.now(local_timezone)

print(f"\n\tThe current local time is: {local_time.strftime("%I:%M %p").lstrip('0')}")   

current_conditions=location_weather['currentConditions']

wind_direction=wind_angle_to_direction(current_conditions['winddir'])
sunrise_time=convert_time_format(current_conditions['sunrise'])
sunset_time=convert_time_format(current_conditions['sunset'])

print(f"\n\tThe current temperature is: {current_conditions['temp']}{degree_sign}F Feels like {current_conditions['feelslike']}{degree_sign}F")    # TODO: calc in C and display as superscript
print(f"\t\tWind speed: {current_conditions['windspeed']} mph {wind_direction}")                   
print(f"\t\tHumidity: {current_conditions['humidity']} % Precipitation: {current_conditions['precip']} inches")                 # TODO: determine if these are percentages and adjust display accordingly
print(f"\t\tSunrise was at: {sunrise_time} sunset is at {sunset_time}")              # TODO: display time in user friendly format AM/PM
print(f"\t\tCurrent conditions: {current_conditions['conditions']} {location_weather['description']}") # {current_conditions['icon']}") # TODO: determine how to translate icon into an image

# TODO: for now just store the current alerts in a variable possible future work to post them as well
current_alerts=location_weather['alerts']

# print(location_weather['days'])

# TODO: add twisty <div> for 14 day forecast, and sub twistys containing the hourly forecasts for each day

###### FOR NOW JUST SHOW CURRENT WEATHER!!!

# for day in location_weather['days']:
#     print(f"Date: {day['datetime']}")                                                       # TODO: add day of week
#     print(f"\tThe current temperature is: {day['temp']} Feels like {day['feelslike']}")     # TODO: display as F or C with degree symbol
#     print(f"\tHigh: {day['tempmax']} Low: {day['tempmin']}")                                # TODO: display as F or C with degree symbol
#     print(f"\tWind speed: {day['windspeed']} from the {day['winddir']}")                    # TODO: add direction calcuation
#     print(f"\tHumidity: {day['humidity']} Precipitation: {day['precip']}")                  # TODO: need to understand if humidity and precip are percentages
#     print(f"\tSunrise was at: {day['sunrise']} sunset is at {day['sunset']}")               # TODO: need to convert times to friendly AM/PM
#     print(f"\tCurrent conditions: {day['conditions']} {day['description']} {day['icon']}")  # TODO: need to translate icon into an image
#     print(f"\tHourly forecast:")
#     for hour in day['hours']:
#     #     # TODO:  convert times to friendly times 
#          print(f"\t\tTime: {hour['datetime']} Temp: {hour['temp']} Precip Probability: {hour['precipprob']} Condiitons: {hour['conditions']} {hour['icon']}")


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
