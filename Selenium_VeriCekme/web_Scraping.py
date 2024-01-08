
"""
1- Anasayfa duyurulara git
2- Duyurulardan ilkine sırayla girip çıkmasını ve oradaki değerleri almasını sağla
3- Programı kapat
"""


from selenium import webdriver
from time import sleep 
from selenium.webdriver.common.by import By
import requests
import pandas as pd 

browser = webdriver.Edge()

#Duyuru Anasayfası
duyuru1 = "https://yazilimtf.firat.edu.tr/tr/announcements-all"

browser.get(duyuru1)

sleep(3)

dizi_duyuru = []
"""
for i in range(12):
    elements_deneme = browser.find_elements(By.CSS_SELECTOR, '.news-section-card-right')
    for element in elements_deneme:
        dizi_duyuru.append(element.text)
"""
for i in range(12):
    baslık = browser.find_elements(By.CSS_SELECTOR, ".news-section-card-right-title")[i].text
    ıcerık = browser.find_elements(By.CSS_SELECTOR, ".news-section-card-right-explanation")[i].text
    tarih = browser.find_elements(By.CSS_SELECTOR, ".news-section-card-left-date")[i].text
    item = {
        'baslık': baslık,
        'icerik': ıcerık,
        'tarih': tarih
    }
    dizi_duyuru.append(item)

sleep(5)

#Duyuru 2. Sayfa
duyuru2 = "https://yazilimtf.firat.edu.tr/announcements-all/2"
browser.get(duyuru2)
"""
for i in range(12):
    elements_deneme = browser.find_elements(By.CSS_SELECTOR, '.news-section-card-right')
    for element in elements_deneme:
        dizi_duyuru.append(element.text)
"""
for i in range(12):
    baslık = browser.find_elements(By.CSS_SELECTOR, ".news-section-card-right-title")[i].text
    ıcerık = browser.find_elements(By.CSS_SELECTOR, ".news-section-card-right-explanation")[i].text
    tarih = browser.find_elements(By.CSS_SELECTOR, ".news-section-card-left-date")[i].text
    item = {
        'baslık': baslık,
        'icerik': ıcerık,
        'tarih': tarih
    }
    dizi_duyuru.append(item)

sleep(10)

# Akademik Kadro 
akademik_url1 = "https://yazilimtf.firat.edu.tr/tr/academic-staffs"

dizi_akademik = []

browser.get(akademik_url1)

sleep(3)
"""
for i in range(18):
    elements_deneme = browser.find_elements(By.CSS_SELECTOR, '.personnel-card') #  personnel-card-info-contact
    for i in elements_deneme:
        dizi_akademik.append(i.text)
"""
for i in range(18):
    Ad = browser.find_elements(By.CSS_SELECTOR, ".personnel-card-info-name")[i].text
    Mail = browser.find_elements(By.CSS_SELECTOR, ".personnel-card-info-contact-mail")[i].text
    CalısmaAlan = browser.find_elements(By.CSS_SELECTOR, ".personnel-card-info-work-places")[i].text
    item = {
        'ad': Ad,
        'mail': Mail,
        'calısmalanları': CalısmaAlan
    }
    dizi_akademik.append(item)

sleep(3)

#print(dizi_akademik)

browser.quit()

duyuru_dataset = pd.DataFrame({"Veriler_Duyurular": dizi_duyuru})
#print(duyuru_dataset)
akademik_dataset = pd.DataFrame({"Veriler_Akademik": dizi_akademik})
#print(akademik_dataset)


duyuru_dataset.to_csv("duyuru_dataset.csv", index=False)
akademik_dataset.to_csv("akademik_dataset.csv", index=False)