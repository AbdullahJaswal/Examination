from .views import *

from django.urls import path

app_name = 'product'

urlpatterns = [
    # Category
    path('category/', CategoryList.as_view(), name='categoryList'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='categoryDetail'),

    # Subject
    path('subject/', SubjectList.as_view(), name='subjectList'),
    path('subject/<int:pk>/', SubjectDetail.as_view(), name='subjectDetail'),

    # Product
    path('product/', ProductList.as_view(), name='productList'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='productDetail'),

    # Nested (Category)
    path(
        'category/<int:cat>/product/',
        CategoryProductList.as_view(),
        name='categoryProductList'
    ),

    # Nested (Subject)
    path(
        'subject/<int:sub>/product/',
        SubjectProductList.as_view(),
        name='subjectProductList'
    ),

    # Nested (Category Subject)
    path(
        'category/<int:cat>/subject/<int:sub>/product/',
        CategorySubjectProductList.as_view(),
        name='categorySubjectProductList'
    ),
]
