from django.db import models

class Student(models.Model):
	student_id = models.AutoField(primary_key=True, unique=True,)
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	class_id = models.ForeignKey('Classroom')
