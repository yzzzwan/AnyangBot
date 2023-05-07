from . import studyroom_Timetable as st
from . import portal_login_user as plu
import time
def test():
    return "test"

def selfroom_reserve(idx):
    s = "f"
    # 시간 선택
    st.available_time_list_tag[idx].click()
    # 신청 버튼 클릭
    plu.driver.find_element(plu.By.CSS_SELECTOR, "a.btn02.green01.hv01").click()
    time.sleep(1)

    #print(driver.current_url)

    win = plu.driver.window_handles
    #print(win)

    # 신청 팝업 창으로 이동
    plu.driver.switch_to.window(win[1])

    input_member = plu.driver.find_element("name", "mem")

    # 사용인원 입력
    input_member.send_keys("1")

    # 신청사유
    reason = "공부"

    input_reason = plu.driver.find_element("name", "reason")

    # 신청사유 입력
    input_reason.send_keys(reason)

    # 동의 라벨 클릭
    plu.driver.find_element("id", "agree").click()

    # 완료 버튼 클릭
    plu.driver.find_element(plu.By.CSS_SELECTOR, "a.btn02.green01.hv01").click()

    time.sleep(1)

    plu.Alert(plu.driver).accept()

    s = "s"
    return s