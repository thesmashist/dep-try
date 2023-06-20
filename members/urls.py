from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from . import views
from .views import MemberList, MemberAPIView, MemberByRegion, MemberLogin


urlpatterns = [
    path('', MemberList.as_view()),
    path('<int:id>', MemberAPIView.as_view()),
    path('<str:region>', MemberByRegion.as_view()),
    path('login/<int:id>', MemberLogin.as_view()),
]