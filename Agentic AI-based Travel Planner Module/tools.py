#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[ ]:


# Load Flights Data
with open("data/flights.json", "r") as f:
    flights_data = json.load(f)

# Load Hotels Data
with open("data/hotels.json", "r") as f:
    hotels_data = json.load(f)

# Load Places Data
with open("data/places.json", "r") as f:
    places_data = json.load(f)


# In[ ]:


def search_flights(source, destination):

    results = []

    for flight in flights_data:
        if (
            flight["from"].lower() == source.lower()
            and
            flight["to"].lower() == destination.lower()
        ):
            results.append(flight)

    return results


# In[ ]:


def recommend_hotels(city):

    results = []

    for hotel in hotels_data:
        if hotel["city"].lower() == city.lower():
            results.append(hotel)

    return results


# In[ ]:


def discover_places(place_type):

    results = []

    for place in places_data:
        if place["type"].lower() == place_type.lower():
            results.append(place)

    return results


# In[ ]:


def estimate_budget(flight, hotel, days):

    total = (
        flight["price"] +
        hotel["price_per_night"] * days +
        (1000 * days)
    )

    return total


# In[ ]:


import requests


def get_weather(latitude, longitude):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": [
            "temperature_2m_max",
            "weathercode"
        ],
        "forecast_days": 3,
        "timezone": "auto"
    }

    response = requests.get(url, params=params)

    data = response.json()

    return data


# In[ ]:


from langchain_core.tools import Tool

flight_tool = Tool(
    name="Flight Search Tool",
    func=lambda x: search_flights(*x.split(",")),
    description="Search flights by source and destination"
)

hotel_tool = Tool(
    name="Hotel Recommendation Tool",
    func=recommend_hotels,
    description="Recommend hotels by city"
)

places_tool = Tool(
    name="Places Discovery Tool",
    func=discover_places,
    description="Discover tourist attractions by place type"
)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




