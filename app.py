import streamlit as st
import datetime
import requests


'''
# Burak's TaxiFareModel StreamLit Website
'''
st.image(
    'https://media.istockphoto.com/vectors/taxi-car-vector-id1161667429?k=20&m=1161667429&s=612x612&w=0&h=wRxiIAMdxqggCCybbJYlPk-oSQPzXEWqHvGGk47hzJ0=',
    width=400
)

st.markdown('''
Welcome to my first trial to create a simple Streamlit website
''')

date = st.date_input('When do you need a taxi?')
time = st.time_input('At what time do you need a cab?')
date_time = datetime.datetime.combine(date, time).strftime("%Y-%m-%d %H:%M:%S")
passenger_count = st.number_input('How many passengers do you have?',
                                  min_value=1)

'''
Placeholder for Lat/Lon info, later better to connect it to map API
Better to add a map / visual similar to Le Wagon's page
'''
lon1 = st.number_input('pickup longitude', format='%.6f')
lat1 = st.number_input('pickup latitude', format='%.6f')
lon2 = st.number_input('dropoff longitude',format='%.6f')
lat2 = st.number_input('dropoff latitude', format='%.6f')

base_url = 'https://taxifare.lewagon.ai/predict'
params = {'pickup_datetime': date_time,
          'pickup_longitude': lon1,
          'pickup_latitude': lat1,
          'dropoff_longitude': lon2,
          'dropoff_latitude': lat2,
          'passenger_count': int(passenger_count)}

response = requests.get(url=base_url, params=params).json()

st.write(f"## Your predicted fare is ${response['fare']:.2f}")
