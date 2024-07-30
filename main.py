#  Travel Dashboard
import country

# ASSUMPTION: User is in the United States and are travelling to a foreign country
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

print(type(countries))
# print(countries)
print(countries['error'])
print(countries['msg'])

print("Welcome to Travel Dashboard!")

# travel_country = input("Please enter which country you would like to visit: ")

# print(travel_country)

# travel_city = input("Please enter which city in this country you would like to visit: ")

# print(travel_city)

travel_country='Spain'
country_iso2=''
travel_city='Lisbon'

for country in countries['data']:
    if country['name'] == travel_country:
        country_iso2=country['Iso2']
        break

print(f"Country name: {travel_country} iso2: {country_iso2}")


# is travel_country in country data



travel_country='Timbucktooey'
travel_city='ThreePO'


# is travel_country in country data
country_iso2=''
for country in countries['data']:
    if country['name'] == travel_country:
        country_iso2=country['Iso2']
        break

print(f"Country name: {travel_country} iso2: {country_iso2}")

if country_iso2 == '':
    print('Country not found, please try a different country')

    