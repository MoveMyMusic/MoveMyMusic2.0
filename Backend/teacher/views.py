from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from teacher.models import Teacher
from teacher.serializers import TeacherSerializer

#This is where we need to define what we actually need to do for teachers
@api_view(['GET', 'POST'])