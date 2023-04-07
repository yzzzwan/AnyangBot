from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# # local
# driver = webdriver.ChromeOptions()
# driver.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver.Chrome('C:\\Users\\kyw01\\Downloads\\chromedriver_win32\\chromedriver')
# driver.get('https://www.anyang.ac.kr/main/activities/school-cafeteria.do')
# #time.sleep(1)

# server
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=chrome_options)
driver.get('https://www.anyang.ac.kr/main/activities/school-cafeteria.do')



# "날짜 + 월요일" 출력
search_box = driver.find_element(By.CSS_SELECTOR,'th#mon')
print(search_box.text)

# "날짜 + 화요일" 출력
search_box = driver.find_element(By.CSS_SELECTOR,'th#tue')
print(search_box.text)

# "날짜 + 수요일" 출력
search_box = driver.find_element(By.CSS_SELECTOR,'th#wed')
print(search_box.text)

# "날짜 + 목요일" 출력
search_box = driver.find_element(By.CSS_SELECTOR,'th#thu')
print(search_box.text)

# "날짜 + 금요일" 출력
search_box = driver.find_element(By.CSS_SELECTOR,'th#fri')
print(search_box.text)


menu_list=[]

# 월요일 학식
search_box = driver.find_element(By.CSS_SELECTOR,'p.mon02')
menu_list.append(search_box.text[6:])
#print(search_box.text[6:])

# 화요일 학식
search_box = driver.find_element(By.CSS_SELECTOR,'p.tue02')
menu_list.append(search_box.text[6:])
#print(search_box.text[6:])

# 수요일 학식
search_box = driver.find_element(By.CSS_SELECTOR,'p.wed02')
menu_list.append(search_box.text[6:])
#print(search_box.text[6:])

# 목요일 학식
search_box = driver.find_element(By.CSS_SELECTOR,'p.thu02')
menu_list.append(search_box.text[6:])
#print(search_box.text[6:])

# 금요일 학식
search_box = driver.find_element(By.CSS_SELECTOR,'p.fri02')
menu_list.append(search_box.text[6:])
#print(search_box.text[6:])


print(menu_list)


