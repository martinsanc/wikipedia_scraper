# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:07:47 2022

@author: Marina, Martin
"""

import glob
import pandas as pd
import os 

#Cambiamos el directorio para acceder a los csv creados
a = os.getcwd()
os.chdir(a +'/data/')

# Especificamos un patrón de los csv
files = glob.glob('*.csv')
# Mostrar el archivo csv_files, el cual es una lista de nombres
# joining files with concat and read_csv


df1 = pd.read_csv(files[0], index_col=None)

for i in range(1,len(files)):
    df2 = pd.read_csv(files[i], index_col=None)
    # Cambiamos el nombre de la columna que contiene los paises para unir los dataframes
    df2 = df2.rename(columns={df2.columns[0]:'Country'})
    df1 = df1.merge(df2, how='left', on='Country')
    print(df1.iloc[1])

df.to_csv('CSV_Final.csv')

