from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from teacher.models import Teacher
from teacher.serializers import TeacherSerializer

class Teacher(APIView):
	def get(self, request, teacher_id, format=None):
		teacher = self.get_object(teacher_id)
		serializer = TeacherSerializer(teacher, many=True)
		return Response(serializer.data)
	def post(self, request, format=None):
		serializer = TeacherSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def put(self, request, teacher_id, format=None):
		teacher = self.get_object(teacher_id)
		serializer = TeacherSerializer(teacher, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self, request, teacher_id, format=None):
		teacher = self.get_object(teacher_id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)