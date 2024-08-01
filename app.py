from flask import Flask, render_template, request, redirect, url_for, jsonify
from country import get_countries_and_cities, get_currency, get_flag, get_position
from exchange import get_exchange_rate

# Create the Flask app and to instantiate flask function as app
app = Flask(__name__)

default_currency='USD'
country_data = get_countries_and_cities()
countries=[country['country'] for country in country_data['data']] # list compehension

# def get_weather(country, city):
    
# if travel_city in cities['data']:
#     # get position for city
#     position=longlat.get_position(travel_city)
#     if len(position) > 0:
#         lat_pos=position[0]['latitude']
#         long_pos=position[0]['longitude']
#         # print(f"The coordinates for your destination city are: {lat_pos}, {long_pos}")
#     else:
#         print(f"We could not find the specified city {travel_city}.")
#         # get position for country
#         position=country.get_position(country_iso2)
#         lat_pos=position['data'].get('lat')
#         long_pos=position['data'].get('long')
# else:
#     print(f"We could not find the specified city {travel_city}.")
#     # get position for country
#     position=country.get_position(country_iso2)
#     lat_pos=position['data'].get('lat')
#     long_pos=position['data'].get('long')

# TODO: Check 'error' and 'msg' to ensure there were no problems

# form_submitted = False

@app.route('/',methods=['GET', 'POST'])
def index():      
    selected_country = request.form.get('country', 'Afghanistan').strip() 
    cities = country_data['data'][countries.index(selected_country)]['cities']

    iso2 = country_data['data'][countries.index(selected_country)]['iso2']
    currency = get_currency(iso2)['data'].get('currency')
    # print(f"default {default_currency} currency {currency}")
    exchange_rate = get_exchange_rate(default_currency, currency)['conversion_rate']
    # print(f"exchangerate: {exchange_rate}")
    flag = get_flag(iso2)['data'].get('flag')
    # print(f"flag {flag}")
    # if request.method == "GET":


    return render_template('index.html', 
                        #    form_submitted=form_submitted, 
                           countries=countries, 
                           selected_country=selected_country, 
                           cities=cities, 
                           currency=currency, 
                           exchange_rate=exchange_rate, 
                           flag=flag)

if __name__ == "__main__":
    app.run()