from content.models import Answer
from .serializers import *

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


permissions = [IsAuthenticated]
permissions_func = [IsAuthenticated()]

# caching = [cache_page(60 * 5)]
caching = [cache_page(1)]


# Create your views here.

# User Product
class UserProductList(generics.ListCreateAPIView):
    model = UserProduct
    permission_classes = [IsAdminUser]
    throttle_classes = [UserRateThrottle]
    queryset = model.objects.all()
    serializer_class = UserProductSerializer

    def get_queryset(self):
        return self.queryset.all()

    @method_decorator(caching)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserProductDetail(generics.RetrieveUpdateDestroyAPIView):
    model = UserProduct
    permission_classes = [IsAdminUser]
    throttle_classes = [UserRateThrottle]
    queryset = model.objects.all()
    serializer_class = UserProductSerializer


# User Product Submission
class UserProductSubmissionList(generics.ListAPIView):
    model = UserProduct
    permission_classes = permissions
    throttle_classes = [UserRateThrottle]
    queryset = model.objects.all()
    serializer_class = UserProductSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user, product_id=self.kwargs.get('pk'))

    @method_decorator(caching)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserProductSubmissionDetail(generics.RetrieveUpdateAPIView):
    model = UserProduct
    permission_classes = permissions
    throttle_classes = [UserRateThrottle]
    queryset = model.objects.all()
    serializer_class = UserProductSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user, product_id=self.kwargs.get('pk'))

    def patch(self, request, *args, **kwargs):
        try:
            user_product = self.queryset[0]

            if user_product.is_active or user_product.submissions.count() < 3:
                answer = Answer.objects.get(id=self.kwargs.get('aID'))

                self.queryset[0].submissions.create(
                    user=self.request.user,
                    question_id=self.kwargs.get('qID'),
                    answer=answer,
                    is_correct=answer.is_correct
                )

                if answer.is_correct:
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_418_IM_A_TEAPOT)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
