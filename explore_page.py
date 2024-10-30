import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt


def show_explore_page():
    st.title("Visualiztion Plots using streamlit")

    df = pd.read_csv("preprocessed_data.csv")


    st.header("Preprocessed Dataset")
    st.dataframe(df)
    st.write("----")

    # charts using pyplot Function

    st.subheader("Visualizing Rooms Number")
    fig = plt.figure()
    df["Rooms"].value_counts().plot(kind = "bar")
    st.pyplot(fig)

    st.write("----")

    st.subheader("Visualizing Bathrooms Number")
    fig1 = plt.figure()
    df["Bathrooms"].value_counts().plot(kind = "kde")
    st.pyplot(fig1)

    st.write("----")

    st.subheader("Viewing The Furnishing column")
    fig2 = plt.figure()
    sns.countplot(df["Furnishing"])
    st.pyplot(fig2)

    st.write("---")

    st.subheader("Explore Chosen column with each others:")
    list = df.columns.tolist()
    choice = st.multiselect("Choose columns", list, default = "Price")

    data = df[choice]
    st.line_chart(data)

    st.write("----")

    st.area_chart(data)
