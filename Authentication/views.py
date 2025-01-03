from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_405_METHOD_NOT_ALLOWED
from drf_spectacular.utils import extend_schema
from .forms import SignUpForm
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
import logging, json

logger = logging.getLogger('custom_logger')

# Signup View
class SignupView(APIView):
    permission_classes = [AllowAny]
    @extend_schema(
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "username": {"type": "string", "example": "testuser"},
                    "email": {"type": "string", "example": "user@gmail.com"},
                    "password1": {"type": "string", "example": "testpassword"},
                    "password2": {"type": "string", "example": "testpassword"},
                },
                "required": ["username", "password1","password2"],
            }
        },
        responses={
            201: {"description": "User created successfully."},
            400: {"description": "Invalid form data."},
            500: {"description": "Internal server error."},
        },
        description="API endpoint for user signup."
    )
    def post(self, request):
        try:
            data = request.data
            form = SignUpForm(data)
            if form.is_valid():
                form.save()
                logger.info("User signed up successfully.")
                return Response({"success": True, "message": "Sign up successful!"}, status=HTTP_201_CREATED)
            else:
                logger.warning("Sign up failed due to invalid form data.")
                return Response({"success": False, "message": "Invalid form data.", "errors": form.errors}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"An error occurred during signup: {e}", exc_info=True)
            return Response({"success": False, "message": "An error occurred during sign up."}, status=HTTP_500_INTERNAL_SERVER_ERROR)

# Signin View
class SigninView(APIView):
    permission_classes = [AllowAny]
    @extend_schema(
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "username_login": {"type": "string", "example": "testuser"},
                    "password_login": {"type": "string", "example": "testpassword"},
                    "next": {"type": "string", "example": "/dashboard/"}
                },
                "required": ["username_login", "password_login"],
            }
        },
        responses={
            200: {
                "description": "Login successful. Returns JWT tokens.",
                "type": "object",
                "properties": {
                    "refresh": {"type": "string", "example": "refresh_token_example"},
                    "access": {"type": "string", "example": "access_token_example"},
                }
            },
            400: {"description": "Invalid credentials or input."},
            500: {"description": "Internal server error."},
        },
        description="API endpoint for user signin."
    )
    def post(self, request):
        try:
            data = request.data
            username_login = data.get("username_login")
            password_login = data.get("password_login")
            next_page = data.get("next", "")

            if not username_login or not password_login:
                return Response({"success": False, "message": "Email and password are required."}, status=HTTP_400_BAD_REQUEST)

            user = authenticate(request, username=username_login, password=password_login)
            if user:
                login(request, user)
                logger.info(f"Login successful for user: {username_login}")
                refresh = RefreshToken.for_user(user)
                return Response({
                    "success": True,
                    "next_page": next_page,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }, status=HTTP_200_OK)
            else:
                logger.warning(f"Failed login attempt for user: {username_login}")
                return Response({"success": False, "message": "Invalid username or password!"}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"An error occurred during login: {e}", exc_info=True)
            return Response({"success": False, "message": "An error occurred."}, status=HTTP_500_INTERNAL_SERVER_ERROR)

