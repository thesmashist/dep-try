from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from . import views
from .views import BBTList

urlpatterns = [
    path('', BBTList.as_view()),
]