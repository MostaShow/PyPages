import streamlit as st 
import json
import requests
from streamlit_lottie import st_lottie

st.markdown(""" <h2 style='text-align:center;color:white;'>Welcome to my app !</h2>""",unsafe_allow_html=True)

#st.title("Home Page")
#st.write("---")

def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)

#---- Load assets ----
lottie_coding = load_lottiefile("coding.json")
st_lottie(lottie_coding,height=350,width=500,key=None)