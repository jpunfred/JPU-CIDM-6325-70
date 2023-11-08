from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    

class Curriculum(models.Model):
    curriculum_name = models.CharField(max_length=100)
    total_credits_required = models.IntegerField()
    

class Course(models.Model):
    course_code = models.CharField(max_length=10)
    course_title = models.CharField(max_length=100)
    credit_hours = models.IntegerField()
    

class EnrolledCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    grade = models.CharField(max_length=5)
    

class Advisor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    office_location = models.CharField(max_length=100)
    
