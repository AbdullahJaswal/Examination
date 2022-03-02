from .views import *

from django.urls import path

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='create_user'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist'),

    path('', UserDetail.as_view(), name='userDetail'),
]
