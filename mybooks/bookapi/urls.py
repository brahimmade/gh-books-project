from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'books', BooksViewSet) 
router.register(r'users', UserViewSet)

app_name = 'bookapi'

urlpatterns = [
 path('admin/', admin.site.urls),
 path('', include(router.urls))
]