from django.urls import path
from . import views

urlpatterns = [
    path("", views.quizzes, name="quizzes"),
    path("quiz/<str:pk>/", views.quiz, name="quiz"),
    path("quiz/success", views.success, name="success"),
    path("quiz/new-quiz", views.new_quiz, name="new_quiz"),
]