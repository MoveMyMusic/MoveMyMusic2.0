from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from compositions.models import Composition
from compositions.serializers import CompositionSerializer

class Composition(APIView):

	def get(self, request, format=None):
		compositions = Composition.object.all()
		serializer = CompositionSerializer(compositions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
    	serializer = CompositionSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, composition_id,format=None):
        composition = self.get_object(composition_id)
        serializer = CompositionSerializer(composition, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, composition_id, format=None):
        composition = self.get_object(composition_id)
        composition.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
