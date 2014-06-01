from django.db import models

class Assignment(models.Model):
	assignment_id = models.AutoField(primary_key=True, unique=True)
	class_id = models.ForeignKey('class.Classroom')
	#student_id = models.ForeignKey('students.student_id')
	assigned = models.BooleanField()
	answerkey_id = models.ForeignKey('compositions.Composition',related_name='answerkey_composition')
	studentresponse_id = models.ForeignKey('compositions.Composition',related_name='studentresponse')