import pandas as pd
import streamlit as st
import datetime
import matplotlib.pyplot as ptl
import numpy as np
titanic_link = 'titanic.csv'

titanic_data = pd.read_csv(titanic_link)

st.title('Titanic Data')
sidebar = st.sidebar
sidebar.image("credencial.jpeg", use_container_width=True)  # Reemplaza con la ruta de tu imagen

today = datetime.date.today()
today_date = sidebar.date_input('Current date', today)

#Checkbox to show the dataset overview
st.success('Current date: %s' % str(today_date))
    
# agree = st.checkbox('Show dataset Overview')
# if agree:
#     st.dataframe(titanic_data)
    
# fig, ax = ptl.subplots()
# ax.hist(titanic_data['age'].dropna(), bins=30, edgecolor='k')
# st.pyplot(fig)
# ax.hist

#Checkbox 
#Display the dataset if the user select the checkbox
agree = sidebar.checkbox('Show dataset Overview')
if agree:
    st.dataframe(titanic_data)

#Radio
#Select the emabark townn of the passenger and display the data with this selection
selected_town = st.radio("Select the embark town",
                            titanic_data['embark_town'].unique())
st.write('Select embark town:', selected_town)

st.write(titanic_data.query(f"""embark_town ==@selected_town"""))
st.markdown('_')

# SLIDER 
# Select a range of the fare and then display the dataset 
optionals = st.expander("optionals Configurations", True)
fare_min = optionals.slider(
    "Minimum fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max()),
)

fare_max = optionals.slider(
    "Maximum fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max()),
)

subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) & (fare_min <= titanic_data['fare'])]

#Display of the dataset
st.dataframe(subset_fare)


#GRAPHS
fig, ax = ptl.subplots()
ax.hist(titanic_data.fare)
st.header("Histograma del titanic")
st.pyplot(fig)


#Second graph
fig2, ax2 = ptl.subplots()
y_pos = titanic_data['class']
x_pos = titanic_data['fare']

ax2.barh(y_pos, x_pos)
ax2.set_ylabel('Class')
ax2.set_xlabel('Fare')
ax2.set_title('¿Cuanto pagaron las clases del Titanic?')

st.header ("Grafica de barras del titanic")
st.pyplot(fig2)


#Third graph
fig3, ax3 = ptl.subplots()  

ax3.scatter(titanic_data.age, titanic_data.fare)
ax3.set_xlabel('Age')
ax3.set_ylabel('Fare')

st.header("Grafica de dispersion del titanic")
st.pyplot(fig3)

#Maps
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)