# Weather Dashboard Application

## Description: 
    Create a web-based or command-line application that fetches weather data from a public API and displays it to the user. The application should allow users to enter a location (city or coordinates) and display the current weather conditions, as well as a forecast for the next few days.

## Minimum Requirements:

    •	Use functions to structure your code for fetching data, parsing it, and displaying it.
    •	Implement error handling for API requests.
    •	Use containers (lists, dictionaries) to store the weather data.
    •	Incorporate at least one standard library module for parsing JSON (if necessary) and for any other functionality like datetime.
    •	Use TDD with pytest to write tests for your application functions.
    •	Integrate a third-party library for a better user interface (e.g., requests for API calls, Flask for web interface, or Click for command-line interface).

## My twist on this idea

    Turn this into a travel dashboard which displays a map of the area you are visiting, shows the current weather, maybe a 10 day forecast, and also show the exchange rate. 
    
    •   Maybe use geolocation to determine the users current location?
    •   Maybe find an APi to get information about the destination regarding weather for the time of year they are travelling?
    •   Maybe access a flight api for available flights
    •   Maybe access a hotel api for available rooms, Airbnb, vrbo
    •   Maybe access a car rental api for available cars
    •   Maybe find a things to do api

Start with CLI app, then migrate to a Web or GUI interface