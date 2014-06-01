from django.db import models

class Assignment(models.Model):
	assignment_id = models.AutoField(primary_key=True, unique=True)
	class_id = models.ForeignKey('class',related_name='+')
	#student_id = models.ForeignKey('students.student_id')
	assigned = models.BooleanField()
	answerkey_id = models.ForeignKey('compositions',related_name='+')
	studentresponse_id = models.ForeignKey('compositions',related_name='+')