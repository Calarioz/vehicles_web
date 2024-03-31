import pandas as pd
import plotly.express as px
import streamlit as st

def create_bar(car_type:str): #Función para imprimir la cantidad de vehiculos por tipo de color
        st.subheader(f"Gráfica de coches anunciados del tipo: {car_type}")
        type_selector = df_total_models[df_total_models["type"]==car_type]
        fig = px.bar(type_selector,
            x="Color_de_pintura",
            y="Total",
        )
        st.plotly_chart(fig,use_container_width=True)

car_data = pd.read_csv("vehicles_us.csv")   #Leer datos

df_total_models = car_data.groupby(by=["type","paint_color"]).count().reset_index() #Agrupamos el df por tipo y color de pintura para el gráfico de barra
df_total_models["type"] = df_total_models["type"].str.upper() #Normalizamos nombres
df_total_models.rename(columns={"price":"Total"},inplace=True) #Cambiamos nombre de la columna
df_total_models.rename(columns={"paint_color":"Color_de_pintura"},inplace=True)

unique_types = car_data["type"].str.upper().unique() #Lista de tipos de coche

st.header("Anuncios de venta de coches")

hist_checkbox = st.checkbox('Construir histograma') #Crear un check box

if hist_checkbox: # al hacer clic en el botón
    # escribir un mensaje
    st.subheader('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histogramacd Desktop/DC_Course/
    fig1 = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)

scatter_checkbox = st.checkbox("Construir diagrama de dispersion") #Crear un check box

if scatter_checkbox: # al hacer clic en el botón
    df_monthly_price_mean = car_data.groupby(by="type")["price"].mean().reset_index()

    # escribir un mensaje
    st.subheader("**Precio promedio de coches de acuerdo al tipo de vehiculo**")

    # Crear un diagrama de dispersión
    fig2 = px.scatter(df_monthly_price_mean,x="type",y="price")

    # mostrar un gráfico Ploty interactivo
    st.plotly_chart(fig2,use_container_width=True)


bar_selectb = st.selectbox( #Crear un select box
    label = "**Selecciona el tipo de vehiculo**", 
    options = unique_types,
    index = 0
)
if bar_selectb == unique_types[0]:
    create_bar(unique_types[0])

if bar_selectb == unique_types[1]:
    create_bar(unique_types[1])

if bar_selectb == unique_types[2]:
    create_bar(unique_types[2])

if bar_selectb == unique_types[3]:
    create_bar(unique_types[3])

if bar_selectb == unique_types[4]:
    create_bar(unique_types[4])

if bar_selectb == unique_types[5]:
    create_bar(unique_types[5])

if bar_selectb == unique_types[6]:
    create_bar(unique_types[6])

if bar_selectb == unique_types[7]:
    create_bar(unique_types[7])

if bar_selectb == unique_types[8]:
    create_bar(unique_types[8])

if bar_selectb == unique_types[9]:
    create_bar(unique_types[9])

if bar_selectb == unique_types[10]:
    create_bar(unique_types[10])

if bar_selectb == unique_types[11]:
    create_bar(unique_types[11])

if bar_selectb == unique_types[12]:
    create_bar(unique_types[12])



        