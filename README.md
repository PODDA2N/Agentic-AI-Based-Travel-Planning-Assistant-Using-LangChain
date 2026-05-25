# Agentic-AI-Based-Travel-Planning-Assistant-Using-LangChain

Project Overview

The Agentic AI-Based Travel Planning Assistant is an intelligent AI-powered travel recommendation and itinerary generation system developed using Python, LangChain, FastAPI, OpenAI, and real-time APIs. The project is designed to automate the complete travel planning process using Agentic AI architecture and multi-step reasoning capabilities.

The system autonomously analyzes user travel requirements such as destination, duration, budget, and travel preferences, then dynamically selects appropriate tools to generate optimized travel itineraries including flights, hotels, tourist attractions, weather forecasts, and budget estimations.

The project demonstrates how LangChain agents can perform intelligent tool-calling, reasoning, and decision-making to solve real-world travel planning problems.

Objectives
Primary Objectives
Build an Agentic AI system using LangChain that autonomously creates travel itineraries.
Integrate multiple travel planning tools and APIs.
Enable multi-step reasoning and intelligent decision-making using ReAct or ToolCalling agents.
Generate structured and personalized travel plans.
Integrated Tools

The project integrates the following tools:

Flight Search Tool
Uses flights.json
Searches flights based on source and destination
Recommends cheapest or fastest flights
Hotel Recommendation Tool
Uses hotels.json
Recommends hotels based on:
city
price
ratings
Places Discovery Tool
Uses places.json
Suggests tourist attractions and points of interest
Weather Lookup Tool
Integrates Open-Meteo API
Provides real-time weather forecasts
Budget Estimation Tool
Calculates:
flight cost
hotel expenses
local travel & food expenses
Secondary Objectives
Implement filtering and ranking logic
Optimize travel recommendations
Justify AI decisions and recommendations
Provide outputs in:
structured JSON format
human-readable format
Build a simple user interface using:
CLI
Streamlit

Project Approach
Step 1 — Data Setup

The project uses JSON-based datasets stored inside the data/ folder.

Flight Dataset

Contains flight information including:

flight ID
airline name
departure city
destination city
departure time
arrival time
price

Hotel Dataset

Contains hotel-related details:

hotel ID
hotel name
city
star rating
price per night
amenities

Tourist Places Dataset

Contains tourist attraction information:

place ID
attraction name
place type
ratings

Step 2 — Build LangChain Tools

The system creates multiple LangChain tools for autonomous travel planning.

Flight Search Tool
Responsibilities
Read flights.json
Filter flights by source and destination
Recommend cheapest or fastest flight
Hotel Recommendation Tool
Responsibilities
Read hotels.json
Filter hotels by:
city
ratings
price range
Places Discovery Tool
Responsibilities
Read places.json
Recommend attractions based on:
type
ratings
Weather Lookup Tool
Responsibilities
Call Open-Meteo API
Retrieve travel weather forecasts
Budget Estimation Tool
Responsibilities

Calculate total travel expenses including:

flight price
hotel expenses
local food and transportation costs

Budget Formula:

Total Budget=Flight Cost+(Hotel Price Per Night×Days)+(1000×Days)

Step 3 — Create the Agent

The project uses a LangChain ReAct or OpenAI ToolCalling agent.

Agent Responsibilities

The AI agent can:

understand user travel requests
select appropriate tools dynamically
retrieve travel information
analyze travel data
generate optimized itineraries
estimate budgets
provide final structured responses
