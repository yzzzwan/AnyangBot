# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# chrome_options = webdriver.ChromeOptions()
#
# # chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_options=chrome_options)
# driver.implicitly_wait(3)  # seconds
#
#
# def t(a, b):
#     s=a+b
#     return s
#
# # 줄 마다 return 해서 return 되는지 test해보기 time으로 시간측정
#
# # 포탈 로그인
# def portal(pid, ppw):
#     print("포탈 접속 시도")
#     driver.get("https://portal.anyang.ac.kr/")
#     driver.implicitly_wait(2)  # seconds
#
#     ## test
#
#     print("start")
#     start = time.time()
#
#     success = "f"
#
#     print("포탈 접속")
#
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
#     #test
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
#         WebDriverWait(driver, 0.6).until(EC.alert_is_present())
#         alert = driver.switch_to.com
#         alert.accept()
#
#     except:
#         pass
#
#     ## test
#
#     # 로그인 완료되면 포탈페이지로 이동
#     if driver.current_url == "https://portal.anyang.ac.kr/#":
#         print("포탈 로그인 실패!")
#         driver.quit()
#         return success
#
#     else:
#         print("포탈 로그인 성공!")
#
#
#     # print("포폴 접속시도")
#     end = time.time()
#     print("login :", end - start)
#     success="s"
#     driver.quit()
#     return success
#
# # portal("2020E7011","rladyddhks1!")