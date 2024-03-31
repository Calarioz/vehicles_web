import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("../vehicles_us.csv")   #Leer datos

st.header("Anuncios de venta de coches")

hist_button = st.button('Construir histograma') #Crear boton
scatter_checkbox = st.checkbox("Construir diagrama de dispersion")

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_checkbox: # al hacer clic en el botón
    # escribir un mensaje
    st.write("Creación de un diagrama de dispersión para el conjunto de datos de anuncios de ventas de coches")

    # Crear un diagrama de dispersión
    fig = px.scatter(car_data, x="model" ,y="cylinders")

    # mostrar un gráfico Ploty interactivo
    st.plotly_chart(fig,use_container_width=True)

        