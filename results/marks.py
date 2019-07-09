import urllib.request
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

browser = webdriver.Chrome("C:\\Users\\ACER\\Downloads\\chromedriver_win32\\chromedriver.exe")
browser.get("https://rguktn.ac.in/examcell/ConsolidatedResults/2015_Engg/")

df = pd.read_csv('half3.csv')

ids = list(df['0'])
passwds = list(df['1'])
print(ids)
m = []
for i in range(len(ids)):
    try:
        print(ids[i])
        print(passwds[i])
        ID = browser.find_element_by_id('id')
        ID.send_keys(ids[i])

        passwd = browser.find_element_by_id('password')
        passwd.send_keys(passwds[i],Keys.ENTER)

#/html/body/div[1]/div/section/div/div/table/thead/tr[3]/th[3]
        marks = browser.find_element_by_xpath("/html/body/div[1]/div/section/div/div/table/thead/tr[3]/th[3]")
        print(marks.text.split(":")[1])
        m.append(marks.text.split(":")[1])
        time.sleep(10)
        browser.find_element_by_link_text('Logout').click()
    except:
        m.append('NAN')
