import streamlit as st
from funciones import *

def info_sem(df):
    st.title("Semanales.")

    # creacion datasets
    df.set_index('Fecha', inplace=True)
    st.subheader("Helados mas vendidos de mayor a menor.")
    fecha = st.selectbox("Ingrese fecha: ", df.index)
    sem_ord = ventas_ordenadas_por_fecha(df, fecha)
    
    media = pd.DataFrame()
    media["Ventas medias"] = df.mean()    
    
    st.write(sem_ord)
    
    st.subheader("Venta media:")
    st.write(media)



