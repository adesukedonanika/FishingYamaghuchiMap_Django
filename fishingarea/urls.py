# 新規作成した

from django.urls import path
from . import views

app_name = 'fishingarea'
urlpatterns = [
    path('', views.IndexView.as_view(),name="index")
]

