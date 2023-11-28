from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Major(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    buff_id = models.CharField(max_length=7, unique=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Class(models.Model):
    code = models.CharField(max_length=255, default='CIDM')
    classname = models.CharField(max_length=255)
    credit_hours = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.classname}"


class NineHoursFrom(models.Model):
    code = models.CharField(max_length=255, default='CIDM')
    classname = models.CharField(max_length=255)
    credit_hours = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.classname}"


class UCComm(models.Model):
    code = models.CharField(max_length=255, default='CIDM')
    classname = models.CharField(max_length=255)
    credit_hours = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.classname}"


class UCMathSocial(models.Model):
    code = models.CharField(max_length=255, default='CIDM')
    classname = models.CharField(max_length=255)
    credit_hours = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.classname}"


class UCComponent(models.Model):
    code = models.CharField(max_length=255, default='CIDM')
    classname = models.CharField(max_length=255)
    credit_hours = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.classname}"


class Advisor(models.Model):
    name = models.CharField(max_length=255)
    contact_information = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default="CC")

    def __str__(self):
        return f"{self.name}"
