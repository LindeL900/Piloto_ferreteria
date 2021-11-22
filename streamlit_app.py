# -*- coding: utf-8 -*-
#Pandas Piloto analisis ventas de un mes - leer resultado carga ya depurado

import streamlit as st
st.write('Pagina web ejemplo') 
c1, c2 = st.columns([3, 7])
c1.markdown("## Testo columna 1")
#c1.image('images/avatar.jpeg', width=300)
# Contenido de la segunda
c2.markdown("## texto segunda columna")
c2.checkbox("Un Checkbox")
c2.select_slider("Slider de Texto", options=["uno", "dos", "tres", "cuatro"])



