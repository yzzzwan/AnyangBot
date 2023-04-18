from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

import time

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
prefs = {'profile.managed_default_content_settings.images': 2}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_options=chrome_options)
driver.implicitly_wait(2)  # seconds

# 줄 마다 return 해서 return 되는지 test해보기 time으로 시간측정

# 포탈 로그인
def portal(pid, ppw):

    print("포탈 접속 시도")
    driver.get("https://portal.anyang.ac.kr/")
    driver.implicitly_wait(1)  # seconds
    print("start")

    success = "f"


    print("포탈 접속")

    # 로그인 페이지에 접속했는데 이미 (앞 유저의)로그인되어 있는 경우
    if driver.current_url =='https://portal.anyang.ac.kr/c/portal/login_event':
        # 쿠키를 삭제합니다
        driver.delete_all_cookies()

        # 포탈 페이지를 새로고칩니다
        driver.get("https://portal.anyang.ac.kr/")


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
        WebDriverWait(driver, 0.6).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()

    except:
        pass

    # 같은 계정으로 이미 로그인 되어있습니다. \n로그인 되어있던 계정은 로그아웃됩니다.
    try:
        WebDriverWait(driver, 0.6).until(EC.alert_is_present())
        alert = driver.switch_to.com
        alert.accept()

    except:
        pass


    # 로그인 완료되면 포탈페이지로 이동
    if driver.current_url == "https://portal.anyang.ac.kr/#":
        print("포탈 로그인 실패!")
        return success

    else:
        print("포탈 로그인 성공!")


    success="s"
    # time.sleep(1)

    return success


# a=time.time()
# a=portal("2020E7011","rladyddhks1!")
# print(a)

# b=time.time()
# print(b-a)

# a=portal("2020E7011","rladddhks1!")
# a=portal("2020E7011","rladyddhks1!")
#
# b=portal("2020E7011","rladyddhks1!")


