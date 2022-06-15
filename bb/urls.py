from django.contrib import admin
from django.urls import path, include
from .views import BBTAPGetBBTData, BBTAPGetStudentData, BBTAPGetTotalStats

urlpatterns = [
	path('getbbtdata/', BBTAPGetBBTData.as_view()),
	path('getstudentdata/', BBTAPGetStudentData.as_view()),
	path('gettotalstats/', BBTAPGetTotalStats.as_view()),
]