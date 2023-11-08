from django.shortcuts import render, redirect
from .models import Student, Curriculum, Course, EnrolledCourse, Advisor
from django.http import HttpResponse

# View to display a student's checklist
def student_checklist(request, student_id):
    student = Student.objects.get(id=student_id)
    enrolled_courses = EnrolledCourse.objects.filter(student=student)
    curriculum = Curriculum.objects.get(id=student.curriculum.id)
    advisor = Advisor.objects.get(id=student.advisor.id)
    return render(request, 'student_checklist.html', {'student': student, 'enrolled_courses': enrolled_courses, 'curriculum': curriculum, 'advisor': advisor})

# View to display a list of available courses
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

# View to enroll a student in a course
def enroll_course(request, student_id, course_id):
    student = Student.objects.get(id=student_id)
    course = Course.objects.get(id=course_id)
    
    # Add the logic to enroll the student in the course here
    
    return redirect('student_checklist', student_id=student_id)

# View to update a student's grade for a specific course
def update_grade(request, enrolled_course_id):
    enrolled_course = EnrolledCourse.objects.get(id=enrolled_course_id)
    
    if request.method == 'POST':
        new_grade = request.POST.get('new_grade')
        enrolled_course.grade = new_grade
        enrolled_course.save()
        return redirect('student_checklist', student_id=enrolled_course.student.id)
    
    return render(request, 'update_grade.html', {'enrolled_course': enrolled_course})

# View to display advisor details
def advisor_details(request, advisor_id):
    advisor = Advisor.objects.get(id=advisor_id)
    return render(request, 'advisor_details.html', {'advisor': advisor})
