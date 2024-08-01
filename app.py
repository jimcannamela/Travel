from flask import Flask, render_template, request, redirect, url_for, jsonify
from country import get_countries_and_cities

# Create the Flask app and to instantiate flask function as app
app = Flask(__name__)

default_currency='USD'
country_data = get_countries_and_cities()
countries=[country['country'] for country in country_data['data']] # list compehension


# TODO: Check 'error' and 'msg' to ensure there were no problems

@app.route('/',methods=['GET', 'POST'])
def index():    
    return render_template('index.html', countries=countries)

###### How do i capture and save the cooresponding iso2 code?
###### How do i capture and save the city data?

@app.route('/get_cities', methods=['GET'])
def get_cities():
    country = request.args.get('country')
    print("I got this country back: ", country)
    cities = country_data['data'][countries.index(country)]['cities']
    print(cities)
    country_iso2 = country_data['data'][countries.index(country)]['iso2']
    print(country_iso2)
    return cities
    # return None

if __name__ == "__main__":
    app.run()