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

from . import lost_and_found

# 분실물 찾기
@csrf_exempt
def lost_found(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance'] # 사용자의 발화 텍스트

    links = lost_and_found.lost_items_list()
    lost_items = lost_and_found.lost_item_detail(links)

    return JsonResponse({
          "version": "2.0",
          "template": {
            "outputs": [
              {
                "listCard": {
                  "header": {
                    "title": "안양대 분실물 센터"
                  },
                  "items": [
                      {
                          "title": lost_items[0][0] + ") " + lost_items[0][2],
                          "description": lost_items[0][1] + "에서 발견함.",
                          "action": "block",
                          "blockId": "6453e24cff276f32961c361c",
                          "extra": {
                              "num": 0,
                          }
                      },
                      {
                          "title": lost_items[1][0] + ") " + lost_items[1][2],
                          "description": lost_items[1][1] + "에서 발견함.",
                          "action": "block",
                          "blockId": "6453e24cff276f32961c361c",
                          "extra": {
                              "num": 1,
                          }

                      },
                      {
                          "title": lost_items[2][0] + ") " + lost_items[2][2],
                          "description": lost_items[2][1] + "에서 발견함.",
                          "action": "block",
                          "blockId": "6453e24cff276f32961c361c",
                          "extra": {
                              "num": 2,
                          }

                      },
                      {
                          "title": lost_items[3][0] + ") " + lost_items[3][2],
                          "description": lost_items[3][1] + "에서 발견함.",
                          "action": "block",
                          "blockId": "6453e24cff276f32961c361c",
                          "extra": {
                              "num": 3,
                          }

                      },
                      {
                          "title": lost_items[4][0] + ") " + lost_items[4][2],
                          "description": lost_items[4][1] + "에서 발견함.",
                          "action": "block",
                          "blockId": "6453e24cff276f32961c361c",
                          "extra": {
                              "num": 4,
                          }


                      },
                  ],
                  "buttons": [
                    {
                      "label": "더보기",
                      "action": "webLink",
                      "webLinkUrl": "https://www.anyang.ac.kr/main/communication/lost-found.do"
                    }
                  ]
                }
              }
            ]
          }
        })


# 분실물 정보 자세히
@csrf_exempt
def lost_found_detail(request):
    answer = ((request.body).decode('utf-8'))
    json_str = json.loads(answer)
    num = int(json_str['action']['clientExtra']['num'])

    links = lost_and_found.lost_items_list()
    lost_items = lost_and_found.lost_item_detail(links)

    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [{
                'simpleText': {
                    'text': lost_items[num][0] + ", " + lost_items[num][1] + "에서 " + lost_items[num][3] + "이(가) " +
                            lost_items[num][2] + "을(를) 습득하여 " + lost_items[num][4] + "에서 보관중입니다."
                }
            }],
            'quickReplies': [{
                'label': '학생지원과 연락처',
                'action': 'message',
                'messageText': '학생지원처',
            }]
        }
    })

from . import portal_login_user

# 포탈 로그인
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

from . import studyroom_Timetable
# from . import a

