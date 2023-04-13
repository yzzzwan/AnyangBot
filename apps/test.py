from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# local
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)




start= time.time()

# available_timetable 변수를 받기 위한 전역변수
able_timetable=""
global available_timetable

# 사용자에게 아이디와 비밀번호를 입력받음
# id = input("아이디를 입력하세요: ")
# pw = input("비밀번호를 입력하세요: ")
def portal_login(id, pw):
    # id = "2020E7011"
    # pw="rladyddhks1!"

    # 크롬 브라우저 열기
    driver.implicitly_wait(3)
    # 포탈 사이트 로그인 페이지 열기
    print("포탈 접속 시도")
    success = "f"

    driver.get("https://portal.anyang.ac.kr/")
    driver.implicitly_wait(10) # seconds
    print("포탈 접속")

    #print(driver.page_source)

    # 아이디와 비밀번호 입력 후 로그인 버튼 클릭
    login_id = driver.find_element("name", "login")
    login_pw = driver.find_element("name", "password")

    # id pw 입력
    login_id.send_keys(id)
    login_pw.send_keys(pw)


    # 로그인 버튼 클릭
    driver.find_element('id', 'loginImg').click()
    # driver.find_element('xpath', '//*[@class="login_button"]/a').click()

    # //*[@id="tsf"]/div[2]/
    # id가 tsf인 모든 요소의 자식 div 요소 중 3번째 요소를 선택

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


    # 비밀번호 변경 페이지
    if driver.current_url == "https://portal.anyang.ac.kr/c/portal/login_event":
        driver.find_element("name", "pwdReset").click()


    # 로그인 완료되면 포탈페이지로 이동
    if  driver.current_url == "https://portal.anyang.ac.kr/index.jsp#":
        print("포탈 로그인 실패!")
        driver.quit()
        exit()
    else:
        print("포탈 로그인 성공!")

    driver.implicitly_wait(10) # seconds

    print("아리포폴 접속 시도")

    driver.get("https://ari.anyang.ac.kr/sso/index.jsp")
    driver.implicitly_wait(10) # seconds

    print("아리포폴 접속 성공")

    print("스터디룸 접속 시도")
    driver.get("https://ari.anyang.ac.kr/user/jobcafe/index.do?code=001")
    # driver.implicitly_wait(10) # seconds
    # time.sleep(10)

    print("스터디룸 접속 성공")

    driver.implicitly_wait(10) # seconds

    success = "s"
    return success



def show_timetable():
    portal_login()


    # 시간표가 나와있는 div
    time_div = driver.find_element(By.CSS_SELECTOR, "div.tabType05.mt15.time-select")

    # 선택 가능한 시간표 리스트
    time_li_list = time_div.find_elements(By.CSS_SELECTOR, 'li:not(.dsb)')

    test_print=[]
    global available_timetable

    for li in time_li_list:
        available_timetable = li.find_element(By.CSS_SELECTOR, 'label')
        print(available_timetable.text)
        test_print.append(available_timetable.text)

    return test_print

member = 1


def reserve():
    global available_timetable
    available_timetable.click()

    # 신청 버튼 클릭
    driver.find_element(By.CSS_SELECTOR, "a.btn02.green01.hv01").click()
    time.sleep(5)
    # print(driver.current_url)

    win = driver.window_handles
    # print(win)

    # 신청 팝업 창으로 이동
    driver.switch_to.window(win[1])

    input_member = driver.find_element("name", "mem")

    # 사용인원 입력
    input_member.send_keys(member)

    # 신청사유
    reason = "공부"

    input_reason = driver.find_element("name", "reason")

    # 신청사유 입력
    input_reason.send_keys(reason)

    # 동의 라벨 클릭
    driver.find_element("id", "agree").click()

    # 완료 버튼 클릭
    driver.find_element(By.CSS_SELECTOR, "a.btn02.green01.hv01").click()

    time.sleep(5)

    Alert(driver).accept()
    print("예약 완료!")
    driver.quit()

# test = show_timetable()
# time.sleep(15)
# re=reserve()

# end= time.time()
# print("test len = ",len(test))
#
# # 9시 10시 11시 12시 1시
# if len(test) < 5:
#     while(len(test) <5):
#         test.append("-")
#
# # 2시 3시 4시 5시 6시
# elif len(test) > 5 and len(test) < 10:
#     while(len(test) <10):
#         test.append("-")
#
# # 7시 8시 9시 10시
# elif len(test) > 10 and len(test) < 12:
#     while(len(test) <12):
#         test.append("-")
#
# for t in test:
#     print(t)
#
# print(len(test))
#
# print(start)
# print( end)
#

def test_login():
    # id = "2020E7011"
    # pw="rladyddhks1!"

    # 크롬 브라우저 열기
    driver.implicitly_wait(3)
    # 포탈 사이트 로그인 페이지 열기
    print("포탈 접속 시도")
    success = "f"

    driver.get("https://portal.anyang.ac.kr/")
    driver.implicitly_wait(10) # seconds
    print("포탈 접속")

    #print(driver.page_source)

    # 아이디와 비밀번호 입력 후 로그인 버튼 클릭
    login_id = driver.find_element("name", "login")
    login_pw = driver.find_element("name", "password")

    # id pw 입력
    login_id.send_keys(id)
    login_pw.send_keys(pw)


    # 로그인 버튼 클릭
    driver.find_element('id', 'loginImg').click()
    # driver.find_element('xpath', '//*[@class="login_button"]/a').click()

    # //*[@id="tsf"]/div[2]/
    # id가 tsf인 모든 요소의 자식 div 요소 중 3번째 요소를 선택

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


    # 비밀번호 변경 페이지
    if driver.current_url == "https://portal.anyang.ac.kr/c/portal/login_event":
        driver.find_element("name", "pwdReset").click()


    # 로그인 완료되면 포탈페이지로 이동
    if  driver.current_url == "https://portal.anyang.ac.kr/index.jsp#":
        print("포탈 로그인 실패!")
        driver.quit()
        exit()
    else:
        print("포탈 로그인 성공!")

#portal_login("2020E7011", "rladyddhks1!")
