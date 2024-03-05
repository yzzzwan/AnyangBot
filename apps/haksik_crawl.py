import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

# local
# driver = webdriver.ChromeOptions()
# driver.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver.Chrome('C:\\Users\\kyw01\\Downloads\\chromedriver_win32\\chromedriver')
# driver.get('https://www.anyang.ac.kr/main/activities/school-cafeteria.do')
# #server
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=chrome_options)
# driver.get('https://www.anyang.ac.kr/main/activities/school-cafeteria.do')


def print_week_haksik():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_options=chrome_options)
    # driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ExecutablePath="/usr/bin/chromedriver"), options=chrome_options)
    driver.get('https://www.anyang.ac.kr/main/activities/school-cafeteria.do')

    # 주간 학식 메뉴
    week_menu = ""

    # "날짜 + 월요일" 출력
    search_box = driver.find_element(By.CSS_SELECTOR,'th#mon')
    week_menu += search_box.text + "\n"

    # 월요일 학식
    search_box = driver.find_element(By.CSS_SELECTOR,'p.mon02')
    week_menu += search_box.text[6:]+"\n" + ("=" * 11) + "\n"

    # "날짜 + 화요일" 출력
    search_box = driver.find_element(By.CSS_SELECTOR,'th#tue')
    week_menu += search_box.text+"\n"

    # 화요일 학식
    search_box = driver.find_element(By.CSS_SELECTOR,'p.tue02')
    week_menu += search_box.text[6:]+"\n" + ("=" * 11) + "\n"

    # "날짜 + 수요일" 출력
    search_box = driver.find_element(By.CSS_SELECTOR,'th#wed')
    week_menu += search_box.text+"\n"

    # 수요일 학식
    search_box = driver.find_element(By.CSS_SELECTOR,'p.wed02')
    week_menu += search_box.text[6:]+"\n" + ("=" * 11) + "\n"

    # "날짜 + 목요일" 출력
    search_box = driver.find_element(By.CSS_SELECTOR,'th#thu')
    week_menu += search_box.text+"\n"

    # 목요일 학식
    search_box = driver.find_element(By.CSS_SELECTOR,'p.thu02')
    week_menu += search_box.text[6:]+"\n" + ("=" * 11) + "\n"

    # "날짜 + 금요일" 출력
    search_box = driver.find_element(By.CSS_SELECTOR,'th#fri')
    week_menu += search_box.text+"\n"

    # 금요일 학식
    search_box = driver.find_element(By.CSS_SELECTOR,'p.fri02')
    week_menu += search_box.text[6:]

    driver.quit()

    return week_menu


def print_today_haksik():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_options=chrome_options)
    driver.get('https://www.anyang.ac.kr/main/activities/school-cafeteria.do')

    haksik_notice = ("=" * 11) + "\n" + "11:00 ~ 15:00" + "\n" + "15:30 ~ 18:00"

    # 현재 요일 (월:0 화:1 수:2 목:3 금:4 토:5 일:6)
    now = datetime.now().weekday()

    # 주말
    if now == 5 or now == 6:
        today_menu = "오늘은 쉬는 날 입니다.😊"
        return today_menu

    menu_list=[]

    if now == 0:
        # "날짜 + 월요일" 출력
        search_box = driver.find_element(By.CSS_SELECTOR,'th#mon')
        menu_list.append(search_box.text+"\n")

        # 월요일 학식
        search_box = driver.find_element(By.CSS_SELECTOR,'p.mon02')
        menu_list.append(search_box.text[6:]+"\n")

    elif now == 1:
        # "날짜 + 화요일" 출력
        search_box = driver.find_element(By.CSS_SELECTOR,'th#tue')
        menu_list.append(search_box.text+"\n")

        # 화요일 학식
        search_box = driver.find_element(By.CSS_SELECTOR,'p.tue02')
        menu_list.append(search_box.text[6:]+"\n")

    elif now == 2:
        # "날짜 + 수요일" 출력
        search_box = driver.find_element(By.CSS_SELECTOR,'th#wed')
        menu_list.append(search_box.text+"\n")

        # 수요일 학식
        search_box = driver.find_element(By.CSS_SELECTOR,'p.wed02')
        menu_list.append(search_box.text[6:]+"\n")

    elif now == 3:
        # "날짜 + 목요일" 출력
        search_box = driver.find_element(By.CSS_SELECTOR,'th#thu')
        menu_list.append(search_box.text+"\n")

        # 목요일 학식
        search_box = driver.find_element(By.CSS_SELECTOR,'p.thu02')
        menu_list.append(search_box.text[6:]+"\n")

    elif now == 4:
        # "날짜 + 금요일" 출력
        search_box = driver.find_element(By.CSS_SELECTOR,'th#fri')
        menu_list.append(search_box.text+"\n")

        # 금요일 학식
        search_box = driver.find_element(By.CSS_SELECTOR,'p.fri02')
        menu_list.append(search_box.text[6:]+"\n")

        haksik_notice = ("=" * 11) + "\n" + "11:00 ~ 15:00" + "\n" + "(금요일 석식 X)"


    # 오늘의 메뉴
    today_menu= ""

    # 요일
    today_menu += menu_list[0]
    # 메뉴
    today_menu += menu_list[1]

    # 학식 운영시간
    today_menu += haksik_notice

    # 휴일일 경우.
    if len(menu_list[1]) == 1:
        today_menu = "오늘은 쉬는 날 입니다.😊"

    driver.quit()

    return today_menu

