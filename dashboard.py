import streamlit as st
import pandas as pd
import numpy as np

st.title("Livestock and Raw Milk Dashboard")

DATA_URL = (
    'https://raw.githubusercontent.com/'
    'fundaBa/ca2-dashboard/main/FAOSTAT_livestock_and_milk.csv'
)

def load_data():
    data = pd.read_csv(DATA_URL)
    return data

data = load_data()

st.subheader("Livestock and Milk Dataset")

st.write(data)

st.subheader("Dataset Information")

st.write(f"Number of Records: {data.shape[0]}")
st.write(f"Number of Variables: {data.shape[1]}")
st.write(f"Countries Included: {data['Area'].nunique()}")