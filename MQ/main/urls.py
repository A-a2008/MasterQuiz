from cgi import test
from django.urls import path
from .views import *

create_paper = CreatePaper()

urlpatterns = [
    path("", home, name="home"),
    path("test/", test1, name="test"),
    path("create/", create_paper.create_paper_1, name="view_paper")
]
