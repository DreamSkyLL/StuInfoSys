from django.urls import path
from . import views

app_name = 'runningattendance'

urlpatterns = [
    # path("result", views.result, name='result'),
    path('result', views.ResultView.as_view(), name='result'),
]
