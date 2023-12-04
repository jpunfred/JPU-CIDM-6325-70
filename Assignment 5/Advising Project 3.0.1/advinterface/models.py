# advinterface/models.py
from django import forms
from django.db import models
from django.contrib.auth.models import User


class Major(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    SECTION_CHOICES = (
        ('communication', 'Communication'),
        ('mathematics', 'Mathematics'),
        ('social_and_behavioral_sciences', 'Social and Behavioral Sciences'),
        ('component_area_option', 'Component Area Option'),
        ('cis_requirements', 'CIS Requirements'),
        ('nine_hours_from', 'Nine Hours From'),
        ('advanced_cidm_electives', 'Advanced CIDM Electives'),
    )

    class_code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    credit_hours = models.IntegerField(default=3)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)

    def __str__(self):
        return f"{self.class_code} - {self.name}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    buff_id = models.CharField(max_length=7)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)

    # Additional fields for major requirements
    communication = models.ManyToManyField(
        Course, related_name='communication_courses', blank=True)
    mathematics = models.ManyToManyField(Course,
                                         related_name='mathematics_courses',
                                         blank=True)
    social_and_behavioral_sciences = models.ManyToManyField(
        Course, related_name='social_sciences_courses', blank=True)
    component_area_option = models.ManyToManyField(
        Course, related_name='component_area_option_courses', blank=True)
    cis_requirements = models.ManyToManyField(
        Course, related_name='cis_requirements_courses', blank=True)
    advanced_cidm_electives = models.ManyToManyField(
        Course, related_name='advanced_cidm_electives_courses', blank=True)

    # Add the nine_hours_from field
    nine_hours_from = models.ManyToManyField(
        Course, related_name='nine_hours_from_courses', blank=True)


class Advisor(models.Model):
    name = models.CharField(max_length=255)
    contact_information = models.CharField(max_length=255)
