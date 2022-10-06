
from django.urls import path,

from socialapp.views import Register_user

urlpatterns = [

path('',Register_user.as_view()),
]
