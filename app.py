import streamlit as st
import requests
import datetime

'''
# TaxiFareModel
'''

url = 'https://taxifare.lewagon.ai/predict'

min_date = datetime.datetime(1970,1,1)
max_date = datetime.datetime(2100,1,1)

col1, col2 = st.columns(2)
date = col1.date_input("Pickup date", min_value=min_date, max_value=max_date)
time = col2.time_input('Time')

col3, col4= st.columns(2)
pickup_longitude = col3.number_input("Pickup longitude", 40.7614327)
pickup_latitude = col4.number_input("Pickup latitude", -73.9798156)

col5, col6= st.columns(2)
dropoff_longitude = col5.number_input("Dropoff longitude", 40.6513111)
dropoff_latitude = col6.number_input("Dropoff latitude", -73.8803331)

passengers = st.selectbox('Number of passengers', range(1,9,1))

#token = 'pk.eyJ1IjoibGF1LWZzdCIsImEiOiJjbDBzN28wZWMwYWpvM2RxcGRzajNsZmxpIn0.ogWeSPmHFiTBtRznHx22xA'
#data = pd.DataFrame({'lat' : [pickup_latitude, dropoff_latitude], 'lon' : [pickup_longitude, dropoff_longitude]})
#st.map(data, zoom=9)

params = {'pickup_datetime' : f'{date} {time}', 'pickup_longitude' : pickup_longitude , 'pickup_latitude' : pickup_latitude , 'dropoff_longitude' : dropoff_longitude, 'dropoff_latitude' : dropoff_latitude,'passenger_count' : passengers}
url_ = f"{url}?pickup_datetime={params['pickup_datetime']}&pickup_longitude={params['pickup_longitude']}&pickup_latitude={params['pickup_latitude']}&dropoff_longitude={params['dropoff_longitude']}&dropoff_latitude={params['dropoff_latitude']}&passenger_count={params['passenger_count']}"

response = requests.get(url_)
fare = round(response.json()['fare'],2)

st.markdown(f""" ### Fare Amount : {fare}""")
