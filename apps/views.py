from django.shortcuts import render
from django.http import HttpResponse
from . import haksik_crawl
from . import phoneDir_crawl as pdc
# import test2
# from test2 import portal

from django.http import request as json
# Create your views here.
# def index(request):
#     return render(request, "apps/index.html")

def test(request):
     return HttpResponse(haksik_crawl.menu_list)


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

    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [{
                'simpleText': {
                    'text': haksik_crawl.week_menu
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

    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [{
                'simpleText': {
                    'text': haksik_crawl.today_menu
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



# @csrf_exempt
# def portal_login(request):
#     answer = ((request.body).decode('utf-8'))
#     json_str = json.loads(answer)
#
#     Pid = json_str['action']['params']['portal_ID']
#     Ppw = json_str['action']['params']['portal_PW']
#     print("😀")
#     login = portal(Pid, Ppw)
#     print("🥰")
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


