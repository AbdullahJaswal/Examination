from content.models import *
from .serializers import *

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from django.conf import settings
import os
import pandas as pd

permissions = [AllowAny]
permissions_func = [AllowAny()]

# caching = [cache_page(60 * 5)]
caching = [cache_page(1)]


# Create your views here.

# Category
class CategoryList(generics.ListCreateAPIView):
    model = Category
    permission_classes = permissions
    throttle_classes = [UserRateThrottle]
    queryset = model.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]

        return permissions_func

    @method_decorator(caching)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)

    #     # Create CSV in <PROJECT_ROOT>/data for development
    #     if settings.DEBUG:
    #         data = self.queryset

    #         df = pd.DataFrame(data.values())

    #         project_path = settings.BASE_DIR
    #         folder_name = '/data/'
    #         app_name = '{}'.format(self.model._meta.app_label)
    #         file_name = '/{}.csv'.format(self.model.__name__.lower())

    #         folder_path = '{}{}{}'.format(project_path, folder_name, app_name)
    #         file_path = '{}{}'.format(folder_path, file_name)

    #         if not os.path.exists(folder_path):
    #             os.mkdir(folder_path)

    #         if os.path.exists(file_path):
    #             os.remove(file_path)

    #         df = df.sort_values(by=['id'])
    #         df.to_csv(file_path, index=False)

    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Category
    permission_classes = permissions
    throttle_classes = [UserRateThrottle]
    queryset = model.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser()]

        return permissions_func


# Subject
class SubjectList(generics.ListCreateAPIView):
    model = Subject
    permission_classes = permissions
    throttle_classes = [UserRateThrottle]
    queryset =  model.objects.all()
    serializer_class = SubjectSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]

        return permissions_func

    @method_decorator(caching)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)

    #     # Create CSV in <PROJECT_ROOT>/data for development
    #     if settings.DEBUG:
    #         data = self.queryset

    #         df = pd.DataFrame(data.values())

    #         project_path = settings.BASE_DIR
    #         folder_name = '/data/'
    #         app_name = '{}'.format(self.model._meta.app_label)
    #         file_name = '/{}.csv'.format(self.model.__name__.lower())

    #         folder_path = '{}{}{}'.format(project_path, folder_name, app_name)
    #         file_path = '{}{}'.format(folder_path, file_name)

    #         if not os.path.exists(folder_path):
    #             os.mkdir(folder_path)

    #         if os.path.exists(file_path):
    #             os.remove(file_path)

    #         df = df.sort_values(by=['id'])
    #         df.to_csv(file_path, index=False)

    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Subject
    permission_classes = permissions
    throttle_classes = [UserRateThrottle]
    queryset = model.objects.all()
    serializer_class = SubjectSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser()]

        return permissions_func


# Product
class ProductList(generics.ListCreateAPIView):
    model = Product
    permission_classes = permissions
    throttle_classes = [UserRateThrottle]
    queryset = model.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.queryset.filter(
            category__is_active=True,
            subject__is_active=True
        )

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]

        return permissions_func

    @method_decorator(caching)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)

    #     # Create CSV in <PROJECT_ROOT>/data for development
    #     if settings.DEBUG:
    #         data = self.queryset

    #         df = pd.DataFrame(data.values())

    #         project_path = settings.BASE_DIR
    #         folder_name = '/data/'
    #         app_name = '{}'.format(self.model._meta.app_label)
    #         file_name = '/{}.csv'.format(self.model.__name__.lower())

    #         folder_path = '{}{}{}'.format(project_path, folder_name, app_name)
    #         file_path = '{}{}'.format(folder_path, file_name)

    #         if not os.path.exists(folder_path):
    #             os.mkdir(folder_path)

    #         if os.path.exists(file_path):
    #             os.remove(file_path)

    #         df = df.sort_values(by=['id'])
    #         df.to_csv(file_path, index=False)

    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Product
    permission_classes = permissions
    throttle_classes = [UserRateThrottle]
    queryset = model.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser()]

        return permissions_func

# Nested (Category)
class CategoryProductList(generics.ListAPIView):
    permission_classes = permissions
    throttle_classes = [UserRateThrottle]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'cat'

    def get_queryset(self):
        return self.queryset.filter(
            category_id=self.kwargs.get('cat'),
            category__is_active=True,
            is_active=True
        )

    @method_decorator(caching)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# Nested (Subject)
class SubjectProductList(generics.ListAPIView):
    permission_classes = permissions
    throttle_classes = [UserRateThrottle]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'sub'

    def get_queryset(self):
        return self.queryset.filter(
            subject_id=self.kwargs.get('sub'),
            subject__is_active=True,
            is_active=True
        )

    @method_decorator(caching)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# Nested (Category Subject)
class CategorySubjectProductList(generics.ListAPIView):
    permission_classes = permissions
    throttle_classes = [UserRateThrottle]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'cat'

    def get_queryset(self):
        return self.queryset.filter(
            category_id=self.kwargs.get('cat'),
            category__is_active=True,
            subject_id=self.kwargs.get('sub'),
            subject__is_active=True,
            is_active=True
        )

    @method_decorator(caching)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
