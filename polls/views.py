from django_filters.rest_framework import DjangoFilterBackend

from .models import Student, Group, Teacher
from .serializers import StudentSerializer, GroupSerializer, TeacherSerializer
from rest_framework import generics


class StudentList(generics.ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = {'favoriteNumber': ['gt', 'lt']}


class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer


class GroupList(generics.ListCreateAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


class GroupDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
