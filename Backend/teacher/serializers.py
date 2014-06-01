from django.forms import widgets
from rest_framework import serializers
from teacher.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Teacher
		fields = ('username', 'teacher_name', 'email', 'password')
	