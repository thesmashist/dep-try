from django.urls import path
from users import views as userviews
from . import views
from users.views import LoginView, UserView

urlpatterns = [
    path('api', views.getRoutes),
    path('api/token/', userviews.LoginView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', UserView.as_view(), name='token_refresh'),
]