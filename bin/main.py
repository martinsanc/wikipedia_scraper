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

    url = 'https://en.wikipedia.org/wiki/List_of_sovereign_states'
    xpath = '/html/body/div[3]/div[3]/div[5]/div[1]/table/'
    t1 = Table(driver, url, xpath)
    t1.data2csv('data/militar.csv')

    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'
    xpath = '/html/body/div[3]/div[3]/div[5]/div[1]/table/'
    t2 = Table(driver, url, xpath)
    t2.data2csv('data/poblacion.csv')

    # display(t1.df.head())

    driver.quit()
