import streamlit as st
import pandas as pd

st.title("Agricultural Production Dashboard")

DATA_URL = "ml_livestock_and_milk.csv"

def load_data():
    data = pd.read_csv(DATA_URL)
    return data

data_load_state = st.text("Loading data...")

data = load_data()

data_load_state.text("Loading data... Done!")

st.subheader("Raw Dataset")

st.write(data)