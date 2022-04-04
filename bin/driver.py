# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 22:54:48 2022

@author: Marina, Martin
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:
    driver = None

    # Clase que contiene la inicializacion del driver, y los metodos para scrapear tablas.
    def __init__(self):
        self.driver = self.set_useragent()

    def set_useragent(self):
        # Genera un driver y ajusta la configuracion de user_agent
        opts = Options()
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        opts.add_argument('user-agent=' + user_agent)
        driver = webdriver.Chrome(options=opts)
        return driver

    def quit(self):
        self.driver.quit()
