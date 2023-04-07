from django.urls import path
from . import views

urlpatterns = [
    path(r'^', views.today),

    path(r'^keyboard/', views.keyboard),
    path(r'^message', views.message),
    #path('', views.index, name='index'),

]

# from django.contrib import admin
# from django.urls import path, include
# from anyang_Bot.anyang_Bot import views as main_views
# from . import views
#
#
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('', main_views.index, name="index"),
#     path('admin/', admin.site.urls),
# ]