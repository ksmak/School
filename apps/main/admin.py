# Django
from django.contrib import admin

# Project
from .models import (
    Teacher,
    Student,
    Group,
    Subject,
    Lecture,
    Mark
)


admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(Lecture)
admin.site.register(Mark)
