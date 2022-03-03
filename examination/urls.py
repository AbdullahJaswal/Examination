from .views import *

from django.urls import path

app_name = 'examination'

urlpatterns = [
    # User Product
    path('product/', UserProductList.as_view(), name='userProductList'),
    path('product/<int:pk>/', UserProductDetail.as_view(), name='userProductDetail'),

    # User Product Submission
    path('user_product/<int:pk>/submission/', UserProductSubmissionList.as_view(), name='userProductSubmissionList'),
    path('user_product/<int:pk>/submission/<int:qID>/<int:aID>/', UserProductSubmissionDetail.as_view(), name='userProductSubmissionDetail'),
]
