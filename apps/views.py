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
                    'text': lost_items[num][0] + ", " + lost_items[num][1] + "에서 " + lost_items[num][3] + "이(가) " + lost_items[num][2] + "을(를) 습득하여 " + lost_items[num][4] + "에서 보관중입니다."
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
                        'messageText': 'self-학습실 선택하기',
                        'blockId' : '6435ac1770eb005cb17a7588'
                        # [self 학습실 선택하기] 블록

                        # 'blockId' : '6469c17b318d31192baf21d2'
                        # # [self 학습실 이용 날짜 선택] 블록

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
                        # [self 학습실 ID PW 입력] 블록
                    }]
                }
            })
from . import choose_date
# self 학습실 이용일 선택
@csrf_exempt
def choose_weekday(request):
    answer = ((request.body).decode('utf-8'))
    json_str = json.loads(answer)

    room_num = str(json_str['action']['clientExtra']['room_num'])
    room_name = str(json_str['action']['clientExtra']['room_name'])

    weekdays = choose_date.five_days()

    return JsonResponse({
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "self 학습실의 이용 날짜를 선택해주세요."
                        },
                        "items": [
                            {
                                "title": weekdays[0] + " (" + weekdays[1] + ")",
                                "description": "원하는 이용 날짜를 선택해주세요.",
                                "action": "block",
                                "blockId": "6435b4bb66adba12b7012a30",
                                # [self 학습실 final check] 블록
                                "extra": {
                                    "week_day": 0,
                                    "room_num": room_num,
                                    "room_name": room_name
                                }
                            },

                            {
                                "title": weekdays[2] + " (" + weekdays[3] + ")",
                                "description": "원하는 이용 날짜를 선택해주세요.",
                                "action": "block",
                                "blockId": "6435b4bb66adba12b7012a30",
                                # [self 학습실 final check] 블록
                                "extra": {
                                    "week_day": 2,
                                    "room_num": room_num,
                                    "room_name": room_name
                                }
                            },

                            {
                                "title": weekdays[4] + " (" + weekdays[5] + ")",
                                "description": "원하는 이용 날짜를 선택해주세요.",
                                "action": "block",
                                "blockId": "6435b4bb66adba12b7012a30",
                                # [self 학습실 final check] 블록
                                "extra": {
                                    "week_day": 4,
                                    "room_num": room_num,
                                    "room_name": room_name
                                }
                            },

                            {
                                "title": weekdays[6] + " (" + weekdays[7] + ")",
                                "description": "원하는 이용 날짜를 선택해주세요.",
                                "action": "block",
                                "blockId": "6435b4bb66adba12b7012a30",
                                # [self 학습실 final check] 블록
                                "extra": {
                                    "week_day": 6,
                                    "room_num": room_num,
                                    "room_name": room_name
                                }
                            },

                            {
                                "title": weekdays[8] + " (" + weekdays[9] + ")",
                                "description": "원하는 이용 날짜를 선택해주세요.",
                                "action": "block",
                                "blockId": "6435b4bb66adba12b7012a30",
                                # [self 학습실 final check] 블록
                                "extra": {
                                    "week_day": 8,
                                    "room_num": room_num,
                                    "room_name": room_name
                                }
                            },

                        ],
                    }
                }

                        ],
        }
    })

from . import studyroom_Timetable
# 셀프학습실 이용가능 시간표 출력
@csrf_exempt
def selfroom_timetable(request):
    answer = ((request.body).decode('utf-8'))
    json_str = json.loads(answer)

    room_num = str(json_str['action']['clientExtra']['room_num'])
    room_name = str(json_str['action']['clientExtra']['room_name'])
    week_days = int(json_str['action']['clientExtra']['week_day'])

    week_day = choose_date.five_days()
    date = week_day[week_days] + " (" + week_day[week_days + 1] + ")"

    available_Time = studyroom_Timetable.show_studyroom_timetable(room_num, week_days)


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
                                    # [self 학습실 final check] 블록
                                    "extra": {
                                        "idx": 0,
                                        "room": room_name,
                                        "date": date
                                    }

                                },

                                {
                                    "title": available_Time[1],
                                    "description": "원하는 사용시간을 선택해주세요.",

                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    # [self 학습실 final check] 블록

                                    "extra": {
                                        "idx": 1,
                                        "room": room_name,
                                        "date": date
                                    }

                                },

                                {
                                    "title": available_Time[2],
                                    "description": "원하는 사용시간을 선택해주세요.",

                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    # [self 학습실 final check] 블록

                                    "extra": {
                                        "idx": 2,
                                        "room": room_name,
                                        "date": date
                                }

                                },

                                {
                                    "title": available_Time[3],
                                    "description": "원하는 사용시간을 선택해주세요.",

                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    # [self 학습실 final check] 블록

                                    "extra": {
                                        "idx": 3,
                                        "room": room_name,
                                        "date": date
                                }


                                },

                                {
                                    "title": available_Time[4],
                                    "description": "원하는 사용시간을 선택해주세요.",

                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    # [self 학습실 final check] 블록

                                    "extra": {
                                        "idx": 4,
                                        "room": room_name,
                                        "date": date
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
                                    # [self 학습실 final check] 블록

                                    "extra": {
                                        "idx": 5,
                                        "room": room_name,
                                        "date": date
                                }
                                },

                                {
                                    "title": available_Time[6],
                                    "description": "원하는 사용시간을 선택해주세요.",

                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    # [self 학습실 final check] 블록

                                    "extra": {
                                        "idx": 6,
                                        "room": room_name,
                                        "date": date
                                }
                                },

                                {
                                    "title": available_Time[7],
                                    "description": "원하는 사용시간을 선택해주세요.",
                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    # [self 학습실 final check] 블록

                                    "extra": {
                                        "idx": 7,
                                        "room": room_name,
                                        "date": date
                                }
                                },

                                {
                                    "title": available_Time[8],
                                    "description": "원하는 사용시간을 선택해주세요.",

                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    # [self 학습실 final check] 블록

                                    "extra": {
                                        "idx": 8,
                                        "room": room_name,
                                        "date": date
                                }
                                },

                                {
                                    "title": available_Time[9],
                                    "description": "원하는 사용시간을 선택해주세요.",

                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    # [self 학습실 final check] 블록

                                    "extra": {
                                        "idx": 9,
                                        "room": room_name,
                                        "date": date
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
                                    # [self 학습실 final check] 블록

                                    "extra": {
                                        "idx": 10,
                                        "room": room_name,
                                        "date": date
                                }
                                },

                                {
                                    "title": available_Time[11],
                                    "description": "원하는 사용시간을 선택해주세요.",
                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    # [self 학습실 final check] 블록

                                    "extra": {
                                        "idx": 11,
                                        "room": room_name,
                                        "date": date
                                }
                                },

                                {
                                    "title": available_Time[12],
                                    "description": "원하는 사용시간을 선택해주세요.",
                                    "action": "block",
                                    "blockId": "645794dfa58bfd17ce539370",
                                    # [self 학습실 final check] 블록

                                    "extra": {
                                        "idx": 12,
                                        "room": room_name,
                                        "date": date
                                }
                                },
                            ],
                        }
                    },

                ],
                'quickReplies': [{
                    'label': '다른 self-학습실 보기',
                    'action': 'block',
                    'messageText': 'self-학습실 선택하기',
                    'blockId': '6435ac1770eb005cb17a7588'
                    # [self 학습실 선택하기] 블록

                }],
                'quickReplies': [{
                    'label': '다른 날짜 선택하기',
                    'action': 'block',
                    'messageText': 'self-학습실 선택하기',
                    'blockId': '6435ac1770eb005cb17a7588'
                    # [self 학습실 선택하기] 블록

                }]
            }
        })


