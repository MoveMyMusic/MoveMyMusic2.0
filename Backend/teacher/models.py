from django.db import models

class Teacher(models.Model):
	username = models.CharField(max_length=40, blank=True, default='')
	teachername = models.CharField(max_length=40, blank=True, default='')
	email = models.CharField(max_length=100, blank=True, default='')
	password = models.CharField(max_length=40, blank=True, default='')

