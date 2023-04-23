from django.shortcuts import render
from django.http import HttpResponse
from . import haksik_crawl
from . import phoneDir_crawl as pdc
# from . import test2
from django.http import request as json

# Create your views here.
# def index(request):
#     return render(request, "apps/index.html")

# def test(request):
#      return HttpResponse(haksik_crawl.menu_list)


def index(request):
    return render(request, "apps/index.html")


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# test
@csrf_exempt
def message(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    if return_str == '테스트':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': "테스트입니다!"
                    }
                }],
                'quickReplies': [{
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                }]
            }
        })

# 주간 급식 출력
@csrf_exempt
def week_haksik(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance'] # 사용자의 발화 텍스트

    week_haksik_menu = haksik_crawl.print_week_haksik()

    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [{
                'simpleText': {
                    'text': week_haksik_menu

                }
            }],
        }
    })

# 오늘 급식 출력
@csrf_exempt
def today_haksik(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance'] # 사용자의 발화 텍스트

    today_haksik_menu = haksik_crawl.print_today_haksik()

    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [{
                'simpleText': {
                    'text': today_haksik_menu

                }
            }]
        }
    })

# 전화번호부
@csrf_exempt
def phoneDir(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance'] # 사용자의 발화 텍스트
    phoneBook = pdc.find_dept(return_str)
    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [{
                'simpleText': {
                    'text': phoneBook
                }
            }]
        }
    })



from . import portal_login_user

@csrf_exempt
def portal_login(request):
    answer = ((request.body).decode('utf-8'))
    json_str = json.loads(answer)

    Pid = str(json_str['action']['params']['portal_ID'])
    Ppw = str(json_str['action']['params']['portal_PW'])

    login = portal_login_user.portal(Pid, Ppw)

    if login == 's':
        return JsonResponse({
                'version': "2.0",
                'template': {
                    'outputs': [{
                        'simpleText': {
                            'text': "로그인에 성공했습니다.\n self-학습실 선택하기 버튼을 눌러주세요."
                       }
                    }],
                    'quickReplies': [{
                        'label': 'self-학습실 선택하기',
                        'action': 'block',
                        'messageText': '다시 시도하기',
                        'blockId' : '6435ac1770eb005cb17a7588'
                    }]
                }
            })

    else:
        return JsonResponse({
                'version': "2.0",
                'template': {
                    'outputs': [{
                        'simpleText': {
                            'text': '입력하신 아이디 혹은 비밀번호가 일치하지 않습니다.\n 다시 시도하려면 "다시 시도"버튼을 눌러주세요.'
                       }
                    }],
                    'quickReplies': [{
                        'label': '다시 시도하기',
                        'action': 'block',
                        'messageText': '다시 시도하기',
                        'blockId' : '6435adf77ab7b038704cebf7'
                    }]
                }
            })

# from . import studyroom_Timetable
# from . import a

# 셀프학습실 timetable
@csrf_exempt
def selfroom_timetable(request):
    answer = ((request.body).decode('utf-8'))
    json_str = json.loads(answer)

    room_num = str(json_str['action']['clientExtra']['room_num'])
    # available_Time = studyroom_Timetable.show_studyroom_timetable(room_num)
    #  아이디 입력 함수 어떻게 해결했는지 참고해서 해결하기. 윗함수실행시키면 타임오바


    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [{
                'simpleText': {
                    'text': room_num
                }
            }]
        }
    })
## 다른 학습실 보기 버튼
## 출력은 리스트 버튼으로
## 리스트 버튼 클릭 시 예약하겠습니까 버튼.



# @csrf_exempt
# def studyRoom_reserve(request):
#     answer = ((request.body).decode('utf-8'))
#     json_str = json.loads(answer)
#
#     id = json_str['action']['params']['portal_ID']
#     pw = json_str['action']['params']['portal_PW']
#
#     t = test2.pl(id, pw)
#
#
#     if t=="s":
#         return JsonResponse({
#                 'version': "2.0",
#                 'template': {
#                     'outputs': [{
#                         'simpleText': {
#                             'text': 'yes'
#                        }
#                     }]
#                 }
#             })
#     else:
#         return JsonResponse({
#                 'version': "2.0",
#                 'template': {
#                     'outputs': [{
#                         'simpleText': {
#                             'text': 'no'
#                        }
#                     }]
#                 }
#             })









# @csrf_exempt
# def portal_login(request):
#     answer = ((request.body).decode('utf-8'))
#     json_str = json.loads(answer)
#
#     Pid = json_str['action']['params']['portal_ID']
#     Ppw = json_str['action']['params']['portal_PW']
#
#     login = test2.portal(Pid, Ppw)
#
#     if login == 's':
#         return JsonResponse({
#                 'version': "2.0",
#                 'template': {
#                     'outputs': [{
#                         'simpleText': {
#                             'text': "login success"
#                        }
#                     }]
#                 }
#             })
#
#     else:
#         return JsonResponse({
#                 'version': "2.0",
#                 'template': {
#                     'outputs': [{
#                         'simpleText': {
#                             'text': "login fail"
#                        }
#                     }]
#                 }
#             })


