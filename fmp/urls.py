from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from . import views
from .views import EVStats

urlpatterns = [
    path('<int:id>/stats', EVStats.as_view()),
]