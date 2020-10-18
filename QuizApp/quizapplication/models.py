from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.AutoField(primary_key=True)
    rollno=models.CharField(max_length=20)

class Quiz(models.Model):
    id=models.AutoField(primary_key=True)
    text=models.CharField(max_length=20)

class Question(models.Model):
    id=models.AutoField(primary_key=True)
    text=models.CharField(max_length=256)
    Quiz=models.ForeignKey(Quiz,null=False)

class Options(models.Model):
    question=models.ForeignKey(Question,null=False)
    text=models.CharField(max_length=30)
    isCorrect=models.BooleanField(default=False)


