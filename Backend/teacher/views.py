from django.shortcuts import render
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from teacher.models import Teacher
from teacher.serializers import TeacherSerializer

class Teacher(APIView):

	def get(self, request, format=None):
		teachers = Teacher.object.all()
		serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
    	serializer = TeacherSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, teacher_id,format=None):
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