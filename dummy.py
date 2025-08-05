import streamlit as st 
import numpy as np 
import pandas as pd

st.title("Dummy Project")
st.subheader("Project")

st.markdown("""
            Welcome to Data Science""")

selected_country = st.selectbox(
    "Select any values",

    ["India","Russia"]
)

st.write(selected_country)
