
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import pytz
import requests

st.title('Taxi Fare Calculator')
nyc_datetime_now = datetime.now(pytz.timezone('Asia/Tokyo'))
d = st.date_input("Pickup date", datetime.date(nyc_datetime_now))
t = st.time_input('Pickup time', datetime.time(nyc_datetime_now))

pickup_datetime = datetime.combine(d, t).strftime("%Y-%m-%d %H:%M:%S")
pickup_longitude = st.text_input("Pickup longitude")
pickup_latitude = st.text_input("Pickup latitude")
dropoff_longitude = st.text_input("Dropoff longitude")
dropoff_latitude = st.text_input("Dropoff latitude")
passenger_count = st.slider('Number of passengers', 1, 5, 2)
button = st.button('submit')



url = 'https://taxifare.lewagon.ai/predict'

params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

if button:
    response = requests.get(url=url, params=params).json()
    if 'prediction' in response:
        prediction = round(response['prediction'], 2)
        st.write(f"**This trip costs {prediction} €**")
    else:
        st.write("Please enter the information")
else:
    st.write('Please enter the information and submit 😃')
