# # from selenium import webdriver
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.common.by import By
# # import time
# # from selenium.webdriver.chrome.service import Service
# # from webdriver_manager.chrome import ChromeDriverManager
# # from selenium.webdriver.common.alert import Alert
# # from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# #
# # # local
# # options = webdriver.ChromeOptions()
# # options.add_argument('headless')
# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# #
# #
# #
# #
# # #start=time.time()
# #
# # # 사용자에게 아이디와 비밀번호를 입력받음
# # # id = input("아이디를 입력하세요: ")
# # # pw = input("비밀번호를 입력하세요: ")
# #
# # id = "2020E7011"
# # pw="rladyddhks1!"
# # member=1
# #
# # # 크롬 브라우저 열기
# # driver.implicitly_wait(3)
# # # 포탈 사이트 로그인 페이지 열기
# # driver.get("https://portal.anyang.ac.kr/")
# # driver.implicitly_wait(10) # seconds
# # time.sleep(3)
# # print("포탈 접속")
# #
# # #print(driver.page_source)
# #
# # # 아이디와 비밀번호 입력 후 로그인 버튼 클릭
# # login_id = driver.find_element("name", "login")
# # login_pw = driver.find_element("name", "password")
# #
# # # id pw 입력
# # login_id.send_keys(id)
# # login_pw.send_keys(pw)
# #
# #
# # # 로그인 버튼 클릭
# # driver.find_element('id', 'loginImg').click()
# # # driver.find_element('xpath', '//*[@class="login_button"]/a').click()
# #
# # # //*[@id="tsf"]/div[2]/
# # # id가 tsf인 모든 요소의 자식 div 요소 중 3번째 요소를 선택
# #
# # # 로그인 처리중입니다. 잠시만 기다려주세요 \n\n *최초 로그인시에는 로그인이 조금 지연될 수 있습니다.
# #
# #
# # try:
# #     WebDriverWait(driver, 1).until(EC.alert_is_present())
# #     alert = driver.switch_to.alert
# #     alert.accept()
# #
# # except:
# #     pass
# #
# # # 같은 계정으로 이미 로그인 되어있습니다. \n로그인 되어있던 계정은 로그아웃됩니다.
# # try:
# #     WebDriverWait(driver, 1).until(EC.alert_is_present())
# #     alert = driver.switch_to.com
# #     alert.accept()
# #
# # except:
# #     pass
# #
# # c = driver.get_cookies()
# # cd = {}
# # for o in c:
# #     cd[o['name']] = o['value']
# #
# #
# # # 비밀번호 변경 페이지
# # if driver.current_url == "https://portal.anyang.ac.kr/c/portal/login_event":
# #     driver.find_element("name", "pwdReset").click()
# #
# #
# # # 로그인 완료되면 포탈페이지로 이동
# # if  driver.current_url == "https://portal.anyang.ac.kr/index.jsp#":
# #     print("포탈 로그인 실패!")
# #     driver.quit()
# #     exit()
# # else:
# #     print("포탈 로그인 성공!")
# #
# # driver.implicitly_wait(10) # seconds
# # time.sleep(5)
# #
# #
# # print("아리포폴 접속 시도")
# # driver.get("https://ari.anyang.ac.kr/sso/index.jsp")
# # driver.implicitly_wait(10) # seconds
# # time.sleep(5)
# #
# # print("아리포폴 접속 성공")
# #
# # print("스터디룸 접속 시도")
# # driver.get("https://ari.anyang.ac.kr/user/jobcafe/index.do?code=001")
# # # driver.implicitly_wait(10) # seconds
# # # time.sleep(10)
# #
# # print("스터디룸 접속 성공")
# #
# # driver.implicitly_wait(10) # seconds
# #
# # # 시간표가 나와있는 div
# # time_div = driver.find_element(By.CSS_SELECTOR, "div.tabType05.mt15.time-select")
# #
# # # 선택 가능한 시간표 리스트
# # time_li_list = time_div.find_elements(By.CSS_SELECTOR, 'li:not(.dsb)')
# #
# # for li in time_li_list:
# #     available_timetable = li.find_element(By.CSS_SELECTOR, 'label')
# #     print(available_timetable.text)
# #
# #
# # # 시간 선택
# #
# #
# # # # a 태그 클릭
# # # a_tag.click()
# #
# #
# #
# # print(4)
# #
# # # end= time.time()
# # #
# # # print(start)
# # # print( end)
# #
#
#
# 'bot': {
#     'id': '63e23010dcff7159538d8bcd!',
#     'name': 'Anyang_Bot'},
#     'intent': {'id': '64300e313d79203595571252',
#                'name': 'Test Block',
#                'extra': {
#                    'reason': {
#                        'code': 101,
#                        'message': 'DIRECT_ID'
#                    }
#                }
#                },
#     'action': {
#         'id': '6435c502972b8a617307f70e',
#         'name': 'Self학습실 예약', 'params': {
#
#         },
#         'detailParams': {
#         },
#         'clientExtra': {
#         }
#     },
#     'userRequest': {
#         'block': {
#             'id': '64300e313d79203595571252',
#             'name': 'Test Block'
#         },
#         'user': {
#             'id': '53a84e54ebe5c3a7b96390e4551f0a3c0766c6455cea41a434e679388a80ea94b5',
#             'type': 'botUserKey',
#             'properties': {
#                 'botUserKey': '53a84e54ebe5c3a7b96390e4551f0a3c0766c6455cea41a434e679388a80ea94b5',
#                 'bot_user_key': '53a84e54ebe5c3a7b96390e4551f0a3c0766c6455cea41a434e679388a80ea94b5'
#             }
#         },
#         'utterance': '',
#         'params': {
#             'ignoreMe': 'true',
#             'surface': 'BuilderBotTest'
#         },
#         'lang': 'ko',
#         'timezone': 'Asia/Seoul'
#     },
#     'contexts': [{
#         'name': 'portal_id',
#         'lifespan': 5,
#         'ttl': 600,
#         'params': {
#             'portal_id': {'value': '손시려',
#                           'resolvedValue': '손시려'
#                           },

#             'portal_pw': {
#                 'value': '발시려',
#                 'resolvedValue': '발시려'
#             }
#         }
#     },
#         {
#             'name': 'portal_pw', 'lifespan': 5,
#             'ttl': 600,
#             'params': {
#                 'portal_id': {
#                     'value': '손시려',
#                     'resolvedValue': '손시려'
#                 },
#                 'portal_pw': {
#                     'value': '발시려',
#                     'resolvedValue': '발시려'}}}]}