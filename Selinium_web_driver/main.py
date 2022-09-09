# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# ser = Service("C:\chromedriver_win32\chromedriver.exe")
# op = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=ser, options=op)
# driver.get("https://www.python.org/")
# # price = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[10]/div[1]/div/table/tbody/tr[2]/td[2]/span[1]/span[1]')
# # print(price.get_attribute('innerHTML'))
#
# #--xpath--
# # upcoming_events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
# # upcoming_events_list = upcoming_events.text.split('\n')
# # print(upcoming_events_list)
# # upcoming_events_dict = {}
# # for i in range (0,len(upcoming_events_list),2):
# #     upcoming_events_dict[upcoming_events_list[i]] = upcoming_events_list[i+1]
# # print(upcoming_events_dict)
# event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
# event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
# events = {}
# for n in range(len(event_names)):
#     events[n] = {
#         "time": [event_times[n].text],
#         "name": [event_names[n].text],
#     }
# print(events)
#
# driver.quit()

import  time

start = time.time()

a =1

while(a<100000000):
    a+=1
end = time.time()

print(end-start)
