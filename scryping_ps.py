from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd 

sleep(1)
print('here')

#options = Options()
#options.add_argument('--headless')
#browser = webdriver.Chrome(options = options)
browser = webdriver.Chrome('chromedriver.exe')

url = 'https://scraping-for-beginner.herokuapp.com/login_page'
browser.get(url)

elem_username = browser.find_element_by_id('username')
elem_username.send_keys('imanishi')

elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')

elem_login_btn = browser.find_element_by_id('login-btn')
elem_login_btn.click()

elems_th = browser.find_elements_by_tag_name('th')
keys = []
for elem_th in elems_th:
    key = elem_th.text
    keys.append(key)

elems_td = browser.find_elements_by_tag_name('td')
values = []
for elem_td in elems_td:
    value = elem_td.text
    values.append(value)

print(keys)
print(values)

df = pd.DataFrame()
df['項目'] = keys
df['値'] = values

df.to_csv('講師情報.csv',index=False)

browser.quit()
