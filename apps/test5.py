# from . import studyroom_Timetable as st
# from . import portal_login_user as plu
# import time
# def test():
#     return "test"
#
# def selfroom_reserve(idx):
#     s = "f"
#     # 시간 선택
#     st.available_time_list_tag[idx].click()
#     # 신청 버튼 클릭
#     plu.driver.find_element(plu.By.CSS_SELECTOR, "a.btn02.green01.hv01").click()
#     time.sleep(1)
#
#     #print(driver.current_url)
#
#     win = plu.driver.window_handles
#     #print(win)
#
#     # 신청 팝업 창으로 이동
#     plu.driver.switch_to.window(win[1])
#
#     input_member = plu.driver.find_element("name", "mem")
#
#     # 사용인원 입력
#     input_member.send_keys("1")
#
#     # 신청사유
#     reason = "공부"
#
#     input_reason = plu.driver.find_element("name", "reason")
#
#     # 신청사유 입력
#     input_reason.send_keys(reason)
#
#     # 동의 체크박스 클릭
#     plu.driver.find_element("id", "agree").click()
#
#     # 완료 버튼 클릭
#     plu.driver.find_element(plu.By.CSS_SELECTOR, "a.btn02.green01.hv01").click()
#
#     time.sleep(1)
#
#     # 저장하시겠습니까? 확인버튼
#     plu.Alert(plu.driver).accept()
#     time.sleep(1)
#
#     if plu.Alert(plu.driver).text == "저장되었습니다.":
#         # 저장되었습니다. 확인버튼
#         plu.Alert(plu.driver).accept()
#         s = "s"
#
#     else:
#         # 예약은 1일 최대 2시간까지 가능합니다. 확인버튼
#         plu.Alert(plu.driver).accept()
#         s="d"
#
#
#
#     # plu.quit()
#
#
#     # s= "f"  실패
#     # s= "s"  성공
#     # s= "d"  실패(예약횟수 초과)
#
#     return s