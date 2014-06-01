from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from class.models import class
from class.serializers import classSerializer

class Classroom(APIView):
	def get(self, request, class_id, format=None):
		classroom = self.get_object(class_id)
		serializer = ClassSerializer(class, many=True)
		return Response(serializer.data)
	def post(self, request, format=None):
		serializer = ClassSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def put(self, request, class_id, format=None):
		classroom = self.get_object(class_id)
		serializer = ClassSerializer(classroom, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self, request, class_id, format=None):
		classroom = self.get_object(class_id)
        classroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)