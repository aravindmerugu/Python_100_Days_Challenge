from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ser = Service("C:\chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get("https://www.linkedin.com/jobs/view/3032789475/?eBP=JOB_SEARCH_ORGANIC&recommendedFlavor=JOB_SEEKER_QUALIFIED&refId=bFhPL5sUsuNdsF616tcSqg%3D%3D&trackingId=VTKbL1W7G4Vhyp3qIE%2BI3A%3D%3D&trk=flagship3_search_srp_jobs")
driver.find_element(By.LINK_TEXT,'Sign in').click()
uname=driver.find_element(By.CSS_SELECTOR,'#username')
uname.send_keys("aravindmeruguwgl@gmail.com")
pwd = driver.find_element(By.CSS_SELECTOR,'#password')
pwd.send_keys("@Infopath77")
pwd.send_keys(Keys.ENTER)
url=driver.find_element(By.CSS_SELECTOR,'.jobs-unified-top-card__company-name').click()


driver.quit()