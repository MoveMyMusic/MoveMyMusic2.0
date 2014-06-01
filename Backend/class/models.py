from django.db import models

class Classroom(models.Model):
	class_id = models.AutoField(primary_key=True, unique=True,)
	teacher_id = models.ForeignKey(Teacher,related_name='+')
	class_password = models.CharField(max_length=40)
	class_name = models.CharField(max_length=40)