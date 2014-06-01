from django.forms import widgets
from rest_framework import serializers
from compositions.models import Composition

class CompositionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Composition
		fields = ('composition_id', 'student_id', 'saved_comp')
	