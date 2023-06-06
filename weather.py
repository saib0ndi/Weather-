# api key
api_key = "4eefa0aab55ffad0ced3008846d3681f"

# Modules
import streamlit as st
import requests
from datetime import datetime , timedelta
import pandas as pd
import matplotlib.pyplot as plt
import time 

# Function for LATEST WEATHER DATA
def getweather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    result = requests.get(complete_url)     
    x = result.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
    
        return current_temperature,current_pressure,current_humidity,weather_description,x["coord"]["lat"],x["coord"]["lon"]
        
    else:
        print("error in search !")

# Let's write the Application

st.header('Streamlit Weather Report')   

city_name = st.text_input("Enter a city name")

if city_name:
    res = getweather(city_name)
    if res:
        st.success('Current Temperature: ' + str(round(res[0],2)))
        st.info('Current Pressure: ' + str(round(res[1],2)))
        st.warning('Current Humidity: ' + str(round(res[2],2)))
        st.error('Weather Description: ' + str(res[3]))
        st.warning('Latitude: ' + str(res[4]))
        st.error('Longitude:' + str(res[5]))