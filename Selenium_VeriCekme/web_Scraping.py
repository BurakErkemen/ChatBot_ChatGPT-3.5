from selenium import webdriver
from time import sleep 
from selenium.webdriver.common.by import By

import requests
import pandas as pd 

browser = webdriver.Edge()
"""
1- Anasayfa duyurulara git
2- Duyurulardan ilkine sırayla girip çıkmasını ve oradaki değerleri almasını sağla
3- Programı kapat
"""
url = "https://yazilimtf.firat.edu.tr/tr/announcements-all"

browser.get(url)
sleep(10)
element_xpath = "/html/body/div[2]/div[1]/div[1]/a[1]/div[2]/div[1]/div[2]"
element = browser.find_element(By.XPATH, element_xpath).text

print(element)


browser.quit()
