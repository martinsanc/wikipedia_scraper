# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 22:54:42 2022

@author: Marina, Martin
"""
from driver import Driver
from table import Table
from csv_handler import *
from utils import clean_string

names = [
    'poblacion',
    'desempleo',
    'suicidios',
    'obesidad'
]
urls = [
    'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)',
    'https://en.wikipedia.org/wiki/List_of_countries_by_unemployment_rate',
    'https://en.wikipedia.org/wiki/List_of_countries_by_suicide_rate',
    'https://en.wikipedia.org/wiki/List_of_countries_by_obesity_rate'
]
xpaths = [
    '/html/body/div[3]/div[3]/div[5]/div[1]/table/',
    '/html/body/div[3]/div[3]/div[5]/div[1]/table[1]/',
    '/html/body/div[3]/div[3]/div[5]/div[1]/table[1]/',
    '/html/body/div[3]/div[3]/div[5]/div[1]/table/'
]


def read_tables():
    for i in range(len(urls)):
        path = 'data/' + names[i] + '.csv'
        print("Scrapeando tabla " + names[i])
        t = Table(driver, urls[i], xpaths[i])
        t.data2csv('data/' + names[i] + '.csv')
        print("  Guardado " + names[i] + '.csv')


if __name__ == '__main__':
    # driver = Driver()
    # dfs = read_tables()
    # driver.quit()

    dfs = read_csv(names)
    df = merge_csvs(dfs)
    dfs[0].head()




