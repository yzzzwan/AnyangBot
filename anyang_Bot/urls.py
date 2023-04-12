"""anyang_Bot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include, re_path
from apps import views as v
from . import views


urlpatterns = [
    path('', v.index, name='index'),
    re_path(r'^weekHaksik/?$', v.week_haksik), # 이번주 학식
    re_path(r'^todayHaksik/?$', v.today_haksik), # 오늘 학식
    re_path(r'^phoneBook/?$', v.phoneDir),  # 전화번호부
    re_path(r'^studyRoom_reserve/?$', v.studyRoom),  # 스터디룸 예약
    #re_path(r'^studyRoom_login/?$', v.studyRoom),  # 스터디룸 login

    #re_path(r'^test/?$', v.test),  # 테스트

    # re_path(r'^message/?$', v.message), #테스트 url
]


# from django.contrib import admin
# from django.urls import path
# from apps import views as main_views
#
# urlpatterns = [
#     path('', main_views.index, name="index"),
#     path('admin/', admin.site.urls),
# ]