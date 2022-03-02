from .serializers import *
from .permissions import *

from rest_framework import status, response, generics
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

# Registration
class CustomUserCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer
    throttle_scope = 'sign_up'  # Scoped throttle for special case. (Sign Up RATE)


class BlacklistTokenUpdateView(generics.CreateAPIView):
    permission_classes = [AllowAny, IsOwnerOfObject]
    throttle_classes = [UserRateThrottle]  # Can only log out when logged in. (USER RATE)
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = self.request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()

            return response.Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


# User Profile (for frontend)
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOfObject]
    throttle_classes = [UserRateThrottle]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Always return current user.
    def get_object(self):
        return self.request.user
