from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from students.models import Student
from students.serializers import StudentSerializer

#put:update, post:create

class Student(APIView):
	def get(self, request, student_id, format=None):
		student = self.get_object(student_id)
		serializer = StudentSerializer(student, many=True)
		return Response(serializer.data)
	def post(self, request, format=None):
		serializer = StudentSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def put(self, request, student_id, format=None):
		student = self.get_object(student_id)
		serializer = StudentSerializer(student, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self, request, student_id, format=None):
		student = self.get_object(student_id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)