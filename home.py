import requests
import streamlit as st
from streamlit_lottie import st_lottie


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- load Asset ----
lottie_house = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_67nlyyap.json")
lottie_data = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_49rdyysj.json")
lottie_price = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_cdnc1ioz.json")

def show_home():
    st.header("Hi :wave:")
    st.header("Welcome to KLPropreites!")
    st.subheader("The easiest way to get your unit price. ")
    st.write("")
    with st.empty():
        left_column, middle_column, right_column = st.columns(3)
        with left_column:
            st_lottie(lottie_house, height=200, key="data")
        with middle_column:
            st_lottie(lottie_data, height=250, key="house")
        with right_column:
            st_lottie(lottie_price, height=250, key="coding")

    st.write("#### All you need is just enter unit data to get your accurate price.")
