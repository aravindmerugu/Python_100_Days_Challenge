from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ser = Service("C:\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_WT=3&geoId=102713980&keywords=software%20developer%20python&location=India")
driver.find_element(By.LINK_TEXT,'Sign in').click()
uname=driver.find_element(By.CSS_SELECTOR,'#username')
uname.send_keys("YOUR_EMAIL")
pwd = driver.find_element(By.CSS_SELECTOR,'#password')
pwd.send_keys("YOUR_PASSWORD")
pwd.send_keys(Keys.ENTER)
jobs_list=[]
jobs_url = driver.find_elements(By.CSS_SELECTOR,'li a')
for link in jobs_url:
    url = link.get_attribute('href')
    role = link.text
    if 'JOB_SEARCH' in url:
        jobs_list.append({'role':role,'url':url})
jobs_list.remove(jobs_list[0])

for item in jobs_list:
    try:
        web_url=item['url']
        driver.get(web_url)
        driver.find_element(By.CSS_SELECTOR,'.jobs-save-button').click()
        cname=driver.find_element(By.CSS_SELECTOR,'.p5 a')
        cname.click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,'.org-top-card-primary-actions__inner').find_element(By.TAG_NAME,'button').click()

    except NoSuchElementException as e:
        print(e)



time.sleep(300)