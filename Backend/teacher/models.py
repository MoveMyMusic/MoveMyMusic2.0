from django.db import models

class Teacher(models.Model):
	teacher_id = models.AutoField(primary_key=True, unique=True,)
	username = models.CharField(max_length=40)
	teacher_name = models.CharField(max_length=40)
	email = models.EmailField(max_length=254)
	password = models.CharField(max_length=40)

