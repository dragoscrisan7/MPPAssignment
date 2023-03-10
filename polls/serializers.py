from rest_framework import serializers
from .models import Student, Group, Teacher


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ('id', 'firstname', 'name', 'favoriteNumber', 'favorite_colour', 'GroupId')


class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ('id', 'groupNr', 'groupNickname', 'language', 'year')


class TeacherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Teacher
		fields = ('id', 'firstname', 'name', 'TeachingSubject', 'years_of_experience')
