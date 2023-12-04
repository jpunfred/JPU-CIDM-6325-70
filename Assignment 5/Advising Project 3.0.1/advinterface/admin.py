from django.contrib import admin
from .models import Major, UserProfile, Advisor, Course

@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'buff_id', 'major']

@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_information']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
  list_display = ['class_code', 'name', 'credit_hours', 'section']
  list_filter = ['section']



