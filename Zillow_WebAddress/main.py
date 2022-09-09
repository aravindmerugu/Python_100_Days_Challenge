from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
from bs4 import BeautifulSoup
import requests
import lxml
import pprint

headers = {
    "User-Agent": "your headers info",
    "Accept-Language": "your headers info"
}
LINK = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.64481581640625%2C%22east%22%3A-122.22184218359375%2C%22south%22%3A37.633501230568804%2C%22north%22%3A37.916810261970156%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
response = requests.get(url=LINK,headers=headers)
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "lxml")

# pprint.pprint(soup)

# all_anchor_tags = soup.findAll(name="a", class_ = 'list-card-link')
# for a in all_anchor_tags:
#     print(a.get('href'))

# print(all_anchor_tags)


links = soup.findAll(name="a", class_="list-card-link",tabindex="0")
all_links = [i.get('href') for i in links if "www" in i.get('href')]
prices = soup.findAll(class_="list-card-price")
address = soup.findAll(class_ = 'list-card-addr')
all_prices = [obj.text for obj in prices]
all_address = [obj.text for obj in address]
# print(address)

GOOGLE_DOC = 'https://forms.gle/UdfhGCDuv3KRG5uh9'

ser = Service("C:\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_argument(("--start-maximized"))

driver = webdriver.Chrome(service=ser, options=op)
# print(input_elements)
info = {}
for i in range(len(all_links)):
    info[i] = {
        "address": all_address[i],
        "link":all_links[i],
        "price":all_prices[i]
    }
    driver.get(GOOGLE_DOC)
    time.sleep(3)
    input_elements = driver.find_elements(By.CSS_SELECTOR, '.whsOnd')
    for j in range(len(input_elements)):
        if j == 0:
            input_elements[0].send_keys(f"{all_address[i]}")
            time.sleep(1)
        if j == 1:
            input_elements[1].send_keys(f"{all_prices[i]}")
            time.sleep(1)
        if j == 2:
            input_elements[2].send_keys(f"{all_links[i]}")
            time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,'.NPEfkd').click()
    time.sleep(2)

# all_prices = [for ]
print(info)



# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.alert import Alert
# import time
#
# ser = Service("C:\chromedriver_win32\chromedriver.exe")
# op = webdriver.ChromeOptions()
# op.add_argument(("--start-maximized"))
# driver = webdriver.Chrome(service=ser, options=op)
#
# driver.get('https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.64481581640625%2C%22east%22%3A-122.22184218359375%2C%22south%22%3A37.633501230568804%2C%22north%22%3A37.916810261970156%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D')
#
# links = driver.find_elements(By.CLASS_NAME,'list-card-link')
# for link in links:
#     if 'https' in link:
#         print(link.get_attribute('href'))