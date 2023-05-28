# import time
#
# import portal_login_user as plu
# # from . import portal_login_user as plu
#
#
# # available_timetable 변수를 받기 위한 전역변수
# # available_timetable = ""
# available_time_list_tag = []
#
#
# def show_studyroom_timetable(room_num):
#     tt=""
#     print("start b")
#     # global available_timetable
#     global available_time_list_tag
#
#     print("start")
#     plu.driver.get("https://ari.anyang.ac.kr/sso/index.jsp")
#     plu.driver.implicitly_wait(10) # seconds
#
#
#     print(plu.driver.current_url)
#
#     plu.driver.get("https://ari.anyang.ac.kr/user/jobcafe/index.do?code=0" + room_num)
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
#     available_time_list = []
#     available_time_list_tag = []
#
#
#     for li in time_li_list:
#         available_timetable = li.find_element(plu.By.CSS_SELECTOR, 'label')
#         #print(available_timetable.text)
#         available_time_list_tag.append(available_timetable)
#         available_time_list.append(available_timetable.text)
#
#         # tt+=available_timetable.text+"\n"
#
#     # 9시부터 22시 까지의 13시 타임들 중에서 사용 중인 시간대들은 - 로 표시.
#     for i in range(len(available_time_list), 13):
#         available_time_list_tag.append("-")
#         available_time_list.append("-")
#
#     return available_time_list
#
#
#
#






import datetime

import time

# import portal_login_user as plu
# import choose_date as cd
from . import portal_login_user as plu
from . import choose_date as cd




# available_timetable 변수를 받기 위한 전역변수
# available_timetable = ""
available_time_list_tag = []


def show_studyroom_timetable(room_num, weekday):
    days = cd.five_days()

    tt=""
    print("start b")
    # global available_timetable
    global available_time_list_tag

    print("start")

    # 아리포트폴리오 페이지로 이동
    plu.driver.get("https://ari.anyang.ac.kr/sso/index.jsp")
    plu.driver.implicitly_wait(10)  # seconds

    print(plu.driver.current_url)

    # study room 예약 페이지로 이동
    plu.driver.get("https://ari.anyang.ac.kr/user/jobcafe/index.do?code=0" + room_num)
    plu.driver.implicitly_wait(10) # seconds
    # print("studyroom페이지 접속")
    print(plu.driver.current_url)


    # 일이 10일 보다 작으면 앞에 0 제거. 월이 10월보다 작으면 앞에 0 제거
    d = days[weekday * 2]
    month = d[5:7]
    date = d[8:10]

    if (int(month) < 10):
        month = str(int(month))

    if (int(date) < 10):
        date = str(int(date))

    css_selector = f'td[data-date="{date}"][data-month="{month}"]'

    # 선택한 날짜 태그 선택
    today_div = plu.driver.find_element(plu.By.CSS_SELECTOR, css_selector)

    # print(today_div.text)

    # 선택한 날짜 클릭
    today_div.click()

    # 시간표가 나와있는 div
    time.sleep(0.3)
    time_div = plu.driver.find_element(plu.By.CSS_SELECTOR, "div.tabType05.mt15.time-select")

    # 해당 날짜의 예약 가능 시간 가져오기
    # 선택 가능한 시간표 리스트
    time_li_list = time_div.find_elements(plu.By.CSS_SELECTOR, 'li:not(.dsb)')

    available_time_list = []
    available_time_list_tag = []

    # print(time_li_list)

    for li in time_li_list:
        available_timetable = li.find_element(plu.By.CSS_SELECTOR, 'label')
        #print(available_timetable.text)
        available_time_list_tag.append(available_timetable)
        available_time_list.append(available_timetable.text)

        # tt+=available_timetable.text+"\n"

    # 9시부터 22시 까지의 13시 타임들 중에서 사용 중인 시간대들은 - 로 표시.
    for i in range(len(available_time_list), 13):
        available_time_list_tag.append("-")
        available_time_list.append("-")

    return available_time_list




