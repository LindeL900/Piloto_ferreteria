# -*- coding: utf-8 -*-
#Pandas Piloto analisis ventas de un mes - leer resultado carga ya depurado

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
#import matplotlib.pyplot as plt
st.header ("Ejercicio cursos streamlit")
name = "Linde"
st.text("Ejercicio de: {}".format (name))
#st.write('Pagina web mostrar graficos') 
c1, c2 = st.columns([3, 7])
#c1.markdown("## Parametros del grafico")
#c1.image('images/avatar.jpeg', width=300)
# Contenido de la segunda
#c2.markdown("## texto segunda columna")
#c2.checkbox("Un Checkbox")
#c2.select_slider("Slider de Texto", options=["uno", "dos", "tres", "cuatro"])
#c3.radio("Radio", options=["AM", "FM", "Online"])
c1.selectbox("Graficos a generar:", options=["Grafico x dia", "Grafico por cliente"])
c2.multiselect("Tipo documento", options=["FCV", "BLV", "NCV"])
datos = np.randon.rand(20,2)
df = pd.dataframe(datos, columns = ['dia','valor']
