# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 22:54:42 2022

@author: Marina, Martin
"""
from driver import Driver
from table import Table

#from IPython.display import display

if __name__ == '__main__':

    driver = Driver()

    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'
    xpath = '/html/body/div[3]/div[3]/div[5]/div[1]/table/'
    t = Table(driver, url, xpath)
    t.data2csv('data/poblacion.csv')
    
    url = 'https://en.wikipedia.org/wiki/List_of_official_languages_by_country_and_territory'
    xpath = '/html/body/div[3]/div[3]/div[5]/div[1]/table[2]/'
    t = Table(driver, url, xpath)
    t.data2csv('data/idioma.csv')
    
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_unemployment_rate'
    xpath = '/html/body/div[3]/div[3]/div[5]/div[1]/table[1]/'
    t = Table(driver, url, xpath)
    t.data2csv('data/desempleo.csv')
    
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_suicide_rate'
    xpath = '/html/body/div[3]/div[3]/div[5]/div[1]/table[1]/'
    t = Table(driver, url, xpath)
    t.data2csv('data/suicidios.csv')
    
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_obesity_rate'
    xpath = '/html/body/div[3]/div[3]/div[5]/div[1]/table/'
    t = Table(driver, url, xpath)
    t.data2csv('data/obesidad.csv')
    
    
    #display(t1.df.head())

    driver.quit()

