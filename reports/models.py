from django.db import models
from home.models import BaseModel, Student
from quiz.models import Quiz


class QuizAttempts(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="quiz")
    choices = models.JSONField()
    score = models.IntegerField()
    total_marks = models.IntegerField()
    passed = models.BooleanField(default=False)

    def __str__(self):
        return self.quiz.category
    