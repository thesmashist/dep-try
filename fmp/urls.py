from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from . import views
from .views import EVStats, EVSeason, EVStatsOverall

urlpatterns = [
    path('<int:id>/weeklystats', EVStats.as_view()),
    path('<int:id>/stats', EVStatsOverall.as_view()),
    path('<str:region>/season/', EVSeason.as_view()),
    path('<str:region>/season/<department>', EVSeason.as_view()),
]

def getRoutes(request):
    routes = [
        'api/fmp/<int:id>/stats',
        'api/fmp/<int:phone>/check',
        'api/fmp/<str:region>/season/',
        'api/fmp/<str:region>/season/<department>',
    ]