# 셀프학습실 예약 final check 질문
@csrf_exempt
def studyRoom_final_check(request):
    answer = ((request.body).decode('utf-8'))
    json_str = json.loads(answer)

    idx = int(json_str['action']['clientExtra']['idx'])
    room = str(json_str['action']['clientExtra']['room'])
    date = str(json_str['action']['clientExtra']['date'])

    select_time = studyroom_Timetable.available_time_list_tag[idx].text

    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [{
                'simpleText': {
                    'text': "[" + date + "], [" + select_time + "]" + "에 "+room + "을(를) 예약하시겠습니까?"
                           # [2023-05-04 (수)], [9:00 ~ 10:00]에 [self 학습실4]를 예약하시겠습니까?

                }
            }],
            'quickReplies': [
                {
                    "label": "네",
                    "action": "block",
                    "messageText": "예약하겠습니다.",
                    'blockId': '6457acc18edae924e926b707',
                    # self 학습실 예약
                    "extra": {
                        "num": idx,
                        "room": room,
                        "date": date,
                        "select_time": select_time
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

# 다른 학습실 보기 버튼
# 출력은 리스트 버튼으로
# 리스트 버튼 클릭 시 예약하겠습니까 버튼.

from . import reserve_studyroom
# self 학습실 예약
@csrf_exempt
def studyRoom_reserve(request):
    answer = ((request.body).decode('utf-8'))
    json_str = json.loads(answer)

    idx = int(json_str['action']['clientExtra']['num'])
    room = str(json_str['action']['clientExtra']['room'])
    date= str(json_str['action']['clientExtra']['date'])


    s = reserve_studyroom.selfroom_reserve(idx)


    # select_time = studyroom_Timetable.available_time_list_tag[idx].text


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


    # if s =="s":
    #     return JsonResponse({
    #         'version': "2.0",
    #         'template': {
    #             'outputs': [{
    #                 'simpleText': {
    #                     # 2023-05-04 (수), [9:00 ~ 10:00]에 [self 학습실4]를 예약했습니다.
    #                     'text':  date + ", " + "[" + select_time + "]에 [" + room + "]을(를) 예약했습니다."
    #                 }
    #             }]
    #         },
    #
    #     })
    #
    # elif s =="d":
    #     return JsonResponse({
    #         'version': "2.0",
    #         'template': {
    #             'outputs': [{
    #                 'simpleText': {
    #                     'text': "예약에 실패했습니다.\n예약은 1일 최대 2시간까지 가능합니다."
    #                 }
    #             }]
    #         }
    #     })
    #
    # elif s =="f":
    #     return JsonResponse({
    #         'version': "2.0",
    #         'template': {
    #             'outputs': [{
    #                 'simpleText': {
    #                     'text': "예약에 실패했습니다.\n다시 시도해주세요."
    #                 }
    #             }],
    #             'quickReplies': [{
    #                 'label': '다시 시도',
    #                 'action': 'block',
    #                 'messageText': '다시 시도하기',
    #                 'blockId': '6435adf77ab7b038704cebf7'
    #             }]
    #         }
    #     })








#예약은 돼..
# 근데 알터 창이 어디선 하나 더뜨고 어디서 안뜨나봐
# 현재는 알터 창이 한번 더 뜨면 초과로 인식하는데 이걸 수정해야돼
#
# 그리고 2번째 예약때 로그인이 아에 작동안해

