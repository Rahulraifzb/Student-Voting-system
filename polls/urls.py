from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt





urlpatterns = [ 
    path("list/",polls,name="polls"),
    path("vote/",poll_vote,name="poll-vote"),
    path("<str:pk>/",poll_detail,name="poll-detail"),
]