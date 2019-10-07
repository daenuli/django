from django.urls import path

from . import views

app_name = 'depanhome'
urlpatterns = [
    path('', views.index, name='index'),
]