# # self 학습실 시간표 보여주기
# @csrf_exempt
# def studyRoom_timetable(request):
#     answer = ((request.body).decode('utf-8'))
#     json_str = json.loads(answer)
#     room_num = str(json_str['contexts'][1]['params']['room_num']['value']) # 룸 번호
#
#     available_time = test2.ari(room_num)
#
#     # portal_id = json_str['contexts'][0]['params']['portal_id']['value']
#     # portal_pw = c
#     # portal_id = json_str['contexts'][0]['params']['portal_id']
#     # portal_pw = json_str['contexts'][0]['params']['portal_pw']
#
#     return JsonResponse({
#         'version': "2.0",
#         'template': {
#             'outputs': [{
#                 'simpleText': {
#                     'text':  available_time# 리스트를 문자열 식으로 받아와서 출력
#                 }
#             }]
#         }
#     })








# # self 학습실 예약하기
# @csrf_exempt
# def studyRoom_reserve(request):
#     answer = ((request.body).decode('utf-8'))
#     json_str = json.loads(answer)
#     time_select = int(json_str['contexts'][1]['params']['time_select']['value']) # 선택한 시간대
#     done = test2.reserve(time_select)
#
#     if done == 'done':
#         return JsonResponse({
#                 'version': "2.0",
#                 'template': {
#                     'outputs': [{
#                         'simpleText': {
#                             'text': "reserve success"
#                        }
#                     }]
#                 }
#             })
#
#     else:
#         return JsonResponse({
#                 'version': "2.0",
#                 'template': {
#                     'outputs': [{
#                         'simpleText': {
#                             'text': "reserve fail"
#                        }
#                     }]
#                 }
#             })














# self 학습실 예약하기
# @csrf_exempt
# def studyRoom_timetable(request):
#     answer = ((request.body).decode('utf-8'))
#     json_str = json.loads(answer)
#     #return_str = json_str['contexts']['params']['portal_id']['value']  # 사용자의 발화 텍스트
#     sta = str(str(json_str['contexts'][1]['params']['portal_pw']['value']))
#
#     #json_str = str(json_str)
#     #cons=str(return_str)
#     # portal_id = json_str['contexts'][0]['params']['portal_id']['value']
#     # portal_pw = c
#     # portal_id = json_str['contexts'][0]['params']['portal_id']
#     # portal_pw = json_str['contexts'][0]['params']['portal_pw']
#
#     return JsonResponse({
#         'version': "2.0",
#         'template': {
#             'outputs': [{
#                 'simpleText': {
#                     'text': sta
#                 }
#             }]
#         }
#     })

    # if len(times) <= 5:
    #     return JsonResponse({
    #         'version': "2.0",
    #         "template": {
    #             "outputs": [
    #               {
    #                   "listCard": {
    #                   "header": {
    #                     "title": room+"의 이용 가능 시간"
    #                   },
    #                     "items": [
    #                         {
    #                             "title": test.test[0],
    #                         },
    #
    #                         {
    #                             "title": test.test[1],
    #                         },
    #
    #                         {
    #                             "title": test.test[2],
    #                         },
    #
    #                         {
    #                             "title": test.test[3],
    #                         },
    #
    #                         {
    #                             "title": test.test[4],
    #                         },
    #                     ],
    #                 }
    #               }]
    #          }
    #     })
    #
    # elif len(times) <= 10:
    #     return JsonResponse({
    #         'version': "2.0",
    #          "template": {
    #             "outputs": [
    #               {
    #                 "listCard": {
    #                   "header": {
    #                     "title": room+"의 이용 가능 시간2"
    #                   },
    #                     "items": [
    #                         {
    #                             "title": test.test[0],
    #                         },
    #
    #                         {
    #                             "title": test.test[1],
    #                         },
    #
    #                         {
    #                             "title": test.test[2],
    #                         },
    #
    #                         {
    #                             "title": test.test[3],
    #                         },
    #
    #                         {
    #                             "title": test.test[4],
    #                         },
    #
    #                         {
    #                             "title": test.test[5],
    #                         },
    #
    #                         {
    #                             "title": test.test[6],
    #                         },
    #
    #                         {
    #                             "title": test.test[7],
    #                         },
    #
    #                         {
    #                             "title": test.test[8],
    #                         },
    #
    #                         {
    #                             "title": test.test[9],
    #                         },
    #                     ],
    #
    #                 }
    #               }]
    #          }
    #     })
    #
    # else:
    #     return JsonResponse({
    #         'version': "2.0",
    #         "template": {
    #             "outputs": [
    #                 {
    #                     "listCard": {
    #                         "header": {
    #                             "title": room + "의 이용 가능 시간2"
    #                         },
    #                         "items": [
    #                             {
    #                                 "title": test.test[0],
    #                             },
    #                             {
    #                                 "title": test.test[1],
    #                             },
    #                             {
    #                                 "title": test.test[2],
    #                             },
    #                             {
    #                                 "title": test.test[3],
    #                             },
    #                             {
    #                                 "title": test.test[4],
    #                             },
    #                             {
    #                                 "title": test.test[5],
    #                             },
    #                             {
    #                                 "title": test.test[6],
    #                             },
    #                             {
    #                                 "title": test.test[7],
    #                             },
    #                             {
    #                                 "title": test.test[8],
    #                             },
    #                             {
    #                                 "title": test.test[9],
    #                             },
    #                             {
    #                                 "title": test.test[10],
    #                             },
    #                             {
    #                                 "title": test.test[11],
    #                             },
    #                             {
    #                                 "title": test.test[12],
    #                             },
    #                         ],
    #                     }
    #                 }]
    #         }
    #     })


