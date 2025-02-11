import pandas as pd
import streamlit as st

name_link= 'dataset.csv'

name_data = pd.read_csv(name_link)
st.header('inicio')
st.title('name dataset')
st.dataframe(name_data)