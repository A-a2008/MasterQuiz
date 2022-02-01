from cgi import test
from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("test/", test1, name="test")
]
