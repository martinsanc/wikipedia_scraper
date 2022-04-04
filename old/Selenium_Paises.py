# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 15:13:28 2022

@author: Marina, Martin
"""

import re
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


url = 'https://en.wikipedia.org/wiki/List_of_sovereign_states'


def set_useragent():
    # Genera un driver y ajusta la configuracion de user_agent
    opts = Options()
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    opts.add_argument('user-agent=' + user_agent)
    driver = webdriver.Chrome(options=opts)
    return driver

def read_country_data():
    # Lee los datos de la tabla de paises
    # En construcción
    data = []
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
    return re.sub("[\(\[].*?[\)\]]", "", str)

def read_country_headers():
    # Lee los nombres del encabezado de la tabla
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



# Set up scraper
driver = set_useragent()

# Execute
driver.get(url)

# Read data
print(driver.title)
countries = read_country_data()

countries.head()
countries.to_csv('countries.csv')

# Close scraper
driver.quit()





'''
def get_upcoming_events(url):
    driver = webdriver.Chrome()
    driver.get(url)

    events = driver.find_elements_by_xpath('//ul[contains(@class, "list-recent-events")]/li')

    for event in events:
        event_details = dict()
        event_details['name'] = event.find_element_by_xpath('h3[@class="event-title"]/a').text
        event_details['location'] = event.find_element_by_xpath('p/span[@class="event-location"]').text
        event_details['time'] = event.find_element_by_xpath('p/time').text
        print(event_details)

    driver.close()

get_upcoming_events('https://www.python.org/events/python-events/')
'''