from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser = Service("C:\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR,'#cookie')

def store_list():
    buy = {}
    store = driver.find_element(By.CSS_SELECTOR, '#store')
    store_list1 = store.text.split('\n')
    store_list2 = []
    for item in store_list1:
        if len(item.split(' '))!=1:
            store_list2.append(item)
    # print(store_list2)
    for item in range(0, len(store_list2), 2):
        store_item = store_list2[item].split(' ')
        if store_item[0] == 'Time' or store_item[0] == 'Alchemy':
            buy[int(item / 2)] = {
                store_item[0]: int(store_item[3].replace(',', ''))
            }
        else:
            buy[int(item / 2)] = {
                store_item[0]: int(store_item[2].replace(',', ''))
            }
    money = int(driver.find_element(By.CSS_SELECTOR, '#money').text.replace(',',''))
    return max_buy(money,buy)

def max_buy(money,buy):
    global maxi
    for key in buy:
        for key1 in buy[key]:
            if  money> buy[key][key1]:
                maxi = key1
    return maxi


x=0
start = time.time()
end = time.time()

while end-start < 300:
    x+=1
    cookie.click()
    if x%800==0:
        maxi = store_list()
        # print(maxi)
        driver.find_element(By.CSS_SELECTOR,f'#buy{maxi}').click()
    end = time.time()
    # print(end-start)
cps = driver.find_element(By.CSS_SELECTOR, '#cps')
print(cps.text)

driver.quit()