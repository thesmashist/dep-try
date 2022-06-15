from django.contrib import admin
from django.urls import path, include
from .views import AutoCompFruitsView, CheckDFView

urlpatterns = [
	path('autoCompF/', AutoCompFruitsView.as_view()),
	path('checkDF/', CheckDFView.as_view()),
]