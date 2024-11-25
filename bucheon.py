import streamlit as st
import pandas as pd

# from folium.plugins import HeatMap
# import folium
bc = pd.read_csv('bucheon.csv')
st.title('부천시 편의점 위치')
st.dataframe(bc)

import matplotlib.pyplot as plt

temp=bc['color'].value_counts()
fig= plt.figure(figsize=(7,5))
plt.bar(x=temp.index, height=temp.values)
plt.xticks(temp.index, ['GS', 'CU', 'Seven', 'Emart'])
st.pyplot(fig)
