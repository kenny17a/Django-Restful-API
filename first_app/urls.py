from django.contrib import admin
from django.urls import path
from .views import UserRegistration, UserLogin, UserProfile, UserChangePassword, SentResetPasswordEmail, UserPasswordReset, LogoutUser

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", UserRegistration.as_view(), name="register"),
    path("login/", UserLogin.as_view(), name="login"),
    path("profile/", UserProfile.as_view(), name="profile"),
    path("changePassword/", UserChangePassword.as_view(), name="changePassword"),
    path("reset-password/", SentResetPasswordEmail.as_view(), name="resetPassword"),
    path("reset-password/<uid>/<token>/", UserPasswordReset.as_view(), name="user-reset-password"),
    path("logout/", LogoutUser.as_view(), name="logout")
]
