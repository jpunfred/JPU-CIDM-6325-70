from django.urls import path
from . import views

app_name = 'degree_checklist'

urlpatterns = [
    path('student_checklist/<int:student_id>/', views.student_checklist, name='student_checklist'),
    path('course_list/', views.course_list, name='course_list'),
    path('advisor_details/<int:advisor_id>/', views.advisor_details, name='advisor_details'),
]
