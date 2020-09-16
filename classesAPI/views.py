from django.shortcuts import render
from classes.models import Classroom

from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import RigesterSerializer, ClassroomListSerializer, ClassroomDetailsSerializer, ClassroomUpdateSerializer


# Create your views here.

class Rigester(CreateAPIView):
    serializer_class = RigesterSerializer

class ClassroomList(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer

class ClassroomDetails(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class ClassroomUpdate(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class ClassroomCreate(CreateAPIView):
    serializer_class = ClassroomUpdateSerializer
    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class ClassroomDelete(DestroyAPIView):
    queryset = Classroom.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'
