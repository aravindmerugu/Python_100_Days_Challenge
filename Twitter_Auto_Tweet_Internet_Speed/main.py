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

PROMISED_UP = 10
PROMISED_DOWN = 150
TWITTER_EMAIL = 'YOUR_EMAIL'
TWITTER_PASSWORD = 'YOUR_PASSWORD'


class Twitter:
    def __init__(self, ser, op):
        self.driver = webdriver.Chrome(service=ser, options=op)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '.start-button a').click()
        time.sleep(50)
        self.down = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]')
        self.up = self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]')
        self.down = self.down.text
        self.up = self.up.text
        print(self.down)
        print(self.up)


    def tweet_at_provider(self):
        self.driver.get('http://twitter.com/login')
        time.sleep(2)
        self.email = self.driver.find_element(By.NAME,"username")
        self.email.send_keys(TWITTER_EMAIL)
        self.email.send_keys(Keys.ENTER)
        time.sleep(2)
        self.password = self.driver.find_element(By.NAME,"password")
        self.password.send_keys(TWITTER_PASSWORD)
        self.password.send_keys(Keys.ENTER)

twiter = Twitter(ser, op)
twiter.get_internet_speed()
twiter.tweet_at_provider()

