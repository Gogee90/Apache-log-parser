from .views import CreateUserAccountView, LoginView
from django.urls import path, include


urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("register/", CreateUserAccountView.as_view(), name='register'),
    path("dj-rest-auth/", include('dj_rest_auth.urls'), name='api-login')
]