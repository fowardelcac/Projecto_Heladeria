import streamlit as st
from funciones import *

def info_mensual(df):
    st.title("Historicos.")
    # Creacion datasets
    data_m = agrupar_ventas_mensuales(df)
    suma_filas = pd.DataFrame()
    suma_filas["Total"] = data_m.sum(axis=1)
    
    # Muestra
    st.title("Hojas de calculo: ")
    dicc = dict({
        'Ventas mensuales':data_m,
        'Ventas totales por mes': suma_filas
        })
    
    hoja = st.selectbox("Que tipo de hoja de calculo desea ver:",
                 dicc.keys()
                 )
    st.write(dicc[str(hoja)])
    
    st.title("Graficos.")
    
    st.subheader("Grafico de lineas. :chart_with_upwards_trend: ")
    st.markdown("Ingrese un gusto y podra ver como ha sido su comportamiento durante el tiempo.")
    sabor = st.selectbox("Ingrese sabor:", data_m.columns)
    st.line_chart(data_m[str(sabor)])
    
    st.subheader("Grafico de barras. :bar_chart:")
    st.markdown("Este grafico muestra las ventas mensuales de una manera mas comprensible.")
    st.bar_chart(suma_filas["Total"])    
    