from django.contrib import admin
from django.urls import path, include
from .views import AutoCompFruitsView, getBbtStudentsView, getPerBBTView

urlpatterns = [
	path('autoCompF/', AutoCompFruitsView.as_view()),
	path('bbtStudent/<int:id>', getBbtStudentsView.as_view()),
	path('bbt/<int:seasonid>/students', getPerBBTView.as_view())
]