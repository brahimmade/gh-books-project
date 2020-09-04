from django.urls import path

from . import views

app_name = 'bookselection'

urlpatterns = [
    # ex: /bookselection/
    path('', views.index, name='index'),
]