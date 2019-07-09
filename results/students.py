import urllib.request
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

text = urllib.request.urlopen("file:///C:/Users/ACER/Desktop/sample/users.html").read()
text = str(text)
text = text.split("\\r\\n")
sub = "N15"
students = [i for i in text if sub in i]
dobl=[]
ids = [i.split(":")[0] for i in students]
passwds = [i.split(":")[1] for i in students]

print(ids)
browser = webdriver.Chrome("C:\\Users\\ACER\\Downloads\\chromedriver_win32\\chromedriver.exe")
browser.get("http://intranet.rguktn.ac.in/SMS/")
current_ids = []
for i in range(1,len(ids)):
        try:
                ID = browser.find_element_by_id("user1")
                ID.send_keys(ids[i])
                PSWD = browser.find_element_by_id("passwd1")
                PSWD.send_keys(passwds[i],Keys.ENTER)
                time.sleep(10)
                current_ids.append(ids[i])
                flag = 1
        except:
                pass
	try:
		browser.find_element_by_xpath("//input[@name='q1' and @value='1']").click()
		browser.find_element_by_xpath("//input[@name='q2' and @value='1']").click()
		browser.find_element_by_xpath("//input[@name='q3' and @value='1']").click()
		browser.find_element_by_xpath("//input[@name='q4' and @value='1']").click()
		browser.find_element_by_xpath("//input[@name='q5' and @value='1']").click()
		browser.find_element_by_xpath("//input[@name='q6' and @value='1']").click()

		browser.find_element_by_id("mformsubmit").click()
	except:
		pass
	if flag == 1:
                time.sleep(10)
                elem = browser.find_element_by_link_text('Profile')
                elem.get_attribute('href')
                elem.click()
                elem = browser.find_element_by_link_text('Edit Profile')
                elem.get_attribute('href')
                elem.click()

                dob = browser.find_element_by_id("dob").text
                print(dob)
                name = browser.find_element_by_id("sname").text
                print(name)
                dobl.append(dob)
                browser.find_element_by_link_text(name).click()
                browser.find_element_by_link_text("Sign out").click()
                flag = 0
df = pd.DataFrame(np.array([ids[1:len(dobl)+1],dobl]),column_names=['ID','DOB']) #column_names
df = pd.DataFrame(data=df)
df.to_csv('students.csv')



