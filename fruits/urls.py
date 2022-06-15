from django.contrib import admin
from django.urls import path, include
from .views import AutoCompFruitsView

urlpatterns = [
	path('autoCompF/', AutoCompFruitsView.as_view()),
]