# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 15:13:28 2022

@author: Marina
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib3
from bs4 import BeautifulSoup
from random import randint
from time import sleep
import requests


class CarScraper():

    def __init__(self):
        self.url = 'https://www.esmadrid.com/calendario-eventos-madrid'
        self.data = []


    def scrap(self, pages):
        # Scrap the number of pages given
    
        for i in range (1, pages):
            opts = Options()
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
            opts.add_argument('user-agent='+user_agent)
            driver = webdriver.Chrome(chrome_options=opts)
            res = driver.get(self.url + '?pg=' + str(i))
            check_useragent = driver.execute_script('return navigator.userAgent;')
            bs = BeautifulSoup(res, "lxml")
            sleep(randint(2,10))
            print(str(bs)[:1000])
    
scraper = CarScraper()
scraper.scrap(2)
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