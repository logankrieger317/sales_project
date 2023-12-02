from django.shortcuts import render

# views.py
from django.http import JsonResponse
from .models import User, Profile
from .serializers import ProfileSerializer, UserSerializer
from rest_framework import generics
from django.contrib import admin
from django.http import Http404
from rest_framework.response import Response


def user_list(request):
    users = User.objects.all().values(
        "name",
        "position",
    )  # only grab some attributes from our database, else we can't serialize it.
    user_list = list(users)  # convert our users to a list instead of QuerySet
    return JsonResponse(
        user_list, safe=False
    )  # safe=False is needed if the first parameter is not a dictionary.


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all().values("position", "availability")
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all().values("position", "availability")


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            return Response({"error": "User not found"}, status=404)


# Create your views here.
