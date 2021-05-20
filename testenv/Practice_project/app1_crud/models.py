from django.db import models


# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    dept_id = models.IntegerField()
    age = models.IntegerField()


class Department(models.Model):
    dep_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    dep_name = models.CharField(max_length=20)



