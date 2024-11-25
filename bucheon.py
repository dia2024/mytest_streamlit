import streamlit as st
import pandas as pd

# from folium.plugins import HeatMap
# import folium
bc = pd.read_csv('bucheon.csv')
st.title('부천시 편의점 위치')
st.dataframe(bc)
temp=bc['color'].value_counts().plot(kind='bar')
st.pyplot(temp)
