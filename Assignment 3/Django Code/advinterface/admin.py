from django.contrib import admin
from .models import Major, Student, Class, Advisor, NineHoursFrom, UCComm, UCMathSocial, UCComponent

admin.site.register(Major)
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(UCComm)
admin.site.register(UCComponent)
admin.site.register(UCMathSocial)
admin.site.register(NineHoursFrom)
admin.site.register(Advisor)
