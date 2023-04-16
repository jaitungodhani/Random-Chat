from django.urls import path, include
from .views import (
    LoginView,
    LogoutView,
    UserManageView
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("logout", LogoutView, basename="logout")
router.register("user", UserManageView, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path("login/", LoginView.as_view())
]