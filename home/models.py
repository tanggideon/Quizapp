from django.db import models
from django.contrib.auth.models import User
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class BaseInfo(models.Model):
    middle_name = models.CharField(max_length=256, null=True, blank=True)
    id = models.CharField(max_length=11)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    

    class Meta:
        abstract = True


class Student(BaseModel, BaseInfo):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student")
    cummulative = models.DecimalField(max_digits=3, decimal_places=2, default=4.00, editable=False)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True)


position = [
    ('Prof.', ' Professor'),
    ('Ass. Prof', 'Associate Professor'),
    ('Lecturer', 'Lecturer'),
    ('Dr.', 'Doctor'),
    ('Ass. Lecturer', 'Assistant Lecturer'),
]


class Lecturer(BaseModel, BaseInfo):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lecturer")
    position = models.CharField(max_length=21, choices=position)



class Course(BaseModel):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, null=True)
    course_title = models.CharField(max_length=256)
    course_code = models.CharField(max_length=8, null=True)
    credit_hours = models.IntegerField()
    students = models.ManyToManyField(Student, related_name='coursestudents')
    

    def __str__(self) -> str:
        return self.course_title    

