import streamlit as st
import pandas as pd
import numpy as np

st.title("Livestock and Raw Milk Dashboard")

DATA_URL = (
    'https://raw.githubusercontent.com/'
    'fundaBa/ca2-dashboard/main/ml_livestock_and_milk.csv'
)

def load_data():
    data = pd.read_csv(DATA_URL)
    return data

data = load_data()

st.subheader("Livestock and Milk Dataset")

st.write(data)

st.markdown("""
### Dataset Overview

This dashboard presents livestock population and milk production data from selected European countries.
The dataset includes information on cattle, goats, sheep, cattle milk production, goat milk production, and sheep milk production collected over multiple years.

The dashboard allows users to explore production trends, relationships between variables, and machine learning results generated during the analysis.
""")

st.markdown("### Dataset Information")

st.write(f"Number of Records: {data.shape[0]}")
st.write(f"Number of Variables: {data.shape[1]}")
st.write(f"Countries Included: {data['Area'].nunique()}")

st.markdown("### Country Filter")

selected_country = st.selectbox(
    "Select a Country",
    sorted(data["Area"].unique())
)

filtered_data = data[data["Area"] == selected_country]

st.write(filtered_data)

import matplotlib.pyplot as plt

st.markdown("### Cattle Stock and Milk Production Trend")

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    filtered_data["Year"],
    filtered_data["Cattle"],
    marker="o",
    label="Cattle Stock"
)

ax.plot(
    filtered_data["Year"],
    filtered_data["Raw milk of cattle"],
    marker="o",
    label="Cattle Milk Production"
)

ax.set_xlabel("Year")
ax.set_ylabel("Value")
ax.set_title(f"Cattle Stock and Milk Production in {selected_country}")

ax.legend()

st.pyplot(fig)