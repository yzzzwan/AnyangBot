from django.shortcuts import render
from django.http import HttpResponse
from . import crawl
from django.http import JsonResponse
from django.http import request as json
# Create your views here.
# def index(request):
#     return render(request, "haksik/index.html")

def test(request):
     return HttpResponse(crawl.menu_list)


def index(request):
    return render(request, "haksik/index.html")


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
                    'text': crawl.week_menu
                }
            }],
            'quickReplies': [{

            }]
        }
    })

# 오늘 급식 출력
@csrf_exempt
def today_haksik(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance'] # 사용자의 발화 텍스트

    #월 ~ 금
    if(crawl.now >=0 and crawl.now <=4):
            return JsonResponse({
                'version': "2.0",
                'template': {
                    'outputs': [{
                        'simpleText': {
                            'text': crawl.today_menu
                        }
                    }],
                    'quickReplies': [{
                        'label': '처음으로',
                        'action': 'message',
                        'messageText': '처음으로'
                    }]
                }
            })

    else:
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': "오늘은 쉬는 날 입니다.😊"
                    }
                }],
                'quickReplies': [{
                'label': '처음으로',
                'action': 'message',
                    'messageText': '처음으로'
                }]
            }
        })

