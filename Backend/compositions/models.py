from django.db import models

class Composition(models.Model):
	composition_id = models.AutoField(primary_key=True, unique=True)
	student_id = models.ForeignKey('students.student_id')
	saved_compostion = models.TextField(blank=True)