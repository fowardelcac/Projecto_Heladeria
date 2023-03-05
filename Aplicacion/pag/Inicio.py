import streamlit as st
import pandas as pd

def mostrar_inicio():
    
    """
    Muestra la página de inicio de la aplicación.
    """
    st.title("Heladeria Chuii :icecream:")
    st.header("Bienvenido")
    st.markdown('''Esta es una aplicación desarrollada para visualizar de manera rápida y sencilla 
  un análisis rápido del negocio.  Cuenta con dos pestañas: ''')
    st.markdown('''
                - Inicio
                - Historico.
                - Semanal.
        ''')
    st.header('Inicio. :sparkles:')
    st.markdown(''' Esta es la pestalla principal, donde cuenta con una breve introduccion y aqui sera donde debe cargar sus datos actualizados
                ''')
                
    st.header('Historico. :date:')
    st.markdown('''En esta pestaña se podrá visualizar de manera rápida una hoja de cálculo con la cantidad 
            de helado vendido, existe la opción de ingresar determinado mes y recibir una hoja de cálculo 
            con las ventas ordenadas de mayor a menor, incluso ver distintos gráficos.''')
    st.header('Semanal. :calendar:')
    st.markdown('''En esta pestaña se podrá visualizar a través de una hoja de cálculo las ventas semanales
            ordenadas de manera descendente.''')
            


