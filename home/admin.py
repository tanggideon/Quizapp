from django.contrib import admin
from .models import Student, Lecturer, Course

# Register your models here.

class CourseInline(admin.StackedInline):
    model = Course

class LectureAdmin(admin.ModelAdmin):
    inlines = [CourseInline]

class CourseAdmin(admin.ModelAdmin):
    list_display = ["course_title", "course_code", "lecturer"]


admin.site.register(Student)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lecturer, LectureAdmin)

