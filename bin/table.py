# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 23:10:12 2022

@author: Marina, Martin
"""

from utils import *

import os
import pandas as pd
from selenium.common.exceptions import *


class Table:
    # Objeto tabla, al inicializar scrapea y carga la tabla.
    driver = None
    url = None
    xpath = None
    df = None

    def __init__(self, driver, url, xpath):
        self.driver = driver
        self.xpath = xpath

        self.driver.driver.get(url)
        self.df = self.read_data()

    def read_data(self):
        # Lee los datos de la tabla
        headers = self.read_headers()
        data = []
        flag = True
        i=1
        count=0
        while flag:
            dict = {}
            try:
                for j in range(len(headers)):
                    cell = self.driver.driver.find_element_by_xpath(self.xpath + "tbody/tr[" + str(i) + "]/td[" + str(j+1) + "]")
                    dict[headers[j]] = clean_string(cell.text)
                if dict is not {}:
                    data.append(dict)
                    count = 0
                else:
                    count += 1
                    if count > 3:
                        # Termina de buscar cuando no encuentra información en 3 celdas consecutivas.
                        flag = False
            except:
                count += 1
                if count>3:
                    # Termina de buscar cuando no encuentra información en 3 celdas consecutivas.
                    flag = False
            finally:
                i += 1
        df = pd.DataFrame(data)
        return df

    def read_headers(self):
        # Lee los nombres del encabezado de la tabla
        headers = []
        flag = True
        i = 1
        while flag:
            try:
                header = self.driver.driver.find_element_by_xpath(self.xpath + "thead/tr/th[" + str(i) + "]")
                headers.append(clean_string(header.text))
                i += 1
            except:
                flag = False
        return headers

    def data2csv(self, nombre_csv):
        path = os.path.dirname(nombre_csv)
        if not os.path.exists(path):
            # Crea directorio si no existe
            os.makedirs(path)
        name_columns = list(self.df.columns.values)
        self.df.to_csv(nombre_csv, columns=name_columns, header=name_columns, index=False)