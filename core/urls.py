"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

import environ

env = environ.Env()
env.read_env()

urlpatterns = [
    # Django
    path('admin/', admin.site.urls) if settings.DEBUG else path(env('ADMIN_PAGE'), admin.site.urls),

    # Rest Framework
    path('api-auth/', include('rest_framework.urls')),

    # Other
    path('__debug__/', include('debug_toolbar.urls')),

    # Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Apps
    path('user/', include('users.urls', namespace='users')),
    path('content/', include('content.urls', namespace='content')),
    path('product/', include('product.urls', namespace='product')),
    path('examination/', include('examination.urls', namespace='examination')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
