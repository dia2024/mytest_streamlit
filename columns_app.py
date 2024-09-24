import streamlit as st
from PIL import Image

st.title('화면분할 사용예')

# 1) 2개로 세로단 분할
[col1, col2]= st.columns(2)
with col1:
    st.subheader('youtube video1')
    url_col1='https://youtu.be/ixnaXXsLHcI?si=YTlwe25tq6VqiSGv'
    st.video(url_col1)

with col2:
    st.subheader('youtube video2')
    url_col2 = 'https://www.youtube.com/watch?v=otImuTAybrI'
    st.video(url_col2)

#3개로 세로단 분할
columns = st.columns([1.1, 1.0, 0.9])
image_files = ['boy.png', 'fever.png', 'user.png']
image_captions =['아이', '열병', '사용자']

for k in range(len(columns)):
    with columns[k]:
        st.subheader(image_captions[k])
        image_local = Image.open(image_files[k])
        st.image(image_local, caption=image_captions[k])
