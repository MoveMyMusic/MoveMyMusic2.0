from django.forms import widgets
from rest_framework import serializers
from compositions.models import Composition

class AssignmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Assignment
		fields = ('assignment_id','class_id','assigned','answerkey_id','studentresponse_id')