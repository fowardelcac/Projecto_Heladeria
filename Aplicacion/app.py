import streamlit as st
import pandas as pd
from pag import Inicio, Historico, Semanal
from streamlit_option_menu import option_menu

@st.cache_data
def load_data():
    url = "https://github.com/fowardelcac/Projecto_Heladeria/raw/main/VentasTabla.xlsx"
    df = pd.read_excel(url)
    df.dropna(inplace=True)
    df = df.drop(['Unnamed: 0'], axis=1) 
    return df
with st.sidebar:
    selected = option_menu("Menu principal", 
                           ['Inicio', 'Historicos', 'Semanal'],
                           icons=['house', 'arrow-return-right', 'arrow-return-right'], menu_icon="cast"
                           )

df = load_data()

if selected == 'Inicio':
    Inicio.mostrar_inicio()
elif selected == 'Historicos':
    Historico.info_mensual(df)
elif selected == 'Semanal':
    Semanal.info_sem(df)
