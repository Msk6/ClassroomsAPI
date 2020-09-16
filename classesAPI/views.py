from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import RigesterSerializer


# Create your views here.

class Rigester(CreateAPIView):
    serializer_class = RigesterSerializer


