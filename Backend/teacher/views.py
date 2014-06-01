from teacher.models import Teacher
from teacher.serializers import TeacherSerializer
from rest_framework import generics

class TeacherList(generics.ListCreateAPIView):
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer