# import datetime
#
# # today = datetime.date.today()
# today = datetime.date(2023, 5, 26)
# month = str(today)[5:7]
# date =str(today)[8:10]
#
# # print(month + date)
# # print(today)
#
# # 주말을 제외한 5일간의 날짜 구하기
# count = 0
# week_dates = []
# while count < 5:
#     if today.weekday() < 5:  # 주말(토요일: 5, 일요일: 6)이 아닌 경우만 추가
#         week_dates.append(int(str(today)[8:10]))
#         count += 1
#     today += datetime.timedelta(days=1)
#
# print(week_dates)

import portal_login_user
import studyroom_Timetable
# import reserve_studyroom
import choose_date
a="01"
def one():
    portal_login_user.portal("2020E7011", "rladyddhks1!")

def two():
    K=studyroom_Timetable.show_studyroom_timetable(a)
    print(K)

def thr():
    print(reserve_studyroom.selfroom_reserve(1))

def four():
    K = studyroom_Timetable.show_studyroom_timetable(a,2)
    print(K)

one()
four()
# two()
# thr()

# o,
# import time
# # # print("start a")
# # # sa=time.time()
# # # a=portal_login_user.portal("2020E7011","rladyddhks1!")
# # # ea=time.time()
# # # print("end a")
# # #
# # # print(ea-sa)
# # #
# # print("start b")
# # sb=time.time()
# # b=studyroom_Timetable.show_studyroom_timetable("01")
# # eb=time.time()
# # print("end b")
# # print(b)
# # print(eb-sb)
# #
# #
# #
# #
# #
# # a="1"
# # def one():
# #     portal_login_user.portal("2020E7011","rladyddhks1!")
# #
# # def two():
# #     K=studyroom_Timetable.show_studyroom_timetable(a)
# #     print(K)
# # #
# # one()
# # two()
#
# # def tt():
# #     return "test"
#
#
#
#
#
#
#
#
#

#
#
#
#
#
#
#     ## studyroom full code
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# # local
# options = webdriver.ChromeOptions()
# prefs = {'profile.managed_default_content_settings.images': 2}
# options.add_experimental_option('prefs', prefs)
# # options.add_argument('--headless')
# options.add_argument('--blink-settings=imagesEnabled=false')
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#
#
#
#
# #start=time.time()
#
# # 사용자에게 아이디와 비밀번호를 입력받음
# # id = input("아이디를 입력하세요: ")
# # pw = input("비밀번호를 입력하세요: ")
#
# id = "2020E7011"
# pw="rladyddhks1!"
# member=1
#
# # 크롬 브라우저 열기
# driver.implicitly_wait(3)
# # 포탈 사이트 로그인 페이지 열기
# driver.get("https://portal.anyang.ac.kr/")
# driver.implicitly_wait(10) # seconds
# time.sleep(3)
# print("포탈 접속")
#
# #print(driver.page_source)
#
# # 아이디와 비밀번호 입력 후 로그인 버튼 클릭
# login_id = driver.find_element("name", "login")
# login_pw = driver.find_element("name", "password")
#
# # id pw 입력
# login_id.send_keys(id)
# login_pw.send_keys(pw)
#
#
# # 로그인 버튼 클릭
# driver.find_element('id', 'loginImg').click()
# # driver.find_element('xpath', '//*[@class="login_button"]/a').click()
#
# # //*[@id="tsf"]/div[2]/
# # id가 tsf인 모든 요소의 자식 div 요소 중 3번째 요소를 선택
#
# # 로그인 처리중입니다. 잠시만 기다려주세요 \n\n *최초 로그인시에는 로그인이 조금 지연될 수 있습니다.
#
#
# try:
#     WebDriverWait(driver, 1).until(EC.alert_is_present())
#     alert = driver.switch_to.alert
#     alert.accept()
#
# except:
#     pass
#
# # 같은 계정으로 이미 로그인 되어있습니다. \n로그인 되어있던 계정은 로그아웃됩니다.
# try:
#     WebDriverWait(driver, 1).until(EC.alert_is_present())
#     alert = driver.switch_to.com
#     alert.accept()
#
# except:
#     pass
#
#
#
# # # 비밀번호 변경 페이지
# # if driver.current_url == "https://portal.anyang.ac.kr/c/portal/login_event":
# #     driver.find_element("name", "pwdReset").click()
#
#
# # 로그인 완료되면 포탈페이지로 이동
# if  driver.current_url == "https://portal.anyang.ac.kr/index.jsp#":
#     print("포탈 로그인 실패!")
#     driver.quit()
#     exit()
# else:
#     print("포탈 로그인 성공!")
#
# driver.implicitly_wait(10) # seconds
# time.sleep(5)
#
#
# print("아리포폴 접속 시도")
# driver.get("https://ari.anyang.ac.kr/sso/index.jsp")
# driver.implicitly_wait(10) # seconds
# time.sleep(5)
#
# print("아리포폴 접속 성공")
#
# print("스터디룸 접속 시도")
# driver.get("https://ari.anyang.ac.kr/user/jobcafe/index.do?code=001")
# # driver.implicitly_wait(10) # seconds
# # time.sleep(10)
#
# print("스터디룸 접속 성공")
#
# driver.implicitly_wait(10) # seconds
#
# # 시간표가 나와있는 div
# time_div = driver.find_element(By.CSS_SELECTOR, "div.tabType05.mt15.time-select")
#
# # 선택 가능한 시간표 리스트
# time_li_list = time_div.find_elements(By.CSS_SELECTOR, 'li:not(.dsb)')
#
# for li in time_li_list:
#     available_timetable = li.find_element(By.CSS_SELECTOR, 'label')
#     print(available_timetable.text)
#
# # 시간 선택
# available_timetable.click()
#
# # 신청 버튼 클릭
# driver.find_element(By.CSS_SELECTOR, "a.btn02.green01.hv01").click()
# time.sleep(5)
# #print(driver.current_url)
#
# win = driver.window_handles
# #print(win)
#
# # 신청 팝업 창으로 이동
# driver.switch_to.window(win[1])
#
#
#
# input_member = driver.find_element("name", "mem")
#
# # 사용인원 입력
# input_member.send_keys(member)
#
# # 신청사유
# reason = "공부"
#
# input_reason = driver.find_element("name", "reason")
#
# # 신청사유 입력
# input_reason.send_keys(reason)
#
# # 동의 라벨 클릭
# driver.find_element("id", "agree").click()
#
# # 완료 버튼 클릭
# driver.find_element(By.CSS_SELECTOR, "a.btn02.green01.hv01").click()
#
# time.sleep(5)
#
# Alert(driver).accept()
#
# # # a 태그 클릭
# # a_tag.click()
#
#
#
# print(4)
#
# # end= time.time()
# #
# # print(start)
# # print( end)
#
#
# {
#     'bot': {
#         'id': '63e23010dcff7159538d8bcd!',
#         'name': 'Anyang_Bot'
#     },
#     'intent': {
#         'id': '6457acc18edae924e926b707',
#         'name': 'self 학습실 예약',
#         'extra': {
#             'reason': {
#                 'code': 101,
#                 'message': 'DIRECT_ID'
#             }
#         }
#     },
#     'action': {
#         'id': '6457ae843cae9c5307475315',
#         'name': 'self 학습실 예약',
#         'params': {
#
#         },
#         'detailParams': {
#
#         },
#         'clientExtra': {
#             'num': 12, 'room': 'Self 학습실4'}}, 'userRequest': {'block': {'id': '6457acc18edae924e926b707', 'name': 'self 학습실 예약'}, 'user': {'id': '53a84e54ebe5c3a7b96390e4551f0a3c0766c6455cea41a434e679388a80ea94b5', 'type': 'botUserKey', 'properties': {'botUserKey': '53a84e54ebe5c3a7b96390e4551f0a3c0766c6455cea41a434e679388a80ea94b5', 'bot_user_key': '53a84e54ebe5c3a7b96390e4551f0a3c0766c6455cea41a434e679388a80ea94b5'}}, 'utterance': '', 'params': {'ignoreMe': 'true', 'surface': 'BuilderBotTest'}, 'lang': 'ko', 'timezone': 'Asia/Seoul'}, 'contexts': [{'name': 'portal_id', 'lifespan': 1, 'ttl': 600, 'params': {'portal_id': {'value': '2020e7011', 'resolvedValue': '2020e7011'}, 'portal_pw': {'value': 'rladyddhks1!', 'resolvedValue': 'rladyddhks1!'}}}, {'name': 'portal_pw', 'lifespan': 1, 'ttl': 600, 'params': {'portal_id': {'value': '2020e7011', 'resolvedValue': '2020e7011'}, 'portal_pw': {'value': 'rladyddhks1!', 'resolvedValue': 'rladyddhks1!'}}}, {'name': 'where_room', 'lifespan': 3, 'ttl': 600, 'params': {}}]}