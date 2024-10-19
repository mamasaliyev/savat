from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer, LoginSerializer, EmptySerializer


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def get(self, request):
        return Response({
            'message': 'To register, send a POST request with the following fields: username, email, password1, password2, profile_picture, phone_number.',
            'example': {
                'username': 'testuser',
                'email': 'test@example.com',
                'password1': 'yourpassword',
                'password2': 'yourpassword',
                'profile_picture': 'null',
                'phone_number': '1234567890'
            }
        }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Foydalanuvchini yaratish
        user = serializer.save()

        # Token olish
        refresh = RefreshToken.for_user(user)

        return Response({
            'message': 'Registration successful',
            'access': str(refresh.access_token),  # Access token
        }, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Token olish
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Login successful',
                'access': str(refresh.access_token),  # Access token
                'refresh': str(refresh),  # Refresh token
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = EmptySerializer

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
