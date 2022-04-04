# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:41:42 2022

@author: Marina
"""

import re
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Paises:
    
    def read_country_data():
        # Lee los datos de la tabla de paises
        # En construcción
        data = []
        driver = Driver.set_useragent() 
        headers = read_country_headers()

        flag = True
        i=4
        while flag:
            dict = {}
            try:
                for j in range(len(headers)):
                    cell = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[5]/div[1]/table/tbody/tr[" + str(i) + "]/td[" + str(j+1) + "]")
                    dict[headers[j]] = cell.text
                data.append(dict)
                count = 0
            except:
                count += 1
                if count>3:
                    # Termina de buscar cuando no encuentra información en 3 filas consecutivas.
                    flag = False
            finally:
                i += 1

        data = pd.DataFrame(data)

        return data

    def clean_string(str):
        # Elimina referencias [a] [1] del texto
        return re.sub("[\(\[].â€*?[\)\]]", "", str)

    def read_country_headers():
        # Lee los nombres del encabezado de la tabla
        driver = Driver.set_useragent() 
        headers = []
        flag = True
        i = 1
        while flag:
            try:
                header = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[5]/div[1]/table/thead/tr/th[" + str(i) + "]")
                headers.append(clean_string(header.text))
                i += 1
            except:
                flag = False
        return headers
    
        
class Driver:
    
    def set_useragent():
        # Genera un driver y ajusta la configuracion de user_agent
        opts = Options()
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        opts.add_argument('user-agent=' + user_agent)
        driver = webdriver.Chrome(options=opts)
        return driver
    
    def driver(url):
        # Set up scraper
        driver = set_useragent()
        # Execute
        driver.get(url)
        # Read data
        print(driver.title)
        
    
class Archivo:
        
    def data2csv(nombre_csv, url):
        return Driver.driver(url)
        countries = Paises.read_country_data()
        ##countries.head()
        name_colums = list(countries.columns.values)
        #Las columnas que tenemos son
        countries.to_csv(nombre_csv, columns=name_colums, header=name_colums)
        # Close scraper
        driver.quit()
        
        
        
Driver.driver()

Archivo.data2csv('militar','https://en.wikipedia.org/wiki/List_of_sovereign_states')
