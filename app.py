import streamlit as st
import requests
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import pytz
import base64

page_bg_img = '''
<style>
body {
background-image: url("https://w0.peakpx.com/wallpaper/613/605/HD-wallpaper-thoughts-i-had-while-rewatching-the-twilight-saga-new-moon-cute-twilight.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)



'''
Welcome to the New York Taxi fare estimator
'''

st.markdown('''
            The desgin is very human.
''')
current_dateTime = datetime.now()
lagos = pytz.timezone('Africa/Lagos')
lagos_time = lagos.localize(current_dateTime)


seconds = st.number_input('In how many seconds from now would you like to leave?')

pickup_time = lagos_time+timedelta(seconds=seconds)

st.write('That brings you to around ', pickup_time, ' (Lagos, Africa local Datetime)')

def get_map_data(pick_lat, pick_long, drop_lat, drop_long):

    return pd.DataFrame(
            [[pick_lat, pick_long],
            [drop_lat, drop_long]],
            columns=['lat', 'lon']
        )

pick_lat = st.slider('Select pickup latitude', min_value=40.530610, max_value=40.890610, step=0.00001)
pick_long = st.slider('Select pickup longitude', min_value=-74.155242, max_value=-73.655242, step=0.00001)
drop_lat = st.slider('Select dropoff latitude', min_value=40.530610, max_value=40.890610, step=0.00001)
drop_long = st.slider('Select dropoff longitude', min_value=-74.155242, max_value=-73.655242, step=0.00001)


df = get_map_data(pick_lat, pick_long, drop_lat, drop_long)

st.map(df)

passenger = 0

if st.checkbox('+1 passenger'):
    passenger += 1
    if st.checkbox('+1 more passenger'):
        passenger +=1
        if st.checkbox('+1 passenger again'):
            passenger += 1
            if st.checkbox('+1 passenger - someone has to call shotgun'):
                passenger += 1
                if st.checkbox('+1 passenger - getting crowded in here'):
                    passenger += 1
                    if st.checkbox('+1 passenger - I mean just take the bus at some point'):
                        passenger += 1
                        if st.checkbox('+1 passenger - is it me or is it hard to breathe in here'):
                            passenger += 1
                            if st.checkbox('+1 passenger - you know what I can walk'):
                                passenger += 1

st.write(f'{passenger} people in the car')

pickup_date_formatted = pickup_time.strftime("%Y-%m-%d")
pickup_time_formatted = pickup_time.strftime("%H:%M:%S")

url = 'https://taxifareimage-bzkivu3rca-ew.a.run.app/predict'

request = requests.get(f'{url}?pickup_datetime={pickup_date_formatted}%20{pickup_time_formatted}&pickup_longitude={pick_long}&pickup_latitude={pick_lat}&dropoff_longitude={drop_long}&dropoff_latitude={drop_lat}&passenger_count={passenger}')
fare = request.json()
fare = fare['fare']

color = st.color_picker("Select the CornFlowerBlue color to submit", "#00f900")

if color == '#6495ed':
    request = requests.get(f'{url}?pickup_datetime={pickup_date_formatted}%20{pickup_time_formatted}&pickup_longitude={pick_long}&pickup_latitude={pick_lat}&dropoff_longitude={drop_long}&dropoff_latitude={drop_lat}&passenger_count={passenger}')
    fare = request.json()
    fare = fare['fare']
    st.markdown(f'''
                THIS WILL BE A GRAND TOTAL OF {fare} USD - tips not included - cash or cocaine
    ''')
    st.audio(data='https://www.nyan.cat/music/original.mp3', format="audio/mp3", loop=True, autoplay=True)

else:
    st.markdown(f'''
                (this is not CornFlowerBlue)
    ''')
