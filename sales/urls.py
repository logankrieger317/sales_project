# tunr/urls.py
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", views.user_list, name="user_list"),
    path(
        "users/<int:pk>", views.UserDetail.as_view(), name="user_detail"
    ),  # add .as_view()
    path("profiles/", views.ProfileList.as_view(), name="profile_list"),
    path("profiles/<int:pk>", views.ProfileDetail.as_view(), name="profile_detail"),
]
