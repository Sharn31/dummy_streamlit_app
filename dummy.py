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

st.image("https://images.pexels.com/photos/1183099/pexels-photo-1183099.jpeg?_gl=1*ey46ll*_ga*MTI2MDQ2MTM1NS4xNzQ2MDc5Mjc2*_ga_8JE65Q40S6*czE3NTQzNjc2NTUkbzIkZzEkdDE3NTQzNjc2NzAkajQ1JGwwJGgw")
