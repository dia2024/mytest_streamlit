import streamlit as st
import pandas as pd
from folium.plugins import HeatMap
import folium
bc = pd.read_csv('bucheon.csv')
centerx = bc['위도'].mean()
centery = bc['경도'].mean()
m = folium.Map(location=[centerx,centery], zoom_start=15)
HeatMap(data=bc[['위도','경도']], radius=20).add_to(m)
st.write(m)
