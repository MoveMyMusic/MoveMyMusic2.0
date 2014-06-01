from django.db import models

class Composition(models.Model):
	composition_id = models.AutoField(primary_key=True, unique=True)
	student_id = models.ForeignKey('students', related_name='+')
	saved_compostion = models.TextField(blank=True)