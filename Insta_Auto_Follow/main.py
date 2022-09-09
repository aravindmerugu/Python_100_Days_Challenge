from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


SIMILAR_ACCOUNT = 'indian_polity__'
USER_NAME = 'YOUR_INSTA_USERNAME'
PASSWORD = 'INSTA_PASSWORD'

class InstaFollower:
    def __init__(self):
        self.ser = Service("C:\chromedriver_win32\chromedriver.exe")
        self.op = webdriver.ChromeOptions()
        self.op.add_argument(("--start-maximized"))
        self.driver = webdriver.Chrome(service=self.ser, options=self.op)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        uname = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        uname.send_keys(USER_NAME)
        upwd = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        upwd.send_keys(PASSWORD)
        upwd.send_keys(Keys.ENTER)
        time.sleep(4)
        self.driver.find_element(By.CSS_SELECTOR,'.aOOlW.HoLwm').click()


    def find_followers(self):
        # search = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        # search.send_keys(SIMILAR_ACCOUNT)
        # time.sleep(2)
        # search.send_keys(Keys.ENTER)
        # search.send_keys(Keys.ENTER)
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/')
        self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div').click()
        time.sleep(2)

    def follow(self):
        follow_list = self.driver.find_elements(By.CSS_SELECTOR, 'li div button')
        print(follow_list)
        for item in follow_list:
            try:
                item.click()
                time.sleep(1)
                follow_list_temp = self.driver.find_elements(By.CSS_SELECTOR, 'li div button')
                for temp_item in follow_list_temp:
                    if temp_item not in follow_list:
                        follow_list.append(temp_item)
            except ElementClickInterceptedException as e:
                self.driver.find_element(By.CSS_SELECTOR,'.aOOlW.HoLwm').click()
                time.sleep(1)
                print(e)
            except StaleElementReferenceException as e:
                print(e)


instafollower = InstaFollower()

instafollower.login()
instafollower.find_followers()
instafollower.follow()