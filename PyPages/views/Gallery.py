import streamlit as st 
from PIL import Image

st.markdown(""" <h2 style='text-align:center;color:white;'>Gallery</h2>""",unsafe_allow_html=True)

st.write("-")
col1, col2, col3 = st.columns([1,1,1])

img1=Image.open("views/Img/img1.jpg")
col1.image(img1)

img2=Image.open("views/Img/img2.jpg")
col2.image(img2)

img3=Image.open("views/Img/img3.jpg")
col3.image(img3)

col11, col22, col33 = st.columns([1,1,1])
img11=Image.open("views/Img/img4.jpg")
col11.image(img11)

img22=Image.open("views/Img/img5.jpg")
col22.image(img22)

img33=Image.open("views/Img/img6.jpg")
col33.image(img33)

