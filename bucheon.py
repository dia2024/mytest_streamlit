import streamlit as st

import pandas as pd
# from folium.plugins import HeatMap
# import folium
bc = pd.read_csv('bucheon.csv')
st.title('부천시 편의점 위치')
st.dataframe(bc)

import folium
from streamlit_folium import st_folium
centerx = bc['위도'].mean()
centery = bc['경도'].mean()
# center on Liberty Bell, add marker
m = folium.Map(location=[centerx, centery], zoom_start=16)
for name, lat, long, c in zip(bc['상호명'], bc['위도'], bc['경도'], bc['color']):
    folium.Marker([lat, long], popup=name,
              icon=folium.Icon(color=c)).add_to(m)

# call to render Folium map in Streamlit
# st_data = st_folium(m, width=725)

st_folium(m, width=725)
