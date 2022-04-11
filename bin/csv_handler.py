# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:07:47 2022

@author: Marina, Martin
"""

import glob
import pandas as pd
import os
from utils import clean_string

out_path = '../../CSV_FINAL.csv'


def read_csv(names):
    # Devuelve los ficheros csv
    # Cambiamos el directorio para acceder a los csv creados
    a = os.getcwd()
    os.chdir(a + '/data/')
    # Especificamos un patrón de los csv
    dfs = []
    for n in names:
        print("Leyendo " + n + '.csv')
        df = pd.read_csv(n + '.csv', index_col=None)

        print("  Limpiando datos")
        for col in df:
            df[col] = df[col].apply(clean_string)
        df.columns = df.columns.to_series().apply(clean_string)
        dfs.append(df)
    return dfs


def merge_csvs(dfs):
    print("Merging Dataframes")
    df_master = dfs[0]
    df_master = df_master.rename(columns={df_master.columns[0]: 'Country'})
    for i in range(1, len(dfs)):
        df = dfs[i]
        df.rename(columns={df_master.columns[0]: 'Country'})
        df_master = df_master.merge(df, on=['Country'])
    print("Writing file to " + out_path)
    df_master.to_csv(out_path, index=False)
    return df_master
