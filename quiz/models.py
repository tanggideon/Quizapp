from django.db import models
from home.models import BaseModel, Course
from django.utils import timezone
import uuid


class Category(models.Model):
    category_name = models.CharField(max_length=32)
    require_qrcode = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'


class Quiz(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='category', null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    duration = models.IntegerField(help_text='Enter Time in Minutes')
    number_of_questions = models.IntegerField(null=True)
    due_by = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return f"{self.category} ------- {self.course}"

    def overdue(self):
        return timezone.now() >= self.due_by

    class Meta:
        verbose_name_plural = 'Quizzes'


class Instruction(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='quizinstruction', on_delete=models.CASCADE)
    text = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.text


class Question(BaseModel):
    quiz = models.ForeignKey('Quiz',on_delete=models.CASCADE, null=True, related_name='quizquestions')
    text = models.CharField(max_length=512, null=False)
    upload_required = models.BooleanField(default=False)
    mark = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.text


class Answer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name='questionanswer')
    text = models.CharField(max_length=256, null=False)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question} ------- {self.text}"
    