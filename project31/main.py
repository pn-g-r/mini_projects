import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium

st.set_page_config(layout='wide')
st.title('Earthquake Global Map')
df = pd.read_csv('earthquakes_yesterday.csv')

mean_lat = df['Latitude'].mean()
mean_lon = df['Longitude'].mean()

m = folium.Map(location=[mean_lat, mean_lon], zoom_start=2)


for i, row in df.iterrows():
    lat = row['Latitude']
    lon = row['Longitude']
    folium.CircleMarker(
        location=[lat, lon], 
        radius=row['Magnitude'] * 2,
        color='crimson',
        fill=True,
        fill_color='crimson',
        tooltip=f"Loc: {row['Location']} Mag: {row['Magnitude']}"                
                    ).add_to(m)
# To save it as an html file
# m.save('project31/map.html')

st_folium(m, width=1400)