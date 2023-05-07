# import portal_login_user as plu

from . import portal_login_user as plu


# available_timetable 변수를 받기 위한 전역변수
# available_timetable = ""
# available_time_list=[]

def test():
    return "hi"
#
def show_studyroom_timetable(room_num):
    tt=""
    print("start b")
    # global available_timetable
    # global available_time_list

    print("start")
    plu.driver.get("https://ari.anyang.ac.kr/sso/index.jsp")
    plu.driver.implicitly_wait(10) # seconds


    print(plu.driver.current_url)

    plu.driver.get("https://ari.anyang.ac.kr/user/jobcafe/index.do?code=0" + room_num)
    plu.driver.implicitly_wait(10) # seconds
    # print("studyroom페이지 접속")
    print(plu.driver.current_url)

    # 시간표가 나와있는 div
    time_div = plu.driver.find_element(plu.By.CSS_SELECTOR, "div.tabType05.mt15.time-select")

    # 선택 가능한 시간표 리스트
    time_li_list = time_div.find_elements(plu.By.CSS_SELECTOR, 'li:not(.dsb)')

    available_time_list=[]
    for li in time_li_list:
        available_timetable = li.find_element(plu.By.CSS_SELECTOR, 'label')
        #print(available_timetable.text)
        available_time_list.append(available_timetable)
        # tt+=available_timetable.text+"\n"

    return available_time_list






















