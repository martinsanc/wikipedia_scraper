# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:07:47 2022

@author: Marina
"""

import glob
import pandas as pd


# Especificamos un patrón de los csv
files = glob.glob('*.csv')
# Mostrar el archivo csv_files, el cual es una lista de nombres
# joining files with concat and read_csv

for i in range(len(files)-1):
    #nfiles = i.replace('*.csv','')
    df = pd.read_csv(files[0], index_col=None)
    df.merge(pd.read_csv(files[i], index_col=None), how='outer')
    print(df)

df.to_csv('CSV_Final.csv')
