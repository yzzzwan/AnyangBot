from django.shortcuts import render
from django.http import HttpResponse
from . import haksik_crawl
from . import phoneDir_crawl as pdc
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

from . import test

# self 학습실 시간표 보여주기
@csrf_exempt
def studyRoom(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']  # 사용자의 발화 텍스트
    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [{
                'simpleText': {
                    'text': "phoneBook"
                }
            }]
        }
    })

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


