from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=40)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=124)
    dob = models.DateField(null=True, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    email = models.CharField(max_length=125)
    ph_no = models.PositiveIntegerField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    purpose=models.CharField(max_length=250)
    materials=models.CharField(max_length=250)


    def __str__(self):
        return self.name

