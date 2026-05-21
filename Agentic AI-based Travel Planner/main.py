#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI

from tools import (
    search_flights,
    recommend_hotels,
    discover_places,
    get_weather,
    estimate_budget
)

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "AI Travel Planner Running Successfully"
    }


@app.get("/travel-plan")
def travel_plan():

    # User Inputs
    source = "Bangalore"
    destination = "Goa"
    days = 3

    # Flight Search
    flights = search_flights(
        source,
        destination
    )

    if not flights:

        return {
            "error": "No flights found"
        }

    selected_flight = flights[0]

    # Hotel Search
    hotels = recommend_hotels(
        destination
    )

    if not hotels:

        return {
            "error": "No hotels found"
        }

    selected_hotel = hotels[0]

    # Tourist Places
    places = discover_places(
        "Beach"
    )

    # Weather Forecast
    weather = get_weather(
        15.2993,
        74.1240
    )

    # Budget Calculation
    total_budget = estimate_budget(
        selected_flight,
        selected_hotel,
        days
    )

    # Final Output
    return {

        "Trip": "Your 3-Day Trip to Goa (Feb 12–14)",

        "Flight Selected":
            f'{selected_flight["airline"]} '
            f'(₹{selected_flight["price"]}) '
            f'- Departs Delhi at '
            f'{selected_flight["departure_time"]}',

        "Hotel Booked":
            f'{selected_hotel["name"]} '
            f'(₹{selected_hotel["price_per_night"]}/night, '
            f'{selected_hotel["stars"]}-star)',

        "Weather": [

            "Day 1: Sunny (31°C)",

            "Day 2: Partly Cloudy",

            "Day 3: Light Breeze"
        ],

        "Itinerary": {

            "Day 1": [
                "Baga Beach",
                "Candolim Market"
            ],

            "Day 2": [
                "Basilica of Bom Jesus",
                "Old Goa Heritage Walk"
            ],

            "Day 3": [
                "Water Sports at Calangute"
            ]
        },

        "Estimated Total Budget": {

            "Flight":
                f'₹{selected_flight["price"]}',

            "Hotel":
                f'₹{selected_hotel["price_per_night"] * 2}',

            "Food & Travel":
                "₹2500",

            "Total Cost":
                f'₹{total_budget}'
        }
    }

