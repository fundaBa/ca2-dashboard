import streamlit as st
import pandas as pd
import numpy as np

st.title("Agricultural Production Dashboard")

DATA_URL = ('https://raw.githubusercontent.com/'
    'fundaBa/ca2-dashboard/main/FAOSTAT_livestock_and_milk.csv'
)


def load_data():
    data = pd.read_csv(DATA_URL)
    return data

data_load_state = st.text("Loading Data...")

data = load_data()

data_load_state.text("Loading Data...Done!")

st.subheader("Raw Data")

st.write(data)
