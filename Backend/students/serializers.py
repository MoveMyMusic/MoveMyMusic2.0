from django.forms import widgets
from rest_framework import serializers
from teacher.models import Student

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ('student_id', 'first_name', 'last_name', 'class_id')
		
