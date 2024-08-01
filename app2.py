# First attempt at getting flask to work, displays the countries correctly, 
# when city is entered and submit button clicked error occurs

# discovered a different API which returns the country, iso codes, and cities in one request
# going to try with that API to determine if that would work better.

from flask import Flask, render_template, request, redirect, url_for
from country import get_all_countries, get_cities

# Create the Flask app and to instantiate flask function as app
app = Flask(__name__)

default_currency='USD'

# TODO: Check 'error' and 'msg' to ensure there were no problems

@app.route('/',methods=['GET', 'POST'])
def index():
    print('hello')
    country_data = get_all_countries()
    print(country_data['data'][0])
    countries=[country['name'] for country in country_data['data']] # list compehension
    city_data=None
    print(request.method)
    if request.method == 'POST':
        country = request.form['country']
        print(country)
        city = request.form['city']
        print(city)
        city_data=get_cities(country)
        # city_data=[city_name for city_name in city_data['data'] if city_name['city'] == city] # list comprehension
        if 'data' in city_data and city in city_data['data']:
            city_data={'city':city, 'country':country}
    return render_template('index.html', countries=countries, city_data=city_data)

# def index():
#     country_list=[]
#     iso2_list=[]
#     for cntry in country_data['data']:
#         country_list.append(cntry['name'])
#         iso2_list.append(cntry['Iso2'])
#     return render_template('index.html', country_list=country_list)



if __name__ == "__main__":
    app.run()