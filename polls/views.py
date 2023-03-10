from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student, Group, Teacher
from .serializers import StudentSerializer, GroupSerializer, TeacherSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404

class StudentList(APIView):
	def post(self, request):
		student = StudentSerializer(data=request.data)

		# validating for already existing data
		if Student.objects.filter(**request.data).exists():
			raise serializers.ValidationError('This data already exists')

		if student.is_valid():
			student.save()
			return Response(student.data)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)

	def get(self, request):
		# checking for the parameters from the URL
		if request.query_params:
			items = Student.objects.filter(**request.query_params.dict())
		else:
			items = Student.objects.all()

		# if there is something in items else raise error
		if items:
			serializer = StudentSerializer(items, many=True)
			return Response(serializer.data)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)

class StudentDetails(APIView):
	def get_object(self, pk):
		try:
			return Student.objects.get(pk=pk)
		except Student.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

	def get(self, request, pk):
		snippet = self.get_object(pk)
		serializer = StudentSerializer(snippet)
		return Response(serializer.data)

	def delete(self, request, pk):
		item = self.get_object(pk)
		item.delete()
		return Response(status=status.HTTP_202_ACCEPTED)

	def put(self, request, pk):
		item = Student.objects.get(pk=pk)
		data = StudentSerializer(instance=item, data=request.data)

		if data.is_valid():
			data.save()
			return Response(data.data)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)

class GroupList(APIView):
	def post(self, request):
		group = GroupSerializer(data=request.data)

		# validating for already existing data
		if Group.objects.filter(**request.data).exists():
			raise serializers.ValidationError('This data already exists')

		if group.is_valid():
			group.save()
			return Response(group.data)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)

	def get(self, request):
		# checking for the parameters from the URL
		if request.query_params:
			items = Group.objects.filter(**request.query_params.dict())
		else:
			items = Group.objects.all()

		# if there is something in items else raise error
		if items:
			serializer = GroupSerializer(items, many=True)
			return Response(serializer.data)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)

class GroupDetails(APIView):
	def get_object(self, pk):
		try:
			return Group.objects.get(pk=pk)
		except Group.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

	def get(self, request, pk):
		snippet = self.get_object(pk)
		serializer = GroupSerializer(snippet)
		return Response(serializer.data)

	def delete(self, request, pk):
		item = self.get_object(pk)
		item.delete()
		return Response(status=status.HTTP_202_ACCEPTED)

	def put(self, request, pk):
		item = Group.objects.get(pk=pk)
		data = GroupSerializer(instance=item, data=request.data)

		if data.is_valid():
			data.save()
			return Response(data.data)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)