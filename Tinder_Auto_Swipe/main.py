from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time

ser = Service("C:\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_argument(("--start-maximized"))
driver = webdriver.Chrome(service=ser, options=op)
driver.get("https://tinder.com/")
original_window = driver.current_window_handle
time.sleep(3)
driver.find_element(By.LINK_TEXT,'Log in').click()
time.sleep(3)

# try:
#     driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
# except NoSuchElementException as e:
#     print(e)
try:
    driver.find_element(By.XPATH,'//*[@id="q-789368689"]/div/div/div[1]/div/div/div[3]/span/div[2]/button').click()
    driver.find_element(By.XPATH, '//*[@id="q939012387"]/div/div[2]/div/div/div[1]/div[1]/button').click()
except NoSuchElementException as e:
        print(e)
except StaleElementReferenceException as e:
    print(e)
try:
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="q-789368689"]/div/div/div[1]/div/div/div[3]/span/div[2]/button').click()
    driver.find_element(By.XPATH, '//*[@id="q939012387"]/div/div[2]/div/div/div[1]/div[1]/button').click()
except NoSuchElementException as e:
        print(e)
except StaleElementReferenceException as e:
    print(e)
# try:
# driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/button').click()
# driver.find_element(By.XPATH,'//html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button').click()
time.sleep(4)
driver.switch_to.window(driver.window_handles[1])
email = driver.find_element(By.ID,'email')
pwd = driver.find_element(By.ID, 'pass')
email.send_keys("YOUR_EMAIL")
pwd.send_keys("YOUR_PASSWORD")
pwd.send_keys(Keys.ENTER)

driver.switch_to.window(original_window)
time.sleep(3)
print(driver.current_url)
# driver.get('https://tinder.com/app/recs')
# print(driver.current_url)
time.sleep(2)
try:
    # driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/button').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[3]/button[1]').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[2]').click()

except NoSuchElementException as e:
        print(e)
time.sleep(10)
for i in range(1,100,1):
    try:
        btn = driver.find_elements(By.TAG_NAME,'button')
        for btn_v in btn:
            if btn_v.text == 'NOPE':
                btn_v.click()
    except StaleElementReferenceException as e:
        print(e)
        time.sleep(2)
    except NoSuchElementException as e:
        print(e)
        time.sleep(2)
    except ElementNotInteractableException as e:
        print(e)
        time.sleep(2)
    except ElementClickInterceptedException as e:
        print(e)
        time.sleep(2)