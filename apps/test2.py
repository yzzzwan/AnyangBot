# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from bs4 import BeautifulSoup
# from selenium.common.exceptions import TimeoutException
#
# chrome_options = webdriver.ChromeOptions()
# prefs = {'profile.managed_default_content_settings.images': 2}
# chrome_options.add_experimental_option('prefs', prefs)
# # options.add_argument('--headless')
# chrome_options.add_argument('--blink-settings=imagesEnabled=false')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=chrome_options)
# driver.implicitly_wait(3)  # seconds
#
#
# # available_timetable 변수를 받기 위한 전역변수
# available_timetable = ""
# available_time_list=[]
# driver.get("https://portal.anyang.ac.kr/")
# driver.implicitly_wait(3)  # seconds
#
# # pid = "2020E7011"
# # ppw="rladyddhks1!"
#
#
# # 포탈 로그인
# def portal(pid, ppw):
#     print("start")
#     start = time.time()
#
#     print("포탈 접속 시도")
#     success = "f"
#     # sp=time.time()
#
#     print("포탈 접속")
#     # ep = time.time()
#     # print("포탈 접속 시간 = ",ep-sp)
#
#     # sl = time.time()
#
#     # 아이디와 비밀번호 입력 후 로그인 버튼 클릭
#     login_id = driver.find_element("name", "login")
#     login_pw = driver.find_element("name", "password")
#
#     # id pw 입력
#     login_id.send_keys(pid)
#     login_pw.send_keys(ppw)
#
#
#     # 로그인 버튼 클릭
#     driver.find_element('id', 'loginImg').click()
#
#     # 로그인 처리중입니다. 잠시만 기다려주세요 \n\n *최초 로그인시에는 로그인이 조금 지연될 수 있습니다.
#     try:
#         WebDriverWait(driver, 0.6).until(EC.alert_is_present())
#         alert = driver.switch_to.alert
#         alert.accept()
#
#     except:
#         pass
#
#     # 같은 계정으로 이미 로그인 되어있습니다. \n로그인 되어있던 계정은 로그아웃됩니다.
#     try:
#         WebDriverWait(driver).until(EC.alert_is_present())
#         alert = driver.switch_to.com
#         alert.accept()
#
#     except:
#         pass
#
#
#     # 로그인 완료되면 포탈페이지로 이동
#     if driver.current_url == "https://portal.anyang.ac.kr/index.jsp#":
#         print("포탈 로그인 실패!")
#         driver.quit()
#         return success
#     else:
#         print("포탈 로그인 성공!")
#
#     # el = time.time()
#     # print("로그인 시간 = ",el-sl)
#
#     # sa = time.time()
#     # print("포폴 접속시도")
#     end = time.time()
#     print("login :", end - start)
#     success="s"
#     return success
#
#
#
# def ari(room_num):
#     global available_timetable
#     global available_time_list
#     print("start")
#     start = time.time()
#     driver.get("https://ari.anyang.ac.kr/sso/index.jsp")
#
#     # try:
#     #     print("로딩중1")
#     #     driver.get("https://ari.anyang.ac.kr/sso/index.jsp")
#     #     print("로딩중2")
#     #     wait = WebDriverWait(driver, 1)
#     #     element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.warp div.area_head')))
#     #
#     #     # WebDriverWait(driver, 2).until(EC.title_contains("body"))  # 변경 필요
#     #     print("포폴 접속 성공")
#     # except TimeoutException:
#     #     print("Timeout occurred.")
#     #     #driver.quit()
#
#     print(driver.current_url)
#
#     driver.get("https://ari.anyang.ac.kr/user/jobcafe/index.do?code=00" + room_num)
#     driver.implicitly_wait(10) # seconds
#     # print("studyroom페이지 접속")
#     print(driver.current_url)
#
#     # 시간표가 나와있는 div
#     time_div = driver.find_element(By.CSS_SELECTOR, "div.tabType05.mt15.time-select")
#
#     # 선택 가능한 시간표 리스트
#     time_li_list = time_div.find_elements(By.CSS_SELECTOR, 'li:not(.dsb)')
#
#     available_time_list=[]
#     cnt=0
#     for li in time_li_list:
#         available_timetable = li.find_element(By.CSS_SELECTOR, 'label')
#         #print(available_timetable.text)
#         available_time_list.append(available_timetable)
#         cnt+=1
#
#
#     end = time.time()
#     print("print times : ", end - start)
#     return cnt
#
#
#
#
# def reserve(t):
#     done ="fail"
#     global available_timetable
#     start = time.time()
#
#     # 시간 클릭
#     available_time_list[t-1].click()
#
#     # 신청 클릭
#     driver.find_element(By.CSS_SELECTOR, "a.btn02.green01.hv01").click()
#     #print(driver.current_url)
#
#     win = driver.window_handles
#
#     # 신청 팝업 창으로 이동
#     driver.switch_to.window(win[1])
#
#     input_member = driver.find_element("name", "mem")
#
#     # 사용인원 입력
#     input_member.send_keys("1")
#
#     # 신청사유
#     reason = "공부"
#
#     input_reason = driver.find_element("name", "reason")
#
#     # 신청사유 입력
#     input_reason.send_keys(reason)
#
#     # 동의 라벨 클릭
#     driver.find_element("id", "agree").click()
#
#     # 완료 버튼 클릭
#     driver.find_element(By.CSS_SELECTOR, "a.btn02.green01.hv01").click()
#
#     Alert(driver).accept()
#
#     end = time.time()
#     print("reserve : ", end - start)
#     print("done")
#     done = "done"
#     return done
#
#
#
#
# # print(portal("2020E7011", "rladyddhks1!")) #login : 0.777327299118042
# # z=ari("1") #print times :  2.3316853046417236
# # reserve(z) #reserve :  0.29192113876342773
#
#
#
# # 일단 시간 선택해서 원하는 룸에 예약하는거 까지 했음.
# # 배포 과정만 거치면 되는데...
# # 하나는 2시간 초과 예약시 오류 처리 이것만 해결하면돼
