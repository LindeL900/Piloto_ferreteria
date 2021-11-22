# -*- coding: utf-8 -*-

"""
#Created on Thu Oct  7 12:05:25 2021
@author: Linde
"""

#Pandas Piloto analisis ventas de un mes - leer resultado carga ya depurado

import pandas as pd
import numpy as np

#%% 1 lee acumulado y genera df mes de analisis
#desde la posicion del programa hay que colocar los subdirectorios
df_acu = pd.read_csv("C:/Users/Linde/.spyder-py3/Proyecto Piloto/DF_ACU.csv", encoding = "latin-1", sep = ";")
df = df_acu.loc[df_acu["mes"].isin([8])]
print ("valores mes a analizar")
pivot = df.pivot_table(index = "mes", values = "valor_item",
                          aggfunc = { np.sum,np.min, np.max,np.mean})
print (pivot)


