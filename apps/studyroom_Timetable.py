# import time
#
# import portal_login_user as plu
# # from selenium import webdriver
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # import time
# #
# # chrome_options = webdriver.ChromeOptions()
# #
# # # chrome_options.add_argument('--headless')
# # chrome_options.add_argument('--disable-gpu')
# # chrome_options.add_argument('--no-sandbox')
# # prefs = {'profile.managed_default_content_settings.images': 2}
# # chrome_options.add_experimental_option('prefs', prefs)
# # chrome_options.add_argument('--blink-settings=imagesEnabled=false')
# # chrome_options.add_argument('--disable-dev-shm-usage')
# # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# # driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_options=chrome_options)
# # driver.implicitly_wait(2)  # seconds
#
# # available_timetable 변수를 받기 위한 전역변수
# available_timetable = ""
# available_time_list=[]
#
# def show_studyroom_timetable(room_num):
#     print("start b")
#     global available_timetable
#     global available_time_list
#     print("start")
#     plu.driver.get("https://ari.anyang.ac.kr/sso/index.jsp")
#     #time.sleep(2)
#     plu.driver.implicitly_wait(10) # seconds
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
#     print(plu.driver.current_url)
#
#     plu.driver.get("https://ari.anyang.ac.kr/user/jobcafe/index.do?code=00" + room_num)
#     plu.driver.implicitly_wait(10) # seconds
#     # print("studyroom페이지 접속")
#     print(plu.driver.current_url)
#
#     # 시간표가 나와있는 div
#     time_div = plu.driver.find_element(plu.By.CSS_SELECTOR, "div.tabType05.mt15.time-select")
#
#     # 선택 가능한 시간표 리스트
#     time_li_list = time_div.find_elements(plu.By.CSS_SELECTOR, 'li:not(.dsb)')
#
#     available_time_list=[]
#     cnt=0
#     for li in time_li_list:
#         available_timetable = li.find_element(plu.By.CSS_SELECTOR, 'label')
#         print(available_timetable.text)
#         available_time_list.append(available_timetable)
#         cnt+=1
#
#     return cnt
































