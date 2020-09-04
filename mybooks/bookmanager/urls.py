from django.urls import path

from . import views

app_name = 'bookmanager'

urlpatterns = [
    # ex: /bookmanager/
    path('', views.index, name='index'),
]