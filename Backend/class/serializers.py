from django.forms import widgets
from rest_framework import serializers
from teacher.models import Class

class ClassSerializer(serializers.ModelSerializer):
	class Meta:
		model = Class
		fields = ('class_id', 'teacher_id', 'class_password', 'class_name')
	