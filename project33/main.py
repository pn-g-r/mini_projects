import folium
from folium.plugins import MarkerCluster
 
import streamlit as st
from streamlit_folium import st_folium
 
import pandas as pd
 
st.set_page_config(layout="wide")
 
# Load the CSV file containing accident data
data = pd.read_csv("accidents.csv", sep=';', encoding='unicode_escape')
 
# Create a Folium map centered around US
m = folium.Map(location=[34, -86], zoom_start=4)
 
# Create a MarkerCluster object
marker_cluster = MarkerCluster().add_to(m)
 
# Add markers to the MarkerCluster
for i, row in data.iterrows():
    folium.CircleMarker(
        location=[row["LATITUDE"], row["LONGITUD"]],
        tooltip=row["MAN_COLLNAME"],
    ).add_to(marker_cluster)

 
# Render the map in the Streamlit app
# st_folium(m, width=1400)

# Render the map in the html file
m.save('map.html')