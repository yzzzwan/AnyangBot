from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup

# local
options = webdriver.ChromeOptions()

prefs = {'profile.managed_default_content_settings.images': 2}
options.add_experimental_option('prefs', prefs)
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


start= time.time()

# available_timetable 변수를 받기 위한 전역변수
able_timetable=""
global available_timetable

# 사용자에게 아이디와 비밀번호를 입력받음
# id = input("아이디를 입력하세요: ")
# pw = input("비밀번호를 입력하세요: ")

# id = "2020E7011"
# pw="rladyddhks1!"

# 크롬 브라우저 열기
# driver.implicitly_wait(3)
# 포탈 사이트 로그인 페이지 열기
def test(pid, ppw):
    print("포탈 접속 시도")
    success = "f"

    driver.get("https://portal.anyang.ac.kr/")
    driver.implicitly_wait(10) # seconds
    print("포탈 접속")


    # 아이디와 비밀번호 입력 후 로그인 버튼 클릭
    login_id = driver.find_element("name", "login")
    login_pw = driver.find_element("name", "password")

    # id pw 입력
    login_id.send_keys(pid)
    login_pw.send_keys(ppw)


    # 로그인 버튼 클릭
    driver.find_element('id', 'loginImg').click()

    # 로그인 처리중입니다. 잠시만 기다려주세요 \n\n *최초 로그인시에는 로그인이 조금 지연될 수 있습니다.
    try:
        WebDriverWait(driver, 1).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()

    except:
        pass

    # 같은 계정으로 이미 로그인 되어있습니다. \n로그인 되어있던 계정은 로그아웃됩니다.
    try:
        WebDriverWait(driver, 1).until(EC.alert_is_present())
        alert = driver.switch_to.com
        alert.accept()

    except:
        pass


    # 로그인 완료되면 포탈페이지로 이동
    if driver.current_url == "https://portal.anyang.ac.kr/index.jsp#":
        print("포탈 로그인 실패!")
        driver.quit()
        exit()
    else:
        print("포탈 로그인 성공!")

    driver.get("https://ari.anyang.ac.kr/sso/index.jsp")

    driver.get("https://ari.anyang.ac.kr/user/jobcafe/index.do?code=001")
    #driver.implicitly_wait(10) # seconds
    print("studyroom페이지 접속")

    page_source = driver.page_source

    # html 파싱
    soup = BeautifulSoup(page_source, 'html.parser')

    # 시간표가 나와있는 div
    time_div = soup.select_one('div.tabType05.mt15.time-select')

    # 선택 가능한 시간표 리스트
    time_li_list = time_div.select('li')

    available_timetable_list = []

    for li in time_li_list:
        available_timetable = li.select_one('label')
        print(available_timetable.text)
        available_timetable_list.append(available_timetable.text)


    # # 시간표가 나와있는 div
    # time_div = driver.find_element(By.CSS_SELECTOR, "div.tabType05.mt15.time-select")
    #
    # # 선택 가능한 시간표 리스트
    # time_li_list = time_div.find_elements(By.CSS_SELECTOR, 'li:not(.dsb)')
    #
    # test_print = []
    # global available_timetable
    #
    # for li in time_li_list:
    #     available_timetable = li.find_element(By.CSS_SELECTOR, 'label')
    #     print(available_timetable.text)
    #     test_print.append(available_timetable.text)
    #
    # end = time.time()
    # print(end-start)