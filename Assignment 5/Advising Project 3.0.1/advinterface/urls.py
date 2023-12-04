from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('classes/<int:user_id>/', views.classes, name='classes'),
    path('submit/', views.submit, name='submit'),
]
