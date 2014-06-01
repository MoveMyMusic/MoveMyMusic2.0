from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from assignments.models import Assignment
from assignments.serializers import AssignmentSerializer

class Assignment(APIView):

	def get(self, request, format=None):
		assignments = Assignment.object.all()
		serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
    	serializer = AssignmentSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, assignment_id,format=None):
        assignment = self.get_object(assignment_id)
        serializer = AssignmentSerializer(assignment, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, assignment_id, format=None):
        assignment = self.get_object(assignment_id)
        assignment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)