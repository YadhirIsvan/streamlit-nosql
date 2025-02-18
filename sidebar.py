import streamlit as st

st.title("App side bar")

sidebar = st.sidebar

sidebar.title("mi barra lateral")
sidebar.text("menu")
option = st.sidebar.selectbox('Selecciona una opción', ['Opción 1', 'Opción 2', 'Opción 3'])
st.write(f'Has seleccionado: {option}')
sidebar.write("texto en barra lateral")

st.write("texto en la parte principal")

sexo = st.checkbox("eres gay")
if sexo:
    st.write("si eres gay")