# 셀프학습실 이용가능 시간표 출력
@csrf_exempt
def selfroom_timetable(request):
    answer = ((request.body).decode('utf-8'))
    json_str = json.loads(answer)

    room_num = str(json_str['action']['clientExtra']['room_num'])
    available_Time = studyroom_Timetable.show_studyroom_timetable(room_num)

    room_names = ["Self 학습실1(Career design)", "Self 학습실2(Thinking design)", "Self 학습실3(Life story design)",
                  "Self 학습실4", "Self 학습실5", "Self 학습실6", "Self 학습실7-1", "Self 학습실7-2", "Self 학습실8-1",
                  "Self 학습실8-1"]

    room_num = int(room_num) - 1
    room_name = room_names[room_num]

    return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "listCard": {
                            "header": {
                                "title": room_name + "의 이용 가능 시간표"
                            },
                            "items": [
                                {
                                    "title": available_Time[0],
                                    "description": "원하는 사용시간을 선택해주세요.",

                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    "extra": {
                                        "num": 0,
                                        "room": room_name
                                    }

                                },

                                {
                                    "title": available_Time[1],
                                    "description": "원하는 사용시간을 선택해주세요.",

                                                                        "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    "extra": {
                                        "num": 1,
                                        "room": room_name
                                    }

                                },

                                {
                                    "title": available_Time[2],
                                    "description": "원하는 사용시간을 선택해주세요.",

                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    "extra": {
                                    "num": 2,
                                    "room": room_name
                                }

                                },

                                {
                                    "title": available_Time[3],
                                    "description": "원하는 사용시간을 선택해주세요.",

                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    "extra": {
                                    "num": 3,
                                    "room": room_name
                                }


                                },

                                {
                                    "title": available_Time[4],
                                    "description": "원하는 사용시간을 선택해주세요.",

                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    "extra": {
                                        "num": 4,
                                    "room": room_name
                                }
                                },
                            ],
                        }
                    },
                    {
                        "listCard": {
                            "header": {
                                "title": room_name + "의 이용 가능 시간표"
                            },
                            "items": [
                                {
                                    "title": available_Time[5],
                                    "description": "원하는 사용시간을 선택해주세요.",

                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    "extra": {
                                        "num": 5,
                                    "room": room_name
                                }
                                },

                                {
                                    "title": available_Time[6],
                                    "description": "원하는 사용시간을 선택해주세요.",

                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    "extra": {
                                        "num": 6,
                                    "room": room_name
                                }
                                },

                                {
                                    "title": available_Time[7],
                                    "description": "원하는 사용시간을 선택해주세요.",
                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    "extra": {
                                        "num": 7,
                                    "room": room_name
                                }
                                },

                                {
                                    "title": available_Time[8],
                                    "description": "원하는 사용시간을 선택해주세요.",

                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    "extra": {
                                        "num": 8,
                                    "room": room_name
                                }
                                },

                                {
                                    "title": available_Time[9],
                                    "description": "원하는 사용시간을 선택해주세요.",

                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    "extra": {
                                        "num": 9,
                                    "room": room_name
                                }
                                },
                            ],
                        }
                    },
                    {
                        "listCard": {
                            "header": {
                                "title": room_name + "의 이용 가능 시간표"
                            },
                            "items": [
                                {
                                    "title": available_Time[10],
                                    "description": "원하는 사용시간을 선택해주세요.",

                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    "extra": {
                                        "num": 10,
                                    "room": room_name
                                }
                                },

                                {
                                    "title": available_Time[11],
                                    "description": "원하는 사용시간을 선택해주세요.",
                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    "extra": {
                                        "num": 11,
                                    "room": room_name
                                }
                                },

                                {
                                    "title": available_Time[12],
                                    "description": "원하는 사용시간을 선택해주세요.",
                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    "extra": {
                                        "num": 12,
                                    "room": room_name
                                }
                                },
                            ],
                        }
                    },

                ],
            }
        })


# 셀프학습실 예약 final check 질문
@csrf_exempt
def studyRoom_final_check(request):
    answer = ((request.body).decode('utf-8'))
    json_str = json.loads(answer)

    idx = int(json_str['action']['clientExtra']['num'])
    room = str(json_str['action']['clientExtra']['room'])
    select_time = studyroom_Timetable.available_time_list_tag[idx].text
    # 9:00 ~ 10:00에 self 학습실 1를 예약하시겠습니까?

    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [{
                'simpleText': {
                    'text': "(" + select_time + ")" + "에 "+room + "을(를) 예약하시겠습니까?"
                }
            }],
            'quickReplies': [
                {
                    "label": "네",
                    "action": "block",
                    "messageText": "예약하겠습니다.",
                    'blockId': '6457acc18edae924e926b707',
                    "extra": {
                        "num": idx,
                    }

                },

                {
                    "label": "다시 선택",
                    "action": "block",
                    "messageText": "다시 선택할게요.",
                    'blockId': '6435ac1770eb005cb17a7588'

                },

                {
                    "label": "종료하기",
                    "action": "block",
                    "messageText": "self 학습실 예약을 종료합니다.",
                    'blockId': '6435ac1770eb005cb17a7588'

                },
            ],
        }
    })

from . import studyRoom_reserve

# self 학습실 예약
@csrf_exempt
def studyRoom_reserve(request):
    answer = ((request.body).decode('utf-8'))
    json_str = json.loads(answer)

    # idx = int(json_str['action']['clientExtra']['num'])
    # sucess = studyRoom_reserve.selfroom_reserve(idx)
    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [{
                'simpleText': {
                    'text': str(json_str)
                }
            }]
        }
    })

# # 셀프학습실 timetable
# @csrf_exempt
# def selfroom_timetable(request):
#     answer = ((request.body).decode('utf-8'))
#     json_str = json.loads(answer)
#
#     room_num = str(json_str['action']['clientExtra']['room_num'])
#     # available_Time = studyroom_Timetable.show_studyroom_timetable(room_num)
#     #  아이디 입력 함수 어떻게 해결했는지 참고해서 해결하기. 윗함수실행시키면 타임오바
#
#     return JsonResponse({
#         'version': "2.0",
#         'template': {
#             'outputs': [{
#                 'simpleText': {
#                     'text': room_num
#                 }
#             }]
#         }
#     })
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








