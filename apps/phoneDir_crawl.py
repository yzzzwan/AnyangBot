from selenium import webdriver
from selenium.webdriver.common.by import By

# local
# driver = webdriver.ChromeOptions()
# driver.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver.Chrome('C:\\Users\\kyw01\\Downloads\\chromedriver_win32\\chromedriver')
# driver.get('https://www.anyang.ac.kr/main/introduction/anyang-campus001.do')
# #time.sleep(1)


#server
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=chrome_options)
driver.get('https://www.anyang.ac.kr/main/introduction/anyang-campus001.do')
# time.sleep(1)

# dept1 = soup.select(".tit01")
# dept2 = soup.select("h4.tit02")


dept1 = driver.find_elements(By.CSS_SELECTOR, ".tit01")
dept2 = driver.find_elements(By.CSS_SELECTOR, "h4.tit02")

# 부서 이름 저장
depts = dept1[2:9] + dept2[:8] +dept1[11:13] + dept2[8:]


def find_dept(cmd):
    cnt = 0

    # 부서 찾기
    for dept in depts:
        if dept.text == cmd:
            break
        cnt += 1

    # phone book 전체 data
    # data = soup.select(".board-table > tbody")
    data = driver.find_elements(By.CSS_SELECTOR, ".board-table > tbody")

    # for d in data:
    #     print(d.text)
    #     print("@"*10)

    #print(data[cnt].text)
    # print(type(data))
    # print(cnt)
    # print(depts[cnt])

    # 선택한 부서의 튜플들
    # trs = data[cnt].select("tr")
    trs = data[cnt].find_elements(By.CSS_SELECTOR, "tr")

    dept_phoneBook = ""
    for tr in trs:
        # tds = tr.select("td")
        tds = tr.find_elements(By.CSS_SELECTOR, "td")

        # 부서의 세부부서 이름
        # dept_name = tds[0].get_text()
        dept_name = tds[0].text

        # 세부부서의 위치/업무
        # dept_service_pos = tds[1].get_text()
        dept_service_pos = tds[1].text

        # 세부부서의 전화번호
        # dept_phone = tds[2].get_text()
        dept_phone = tds[2].text

        # 빈칸 빈칸 data
        if len(dept_name) == 0 and len(dept_service_pos) == 0:
            dept_phoneBook += dept_phone + ". "

        # 빈칸 data 빈칸
        elif len(dept_name) == 0 and len(dept_phone) == 0:
            dept_phoneBook += dept_service_pos + ". "


        # 빈칸 data data
        elif len(dept_name) == 0:
            dept_phoneBook += "\n" + dept_service_pos + " : " + dept_phone + ". "


        # 첫칸이 괄호로 시작할 때
        elif dept_name[0] == '(':
            dept_service_pos += dept_name
            dept_phoneBook += "\n" + dept_service_pos + " : " + dept_phone + ". "


        # data 빈칸 data
        elif len(dept_service_pos) == 0 and len(dept_name) != 0 and len(dept_phone) != 0:
            dept_phoneBook += "\n" + "\n" + "[" + dept_name + "]" + "\n" + dept_phone + ". "

        # data data data
        else:
            dept_phoneBook += "\n" + "\n" + "[" + dept_name + "]" + "\n" + dept_service_pos + " : " + dept_phone + ". "
    notice = "※ 700~900번대 : 031-467-0___\n※ 100~300번대 : 031-463-1___\n==========================\n"
    dept_phoneBook = notice + dept_phoneBook[2:]
    print(dept_phoneBook)
    return dept_phoneBook



# for dept in depts:
#     if dept.get_text() == cmd:
#         select_dept = dept
#         break
#     cnt+=1
#
# data = soup.select(".board-table > tbody")
# #print(type(data))
# #print(cnt)
# #print(depts[cnt])
# trs = data[cnt].select("tr")
# dept_phoneBook = ""
# for tr in trs:
#     tds = tr.select("td")
#     dept_name = tds[0].get_text()
#
#     dept_service_pos = tds[1].get_text()
#     dept_phone = tds[2].get_text()
#
#     # 빈칸 빈칸 data
#     if len(dept_name) == 0 and len(dept_service_pos) == 0:
#         print(dept_phone + ". ", end="")
#         dept_phoneBook += dept_phone + ". "
#
#     # 빈칸 data 빈칸
#     elif len(dept_name) == 0 and len(dept_phone) == 0:
#         print(dept_service_pos + ". ", end="")
#         dept_phoneBook += dept_service_pos + ". "
#
#
#     # 빈칸 data data
#     elif len(dept_name) == 0 :
#         print()
#         print(dept_service_pos + " : ", end="")
#         print(dept_phone + ". ", end="")
#         dept_phoneBook += "\n" + dept_service_pos + " : " + dept_phone + ". "
#
#
#     # 첫칸이 괄호로 시작할 때
#     elif dept_name[0] == '(':
#         print()
#         dept_service_pos += dept_name
#         print(dept_service_pos + " : ", end="")
#         print(dept_phone + ". ", end="")
#         dept_phoneBook += "\n" + dept_service_pos + " : " + dept_phone + ". "
#
#
#     # data 빈칸 data
#     elif len(dept_service_pos) == 0 and len(dept_name) != 0 and len(dept_phone) !=0:
#         print()
#         print()
#         print("[" + dept_name + "]")
#         print(dept_phone + ". ", end="")
#         dept_phoneBook += "\n" + "\n" + "[" + dept_name + "]" + "\n" + dept_phone + ". "
#
#     # data data data
#     else :
#         print()
#         print()
#         print("[" + dept_name + "]")
#         print(dept_service_pos + " : ", end="")
#         print(dept_phone + ". ",  end="")
#         dept_phoneBook += "\n" + "\n" + "[" + dept_name + "]" + "\n" + dept_service_pos + " : " + dept_phone + ". "
#
#
# print("@@@@@")
# print(dept_phoneBook)


#빈칸 빈칸 데이터 = 윗줄 3칸이랑 합치기 @
#빈칸 데이터 빈칸 ==@

#빈칸 데이터 데이터 = 부서인데 업무가 다른거@

#데이터 빈칸 데이터@

#첫칸 데이터가 괄호로 시작하면 두번쨰칸이랑뒤에 합성@

