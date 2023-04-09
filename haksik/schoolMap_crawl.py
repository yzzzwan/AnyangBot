# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# import requests
# from bs4 import BeautifulSoup
#
# # local
# driver = webdriver.ChromeOptions()
# driver.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver.Chrome('C:\\Users\\kyw01\\Downloads\\chromedriver_win32\\chromedriver')
# driver.get('https://www.anyang.ac.kr/main/introduction/anyang-campus-map.do')
# #time.sleep(1)
#
# #server
# # chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument('--headless')
# # chrome_options.add_argument('--no-sandbox')
# # chrome_options.add_argument('--disable-dev-shm-usage')
# # driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=chrome_options)
# # driver.get('https://www.anyang.ac.kr/main/introduction/anyang-campus-map.do')
# # # time.sleep(1)
#
#
#
# url = 'https://www.anyang.ac.kr/main/introduction/anyang-campus-map.do'
# res = requests.get(url)
# soup = BeautifulSoup(res.content, 'html.parser')
# print(soup)
# for i in range(10):
#     div_id = f'tab{i}LayerMap'
#     div_element = soup.select("#div_id")
#     bldg_name = div_element.select("h5").text()
#     #tbody_element = div_element.find('tbody')
#     #print(f'Tab{i}LayerMap tbody text:')
#     #print(tbody_element.get_text(strip=True)+"\n")
#     print(bldg_name)