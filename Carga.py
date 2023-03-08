import streamlit as st 
import pandas as pd
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Menu principal", 
                           ['Carga', 'Ver'],
                           icons=['house', 'arrow-return-right'])
                           

def carga():
    if 'df' is not st.session_state:
        st.session_state.df = pd.DataFrame()
        uploaded_file = st.file_uploader("Elegir archivo!")
        df = pd.read_excel(uploaded_file)
        df.dropna(inplace=True)
        df = df.drop(['Unnamed: 0'], axis=1) 
        
        
if selected == 'Carga':
    carga()
if selected == 'Ver':
    st.session_state['df']

    
    