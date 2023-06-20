"""dj_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView

from django.urls import path
from base.api import views
from users import views as userviews
from users.views import LoginView, UserView, BBTList
from members import urls
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('base.api.urls')),

    path('', views.getRoutes),
    path('api/token/', userviews.LoginView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', UserView.as_view(), name='token_refresh'),

    path('api/bbt/', BBTList.as_view()),
    path('api/member/', include('members.urls')),

	# path('', include('app.urls')),
	path('bb/', include('bb.urls')),
	path('forms/', include('forms.urls')),
	path('fruits/', include('fruits.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    # re_path(r'^.*', TemplateView.as_view(), name="home")
]
